"""진도 확인 도구입니다. 이 파일은 고치지 않아도 됩니다.

VS Code 터미널에서 `python3 next.py`를 실행하면 지금 할 일을 알려 줍니다.
- 연습 문제와 주간 과제는 테스트 결과로 자동으로 확인합니다.
- 실습 일지는 학생이 직접 씁니다. 일지를 썼는지와 커밋/푸시는 자동으로 확인합니다.
- 테스트로 확인할 수 없는 단계(수업 읽기 등)는 질문으로 확인합니다.

결과는 progress/state.json과 PROGRESS.md에 저장됩니다.
GitHub 자동 테스트에서 실행하면 질문하지 않습니다. 진도표를 실행 요약에 쓰고, 시작한 일차의 테스트만 실행합니다.
"""

import datetime
import json
import os
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
PROGRESS_DIR = ROOT / "progress"
STATE_FILE = PROGRESS_DIR / "state.json"
REPORT_FILE = ROOT / "PROGRESS.md"
TEST_TIMEOUT = 120  # 초
ON_GITHUB = bool(os.environ.get("GITHUB_ACTIONS"))  # GitHub 자동 테스트에서 실행 중입니다.


def load_json(path, default):
    try:
        return json.loads(path.read_text(encoding="utf-8-sig"))
    except (FileNotFoundError, json.JSONDecodeError):
        return default


def load_state():
    """진도 파일을 읽습니다. 파일이 없으면 새 진도, 읽을 수 없으면 None을 돌려줍니다."""
    if not STATE_FILE.exists():
        return {"done": []}
    try:
        state = json.loads(STATE_FILE.read_text(encoding="utf-8-sig"))
    except (OSError, ValueError):
        return None
    done = state.get("done") if isinstance(state, dict) else None
    if not isinstance(done, list) or not all(isinstance(x, str) for x in done):
        return None
    counts = state.get("log_lines", {})
    if not isinstance(counts, dict) or not all(
            type(n) is int and n >= 0 for n in counts.values()):
        return None
    return state


MSG = load_json(PROGRESS_DIR / "messages.json", {})


def load_weeks():
    """progress/weekN_steps.json 파일을 주차 순서대로 읽습니다."""
    files = sorted(PROGRESS_DIR.glob("week*_steps.json"),
                   key=lambda p: int(p.stem[4:].split("_")[0]))
    return [load_json(p, None) for p in files]


def run_tests(paths):
    """pytest를 한 번 실행하고 {테스트 id: 통과 여부}를 돌려줍니다."""
    cmd = [sys.executable, "-m", "pytest", *paths, "-q", "-p", "no:cacheprovider",
           "--tb=no", "--color=no", "-rpfE",
           # 한 파일에 문법 오류가 있어도 나머지 테스트는 실행합니다.
           "--continue-on-collection-errors"]
    try:
        run = subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True,
                             encoding="utf-8", errors="replace", timeout=TEST_TIMEOUT)
    except subprocess.TimeoutExpired:
        return None, "timeout"
    except KeyboardInterrupt:
        return None, "cancelled"
    if "No module named pytest" in run.stderr:
        return None, "no_pytest"
    results = {}
    for line in run.stdout.splitlines():
        for word, ok in (("PASSED ", True), ("FAILED ", False), ("ERROR ", False)):
            if line.startswith(word):
                node = line[len(word):].split(" - ")[0].strip()
                results[node] = ok
    return results, None


def test_passed(step, results):
    """step의 테스트(경로와 -k 조건)에 해당하는 테스트가 모두 통과했는지 확인합니다."""
    matched = []
    k = step.get("k", "").lower()
    for node, ok in results.items():
        path, _, name = node.partition("::")
        in_path = any(path == p or path.startswith(p.rstrip("/") + "/") for p in step["paths"])
        if in_path and k in name.lower():
            matched.append(ok)
    return bool(matched) and all(matched)


def bullet_has_text(line):
    """`- ` 줄에 내용이 있으면 True입니다. 빈 체크 상자(`- [ ]`)만 있는 줄은 빈칸으로 봅니다.

    VS Code가 저장할 때 줄 끝 공백을 지우면 `- `가 `-`로 바뀌므로, `-` 뒤에 공백이 없어도 인정합니다.
    """
    line = line.strip()
    if not line.startswith("-") or set(line) <= {"-", " ", "\t"}:
        return False  # `-`로 시작하지 않거나, `- - -` 같은 구분선입니다.
    text = line.lstrip("-").strip()
    if text[:3].lower() in ("[ ]", "[x]"):
        text = text[3:].strip()
    return bool(text) and LOG_MARK not in text  # ✏️ 안내 글만 있는 줄은 빈칸입니다.


def log_lines_filled():
    """오늘 날짜의 실습 일지에서 내용을 적은 `-` 줄의 수입니다. 파일이 없으면 0입니다."""
    today = ROOT / "logs" / f"{datetime.date.today():%Y-%m-%d}.md"
    if not today.exists():
        return 0
    text = today.read_text(encoding="utf-8-sig", errors="replace")
    return sum(bullet_has_text(line) for line in text.splitlines())


# 일지 양식에서 채울 곳에는 ✏️ 표시가 있습니다.
LOG_MARK = "✏"
# 일지 양식의 빈칸입니다. 공백을 지운 줄에 남아 있으면 아직 채우지 않은 것입니다.
# ✏️ 표시만 지우고 안내 글을 남긴 줄과 예전 양식의 빈칸도 셉니다.
LOG_PLACEHOLDERS = (LOG_MARK, "YYYY-MM-DD",
                    "오늘배운것한가지", "수업파일맨위의제목",
                    "해결방법(없으면", "물어볼질문(없으면", "약몇시간",
                    "Somethingyoulearnedtoday", "titleatthetopofthelesson",
                    "solvedit(ifnone", "foryourmentor(ifnone", "Abouthowmanyhours",
                    "_주차", "_일차", "(수업제목)", "약_시간",
                    "Week_", "Day_", "(lessontitle)", "About_hours")


def is_bullet(line):
    """`-`로 시작하는 줄이면 True입니다. `---` 같은 구분선은 제외합니다."""
    line = line.strip()
    return line.startswith("-") and not (line.count("-") >= 3 and set(line) <= {"-", " ", "\t"})


def log_missing():
    """오늘 일지에서 아직 채우지 않은 줄의 (줄 번호, 줄 내용) 목록입니다.

    제목 줄과 `## ` 절 아래의 줄만 봅니다. 빈칸(✏️ 표시, `YYYY-MM-DD`, 빈 `-` 줄)이
    남은 줄을 셉니다. 절의 내용을 모두 지웠으면 그 절의 제목 줄을 셉니다.
    예전 양식의 연습 문제 표(`|`로 시작하는 줄)는 확인하지 않습니다.
    """
    today = ROOT / "logs" / f"{datetime.date.today():%Y-%m-%d}.md"
    if not today.exists():
        return []
    missing, heading, has_text = [], None, False
    for number, line in enumerate(today.read_text(encoding="utf-8-sig", errors="replace").splitlines(), 1):
        squeezed = "".join(line.split())
        if line.startswith("## "):
            if heading and not has_text:
                missing.append(heading)
            heading, has_text = (number, line + MSG["log_empty_section"]), False
        elif line.startswith("# ") or heading:
            has_text = has_text or bool(squeezed)
            if squeezed.startswith("|"):
                continue
            if (any(p in squeezed for p in LOG_PLACEHOLDERS)
                    or (is_bullet(line) and not bullet_has_text(line))):
                missing.append((number, line.strip()))
    if heading and not has_text:
        missing.append(heading)
    return sorted(missing)


def log_written(state):
    """오늘 일지에 내용을 적었으면 True입니다.

    같은 날짜에 일지 단계를 이미 마쳤다면(하루에 두 일차를 공부한 경우) 그때보다 줄이 늘어야 합니다.
    """
    seen = state.get("log_lines")
    seen = seen.get(f"{datetime.date.today():%Y-%m-%d}", 0) if isinstance(seen, dict) else 0
    return log_lines_filled() > (seen if isinstance(seen, int) else 0)


def record_log(state):
    """일지 단계를 마칠 때 오늘 일지의 줄 수를 기록합니다."""
    if not isinstance(state.get("log_lines"), dict):
        state["log_lines"] = {}
    state["log_lines"][f"{datetime.date.today():%Y-%m-%d}"] = log_lines_filled()


def git(*args):
    return subprocess.run(["git", *args], cwd=ROOT, capture_output=True, text=True,
                          encoding="utf-8", errors="replace")


def pushed():
    """커밋하지 않은 변경이 없고, 푸시하지 않은 커밋도 없으면 True입니다."""
    status = git("status", "--porcelain")
    if status.returncode != 0 or status.stdout.strip():
        return False
    ahead = git("rev-list", "--count", "@{u}..HEAD")
    return ahead.returncode == 0 and ahead.stdout.strip() == "0"


def started_test_paths(weeks, state):
    """학생이 시작한 일차(단계를 하나라도 마친 일차)의 테스트 경로입니다. GitHub 자동 테스트에서 사용합니다."""
    paths = []
    for week in weeks:
        for sec in week["sections"]:
            steps = [s for s in week["steps"] if s["section"] == sec["key"]]
            if any(s["id"] in state["done"] for s in steps):
                for s in steps:
                    if s["kind"] == "test":
                        paths += [p for p in s["paths"] if p not in paths]
    return paths


def github_check(weeks, state, results, error):
    """GitHub 자동 테스트에서 실행합니다. 종료 코드가 커밋의 ✅/❌를 정합니다.

    진도표를 실행 요약 페이지에 쓰고, 시작한 일차의 테스트만 실행합니다.
    아직 시작하지 않은 일차의 연습 문제 때문에 ❌가 나오지 않게 합니다.
    """
    # 이 커밋은 이미 푸시된 것입니다. 지금 할 단계가 커밋과 푸시라면 마친 것으로 표시합니다.
    _, cur = current_step(weeks, state, results)
    if cur and cur["kind"] == "git":
        state["done"].append(cur["id"])
    table = report(weeks, state, results)
    if error:
        table = f"> {MSG[error]}\n\n{table}"
    summary = os.environ.get("GITHUB_STEP_SUMMARY")
    if summary:
        with open(summary, "a", encoding="utf-8") as f:
            f.write(table + "\n")
    else:
        print(table)

    paths = started_test_paths(weeks, state)
    if not paths:
        print(MSG["ci_none"])
        return 0
    cmd = [sys.executable, "-m", "pytest", "-rA", "--continue-on-collection-errors", *paths]
    try:
        return subprocess.run(cmd, cwd=ROOT, timeout=TEST_TIMEOUT).returncode
    except subprocess.TimeoutExpired:
        # 끝나지 않는 반복문이 있어도 GitHub 검사가 멈춰 있지 않고 ❌로 끝나게 합니다.
        print(MSG["timeout"])
        return 1


def is_done(step, state, results):
    kind = step["kind"]
    if kind == "test":
        passed = results is not None and test_passed(step, results)
        # 하루 전체 테스트(질문이 있는 단계)는 통과한 뒤 질문에 y로 답해야 끝납니다.
        return passed and (not step.get("ask") or step["id"] in state["done"])
    return step["id"] in state["done"]


def keep_old_progress(weeks, state):
    """이전 next.py의 진도를 지금 단계 순서에 맞춥니다.

    - 이전에는 하루 전체 테스트를 묻지 않았습니다. 그 뒤 단계를 이미 마쳤다면 마친 것으로 봅니다.
    - 이전에는 커밋과 푸시가 멘토 점검보다 먼저였습니다. 같은 일차에 마치지 않은 단계가 앞에 남아 있으면
      커밋과 푸시를 다시 하게 합니다. 그래야 멘토 점검 답도 GitHub로 갑니다.
    """
    for week in weeks:
        steps = week["steps"]
        for i, step in enumerate(steps):
            if step["kind"] == "test" and step.get("ask") and step["id"] not in state["done"]:
                if any(s["id"] in state["done"] for s in steps[i + 1:]):
                    state["done"].append(step["id"])
        for i, step in enumerate(steps):
            if step["kind"] == "git" and step["id"] in state["done"]:
                before = [s for s in steps[:i] if s["section"] == step["section"] and s["kind"] in ("manual", "log")]
                if any(s["id"] not in state["done"] for s in before):
                    state["done"].remove(step["id"])


def current_step(weeks, state, results):
    for week in weeks:
        for step in week["steps"]:
            if not is_done(step, state, results):
                return week, step
    return None, None


def ask(question):
    try:
        answer = input(f"{question} {MSG['yes_no']} ").strip().lower()
    except (EOFError, KeyboardInterrupt):
        print()
        return False
    return answer in ("y", "yes", "ㅛ")


def section_title(week, key):
    return next(s["title"] for s in week["sections"] if s["key"] == key)


def print_overview(weeks, state, results, cur):
    for week in weeks:
        steps = week["steps"]
        done = sum(is_done(s, state, results) for s in steps)
        print(f"\n{week['title']}  {MSG['progress'].format(done=done, total=len(steps))}")
        for sec in week["sections"]:
            sec_steps = [s for s in steps if s["section"] == sec["key"]]
            if all(is_done(s, state, results) for s in sec_steps):
                mark = "✔"
            elif cur in sec_steps:
                mark = "▶"
            else:
                mark = " "
            print(f"  {mark} {sec['title']}")


def print_step(week, step):
    print(f"\n▶ {MSG['now']} ({section_title(week, step['section'])}): {step['label']}")
    for path in step.get("open", []):
        path = path.replace("{today}", f"{datetime.date.today():%Y-%m-%d}")
        print(f"   {MSG['open']}: {path}")
    if step.get("cmd"):
        print(f"   {MSG['test']}: {step['cmd']}")
    if step.get("note"):
        print(f"   {step['note']}")


def report(weeks, state, results):
    """PROGRESS.md와 GitHub 요약에 쓰는 진도표(Markdown)를 만듭니다."""
    _, cur = current_step(weeks, state, results)
    lines = [f"# {MSG['report_title']}", "", MSG["report_note"], ""]
    if cur:
        lines += [f"**{MSG['now']}:** {cur['label']}", ""]
    for week in weeks:
        steps = week["steps"]
        done = sum(is_done(s, state, results) for s in steps)
        lines += [f"## {week['title']} ({done} / {len(steps)})", ""]
        for sec in week["sections"]:
            lines += [f"### {sec['title']}", ""]
            for s in steps:
                if s["section"] != sec["key"]:
                    continue
                mark = "✅" if is_done(s, state, results) else ("▶️" if s is cur else "⬜")
                lines.append(f"- {mark} {s['label']}")
            lines.append("")
    return "\n".join(lines)


def save(state, weeks, results):
    STATE_FILE.write_text(json.dumps(state, ensure_ascii=False, indent=2) + "\n",
                          encoding="utf-8", newline="\n")
    REPORT_FILE.write_text(report(weeks, state, results), encoding="utf-8", newline="\n")


def main():
    weeks = [w for w in load_weeks() if w]
    state = load_state()
    if state is None:
        # 읽을 수 없는 진도 파일을 덮어쓰지 않습니다.
        print(MSG["bad_state"])
        # GitHub 자동 테스트에서는 ❌로 알립니다.
        sys.exit(1 if ON_GITHUB else 0)
    paths = sorted({p for w in weeks for s in w["steps"] if s["kind"] == "test" for p in s["paths"]})
    if not ON_GITHUB:
        print(MSG["checking"], flush=True)
    results, error = run_tests(paths)
    # pytest가 실행되면 설치 및 준비가 끝난 것입니다.
    for week in weeks:
        for step in week["steps"]:
            if step["kind"] == "setup" and results is not None and step["id"] not in state["done"]:
                state["done"].append(step["id"])
    keep_old_progress(weeks, state)

    if ON_GITHUB:
        sys.exit(github_check(weeks, state, results, error))

    if error:
        # 테스트 결과를 모르면 진도를 저장하지 않습니다(이미 저장된 진도가 지워지지 않도록).
        print(MSG[error])
        return

    shown = False
    while True:
        week, step = current_step(weeks, state, results)
        # 실습 일지와 커밋/푸시는 지금 할 단계일 때만 자동으로 확인합니다.
        if step and step["kind"] == "log" and log_written(state) and not log_missing():
            record_log(state)
            state["done"].append(step["id"])
            continue
        if step and step["kind"] == "git" and pushed():
            state["done"].append(step["id"])
            continue

        if not shown:
            print_overview(weeks, state, results, step)
            shown = True
        if step is None:
            print(f"\n{MSG['all_done']}")
            break
        print_step(week, step)
        # 하루 전체 테스트는 통과해도 학생이 직접 실행했는지 묻습니다.
        if step.get("ask") and (step["kind"] == "manual" or test_passed(step, results)):
            if ask(step["ask"]):
                state["done"].append(step["id"])
                save(state, weeks, results)
                print(MSG["saved"])
                continue
            print(f"\n{MSG['come_back']}")
            break
        print(f"\n{MSG['after_' + step['kind']]}")
        missing = log_missing() if step["kind"] == "log" else []
        if missing:
            print(MSG["log_missing"])
            for number, line in missing:
                print(f"   logs/{datetime.date.today():%Y-%m-%d}.md:{number}   {line}")
            print(MSG["log_missing_hint"])
        break

    save(state, weeks, results)


if __name__ == "__main__":
    main()

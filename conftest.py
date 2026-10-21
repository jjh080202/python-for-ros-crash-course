"""테스트에서 함께 쓰는 도구입니다. 이 파일은 고치지 않아도 됩니다."""

import subprocess
import sys
from pathlib import Path

import pytest

# 모든 주차의 연습 문제와 주간 과제 폴더에서 파일을 불러올 수 있게 합니다.
_ROOT = Path(__file__).resolve().parent
for _folder in sorted(_ROOT.glob("exercises/week*")) + sorted(_ROOT.glob("checkpoints/week*")):
    sys.path.insert(0, str(_folder))


@pytest.fixture
def run_script():
    """터미널에서 실행하는 것처럼 파이썬 스크립트를 실행합니다.

    스크립트가 출력한 글자를 돌려줍니다. `stdin`은 사용자가 입력하는 내용입니다.
    """

    def _run(path: Path, stdin: str = "") -> str:
        try:
            result = subprocess.run(
                [sys.executable, "-X", "utf8", str(path)],
                input=stdin,
                capture_output=True,
                text=True,
                encoding="utf-8",
                timeout=10,
            )
        except subprocess.TimeoutExpired:
            result = None
        if result is None:
            pytest.fail(
                "스크립트가 10초 안에 끝나지 않았습니다.\n"
                "끝나지 않는 반복문이나 필요 없는 input()이 있는지 확인하세요.",
                pytrace=False,
            )
        if result.returncode != 0:
            pytest.fail(
                f"스크립트를 실행하다가 오류가 났습니다. 오류 메시지:\n\n{result.stderr}",
                pytrace=False,
            )
        return result.stdout

    return _run

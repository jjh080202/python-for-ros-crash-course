from pathlib import Path

import pytest

HERE = Path(__file__).parent.parent


def last_line(output):
    lines = output.strip().splitlines()
    return lines[-1] if lines else ""


@pytest.mark.parametrize(
    "capacity, current, expected",
    [
        ("5000", "2000", "Runtime: 2.50 hours"),
        ("1000", "6000", "Runtime: 0.17 hours"),
        ("1500", "3030", "Runtime: 0.50 hours"),
    ],
)
def test_battery_runtime(run_script, capacity, current, expected):
    output = run_script(HERE / "w1d2_battery_runtime.py", f"{capacity}\n{current}\n")
    assert last_line(output)[-len(expected):] == expected, (
        f"용량 {capacity} mAh, 전류 {current} mA일 때 마지막 줄은 {expected!r}로 끝나야 합니다.\n"
        f"프로그램이 출력한 내용: {output!r}"
    )


@pytest.mark.parametrize(
    "seconds, expected",
    [
        ("3721", "1 h 2 m 1 s"),
        ("216000", "60 h 0 m 0 s"),
        ("7199", "1 h 59 m 59 s"),
    ],
)
def test_time_format(run_script, seconds, expected):
    output = run_script(HERE / "w1d2_time_format.py", f"{seconds}\n")
    assert last_line(output)[-len(expected):] == expected, (
        f"{seconds}초일 때 마지막 줄은 {expected!r}로 끝나야 합니다.\n"
        f"프로그램이 출력한 내용: {output!r}"
    )

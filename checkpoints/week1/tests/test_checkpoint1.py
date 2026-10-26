import math

import pytest

import converter
import guess


def fake_input(answers):
    """사용자가 `answers`를 하나씩 입력하는 것처럼 흉내 냅니다."""
    remaining = list(answers)

    def _input(prompt=""):
        print(prompt, end="")
        if not remaining:
            pytest.fail("프로그램이 예상보다 더 많이 입력을 요청했습니다. (반복문이 제대로 멈춥니까?)")
        return remaining.pop(0)

    return _input


# ---- converter.py -------------------------------------------------------

def test_c_to_f():
    assert converter.c_to_f(100) == pytest.approx(212)
    assert converter.c_to_f(0) == pytest.approx(32)
    assert converter.c_to_f(-40) == pytest.approx(-40)


def test_f_to_c():
    assert converter.f_to_c(32) == pytest.approx(0)
    assert converter.f_to_c(212) == pytest.approx(100)


def test_mm_to_m():
    assert converter.mm_to_m(1500) == pytest.approx(1.5)
    assert converter.mm_to_m(0) == pytest.approx(0)


def test_deg_to_rad():
    assert converter.deg_to_rad(180) == pytest.approx(math.pi)
    assert converter.deg_to_rad(90) == pytest.approx(math.pi / 2)


def test_converter_menu(monkeypatch, capsys):
    monkeypatch.setattr("builtins.input", fake_input(["1", "100", "4", "180", "3", "250", "7", "q"]))
    converter.main()
    out = capsys.readouterr().out
    assert "=== Unit Converter ===" in out
    assert "Result: 212.00" in out
    assert "Result: 3.14" in out
    assert "Result: 0.25" in out
    assert "Unknown choice." in out
    assert out.rstrip().endswith("Bye!")


def test_converter_accepts_decimals(monkeypatch, capsys):
    monkeypatch.setattr("builtins.input", fake_input(["2", "98.6", "q"]))
    converter.main()
    assert "Result: 37.00" in capsys.readouterr().out


# ---- guess.py -----------------------------------------------------------

@pytest.mark.parametrize(
    "secret, g, expected",
    [(42, 10, "Too low"), (42, 99, "Too high"), (42, 42, "Correct!")],
)
def test_check_guess(secret, g, expected):
    assert guess.check_guess(secret, g) == expected


def test_guess_game(monkeypatch, capsys):
    calls = []

    def fake_randint(a, b):
        calls.append((a, b))
        return 42

    monkeypatch.setattr(guess.random, "randint", fake_randint)
    monkeypatch.setattr("builtins.input", fake_input(["50", "abc", "25", "42"]))
    guess.main()
    out = capsys.readouterr().out
    for text in ["Too high", "Please enter a number.", "Too low", "Correct!", "You got it in 3 tries!"]:
        assert text in out, f"출력에서 {text!r}을(를) 찾지 못했습니다"
    assert calls == [(1, 100)], "정답은 반복문 앞에서 random.randint(1, 100)으로 한 번만 고르세요"


def test_guess_game_first_try(monkeypatch, capsys):
    monkeypatch.setattr(guess.random, "randint", lambda a, b: 7)
    monkeypatch.setattr("builtins.input", fake_input(["7"]))
    guess.main()
    assert "You got it in 1 tries!" in capsys.readouterr().out

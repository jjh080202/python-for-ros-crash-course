# 1주차 주간 과제 1부: 단위 변환기
# 먼저 checkpoints/week1/README.md를 읽으세요.
#
# 실행(VS Code 터미널): `python3 checkpoints/week1/converter.py`
# 테스트(VS Code 터미널): 단계별 명령은 README에 있습니다. 전체는 `pytest checkpoints/week1`

import math


def c_to_f(c):
    # TODO: 이 줄 아래에 코드를 작성하세요
    return c * 9 / 5 + 32


def f_to_c(f):
    # TODO: 이 줄 아래에 코드를 작성하세요
    return (f - 32) * 5 / 9


def mm_to_m(mm):
    # TODO: 이 줄 아래에 코드를 작성하세요
    return mm / 1000


def deg_to_rad(deg):
    # TODO: 이 줄 아래에 코드를 작성하세요
    return deg * math.pi / 180


def main():
    # 메뉴 반복문(README의 2단계 참고)
    # TODO: 이 줄 아래에 코드를 작성하세요
    while True:
        print("=== Unit Converter ===")
        print("1) Celsius -> Fahrenheit")
        print("2) Fahrenheit -> Celsius")
        print("3) Millimeters -> Meters")
        print("4) Degrees -> Radians")
        print("q) Quit")
        choice = input("Choose: ")

        if choice == "q":
            print("Bye!")
            break
        if choice == "1":
            value = float(input("Value: "))
            print(f"Result: {c_to_f(value):.2f}")
        elif choice == "2":
            value = float(input("Value: "))
            print(f"Result: {f_to_c(value):.2f}")
        elif choice == "3":
            value = float(input("Value: "))
            print(f"Result: {mm_to_m(value):.2f}")
        elif choice == "4":
            value = float(input("Value: "))
            print(f"Result: {deg_to_rad(value):.2f}")
        else:
            print("Unknown choice.")


# 아래 두 줄은 그대로 두세요. 이 파일을 실행하면 main()을 호출하는 시작 장치입니다.
# 코드는 main() 안에 작성하세요. 맨 아래에는 코드를 추가하지 마세요.
# 정확히 어떻게 동작하는지는 3주차에 배웁니다.
if __name__ == "__main__":
    main()

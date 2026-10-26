# 1주차 주간 과제 2부: 숫자 맞히기 게임
# 먼저 checkpoints/week1/README.md를 읽으세요.
#
# 실행(VS Code 터미널): `python3 checkpoints/week1/guess.py`
# 테스트(VS Code 터미널): 단계별 명령은 README에 있습니다. 전체는 `pytest checkpoints/week1`

import random


def check_guess(secret, guess):
    # TODO: 이 줄 아래에 코드를 작성하세요
    if guess < secret:
        return "Too low"
    elif guess > secret:
        return "Too high"
    else:
        return "Correct!"


def main():
    # 게임 반복문(README의 2부 2단계 참고)
    # TODO: 이 줄 아래에 코드를 작성하세요
    secret = random.randint(1, 100)
    tries = 0

    while True:
        user_input = input("Your guess: ")
        if not user_input.isdigit():
            print("Please enter a number.")
            continue

        guess = int(user_input)
        tries += 1
        result = check_guess(secret, guess)
        print(result)
        if result == "Correct!":
            print(f"You got it in {tries} tries!")
            break


# 아래 두 줄은 그대로 두세요. 이 파일을 실행하면 main()을 호출하는 시작 장치입니다.
# 코드는 main() 안에 작성하세요. 맨 아래에는 코드를 추가하지 마세요.
# 정확히 어떻게 동작하는지는 3주차에 배웁니다.
if __name__ == "__main__":
    main()

# 1주차 4일차: for 문과 while 문으로 반복하기
#
# 각 함수의 `pass`를 코드로 바꾸세요.
#
# 테스트(VS Code 터미널): 함수 하나는 수업에 나온 `-k` 명령으로,
#   모든 함수를 마친 뒤에는 `pytest exercises/week1/tests/test_w1d4.py`


def countdown(n):
    """n부터 1까지 거꾸로 센 뒤 "GO!"가 붙는 문자열을 반환하세요.

    숫자는 공백 한 칸으로 구분합니다.

    예:
        countdown(3)은 "3 2 1 GO!"를 반환합니다
        countdown(0)은 "GO!"를 반환합니다

    힌트: 빈 문자열로 시작해서 for 문 안에서 내용을 붙이세요.
    """
    # TODO: 이 줄 아래에 코드를 작성하세요
    text = ""
    for i in range(n, 0, -1):
        text += str(i) + " "
    text += "GO!"
    return text
    pass


def sum_to(n):
    """1 + 2 + ... + n을 반환하세요. 공식 대신 반복문을 사용하세요.

    예:
        sum_to(4)는 10을 반환합니다
        sum_to(0)은 0을 반환합니다
    """
    # TODO: 이 줄 아래에 코드를 작성하세요
    result = 0
    for i in range(1, n + 1):
        result += i
    return result
    pass


def steps_until_low(battery, drain_per_step, low_level):
    """로봇은 한 단계마다 배터리를 `drain_per_step`만큼 사용합니다.

    배터리가 `low_level` 이하가 될 때까지 몇 단계가 걸리는지 세세요.
    while 문을 사용하세요.

    예:
        steps_until_low(100, 10, 50)은 5를 반환합니다   (100 -> 90 -> 80 -> 70 -> 60 -> 50)
        steps_until_low(100, 7, 20)은 12를 반환합니다
        steps_until_low(10, 5, 20)은 0을 반환합니다     (이미 기준 이하입니다)
    """
    # TODO: 이 줄 아래에 코드를 작성하세요
    steps = 0
    while battery > low_level:
        battery -= drain_per_step
        steps += 1
    return steps
    pass

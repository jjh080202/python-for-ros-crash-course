# 1주차 2일차 연습 문제 2: 임무 타이머
#
# 임무 기록에는 시간을 초 단위로 저장합니다. 사람은 시간, 분, 초로
# 나누어 보는 게 더 편합니다.
#
# 1. 초 단위 시간을 입력받으세요:   Seconds:
# 2. 아래처럼 시간, 분, 초로 나누어 출력하세요.
#
#     1 h 2 m 5 s
#
# 예: 3725초이면 "1 h 2 m 5 s"가 나옵니다.
#
# 힌트: //는 나눗셈의 몫이고 %는 나머지입니다.
#       1시간은 3600초이고 1분은 60초입니다.
#
# 실행(VS Code 터미널): `python3 exercises/week1/w1d2_time_format.py`
# 테스트(VS Code 터미널): `pytest exercises/week1/tests/test_w1d2.py -k time_format`

# TODO: 이 줄 아래에 코드를 작성하세요
total_seconds = int(input("Seconds:"))
hours = total_seconds // 3600
remaining_seconds = total_seconds % 3600
minutes = remaining_seconds // 60
seconds = remaining_seconds % 60
print(f"{hours} h {minutes} m {seconds} s")
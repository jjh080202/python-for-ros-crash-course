# 1주차 5일차: 문자열 다루기
#
# 각 함수의 `pass`를 코드로 바꾸세요.
#
# 테스트(VS Code 터미널): 함수 하나는 수업에 나온 `-k` 명령으로,
#   모든 함수를 마친 뒤에는 `pytest exercises/week1/tests/test_w1d5.py`


def clean_command(text):
    """양 끝의 공백과 줄바꿈을 없애고 소문자로 바꾸세요.

    예: clean_command("  FORWARD \n")는 "forward"를 반환합니다
    """
    # TODO: 이 줄 아래에 코드를 작성하세요
    return text.strip().lower()
    pass


def make_topic_name(robot_name, sensor):
    """ROS 방식의 토픽 이름을 만드세요.

    규칙: 모두 소문자로 바꾸고, 공백을 "_"로 바꾸고,
    "/<robot>/<sensor>" 형태로 이어 붙이세요.

    예: make_topic_name("Rail Robot 1", "LiDAR")는 "/rail_robot_1/lidar"를 반환합니다
    """
    # TODO: 이 줄 아래에 코드를 작성하세요
    robot_name = robot_name.lower().replace(" ", "_")
    sensor = sensor.lower().replace(" ", "_")
    return f"/{robot_name}/{sensor}"
    pass


def is_valid_robot_id(robot_id):
    """robot_id가 대문자 두 개, "-", 숫자 네 개 순서이면 True, 아니면 False를 반환하세요.
    앞의 두 글자가 꼭 "RR"일 필요는 없습니다. "WR-1234"도 올바른 식별 번호입니다.

    올바른 식별 번호는 다음과 같습니다.
    - 길이가 정확히 7글자입니다
    - 대문자 두 개로 시작합니다
    - 세 번째 글자는 "-"입니다
    - 숫자 네 개로 끝납니다

    예:
        is_valid_robot_id("RR-0042")는 True를 반환합니다
        is_valid_robot_id("WR-1234")는 True를 반환합니다
        is_valid_robot_id("rr-0042")는 False를 반환합니다
        is_valid_robot_id("RR0042")는 False를 반환합니다

    힌트: len(), robot_id[0:2] 같은 슬라이싱,
          .isalpha(), .isupper(), .isdigit() 메서드를 사용하세요
    """
    # TODO: 이 줄 아래에 코드를 작성하세요
    if len(robot_id) != 7:
        return False
    if not (robot_id[0:2].isalpha() and robot_id[0:2].isupper()):
        return False
    if robot_id[2] != "-":
        return False
    if not robot_id[3:7].isdigit():
        return False
    return True
    pass

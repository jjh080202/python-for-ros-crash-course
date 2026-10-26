import pytest

from w1d5_strings import clean_command, is_valid_robot_id, make_topic_name


@pytest.mark.parametrize(
    "text, expected",
    [("  FORWARD \n", "forward"), ("Stop", "stop"), ("\tturn LEFT  ", "turn left")],
)
def test_clean_command(text, expected):
    assert clean_command(text) == expected


@pytest.mark.parametrize(
    "robot, sensor, expected",
    [
        ("Rail Robot 1", "LiDAR", "/rail_robot_1/lidar"),
        ("drone", "Camera", "/drone/camera"),
        ("Wire Robot", "imu data", "/wire_robot/imu_data"),
    ],
)
def test_make_topic_name(robot, sensor, expected):
    assert make_topic_name(robot, sensor) == expected


@pytest.mark.parametrize(
    "robot_id, expected",
    [
        ("RR-0042", True), ("WR-1234", True),
        ("rr-0042", False), ("RR0042", False), ("RR-00420", False),
        ("RR_0042", False), ("R1-0042", False), ("RR-004A", False), ("", False),
    ],
)
def test_is_valid_robot_id(robot_id, expected):
    assert is_valid_robot_id(robot_id) is expected

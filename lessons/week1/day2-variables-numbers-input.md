# 1주차 · 2일차: 변수, 숫자, 입력

**배울 내용:** 변수에 값을 저장하는 방법, 주요 자료형, 파이썬 계산, 사용자 입력 받기, 숫자를 보기 좋게 표시하는 방법을 배웁니다.

**로봇을 다룰 때 필요한 이유:** 로봇은 라이다 거리, 배터리 전압, 바퀴 속도, 각도처럼 수많은 숫자를 다룹니다. 코드는 이 숫자를 변수에 저장하고 계산한 뒤 사람이 볼 수 있게 보여 줍니다.

---

## 1. 변수

**변수**는 값에 붙인 이름입니다. 이름표를 붙인 상자라고 생각해 보세요.

오늘도 1일차처럼 예제를 `playground.py`에서 실행합니다. VS Code 터미널에 `code playground.py`를 입력해서 `playground.py`를 여세요. **새 예제를 시작할 때마다 `playground.py`의 이전 내용을 모두 지우고 새 예제만 입력하세요.** **Ctrl + S**로 저장한 뒤 VS Code 터미널에서 `python3 playground.py`를 실행하세요. `>>>`가 붙은 예제와 `>>>`에 입력하라는 예제는 파일이 아니라 대화형 모드(`python3`)에서 실행합니다.

`playground.py`의 내용을 아래 코드로 바꾸고 실행하세요. `RR-01`과 `0.5`가 나와야 합니다.

```python
speed = 0.5
robot_name = "RR-01"
battery = 87

print(robot_name)
print(speed)
```

`=`는 **"오른쪽 값을 왼쪽 이름에 저장한다"**는 뜻입니다. 수학에서처럼 "같다"라는 뜻이 아닙니다.

변수의 값은 나중에 바꿀 수 있습니다.

```python
battery = 87
battery = battery - 10    # 기존 값에서 10을 빼고 다시 저장합니다
print(battery)            # 77
```

### 이름 짓는 규칙

- 소문자, 숫자, `_`를 사용하세요. `wheel_speed`, `max_distance`처럼 단어 사이에 `_`를 넣습니다. 이 방식을 **스네이크 표기법**(`snake_case`)이라고 하고, ROS에서도 널리 사용합니다.
- 이름은 숫자로 시작할 수 없습니다: `1st_robot` ❌, `robot_1` ✅
- 대소문자를 구분합니다. `Speed`와 `speed`는 서로 다른 변수입니다.
- 값을 잘 설명하는 이름을 고르세요. `d`나 `x`보다 `distance_m`이 좋습니다.

---

## 2. 자료형

모든 값에는 **자료형**이 있습니다.

| 자료형 | 이름 | 예 | 사용 예 |
|---|---|---|---|
| `int` | 정수(소수 부분이 없는 수) | `7`, `-3`, `5000` | 개수, 식별 번호, 배터리 % |
| `float` | 실수(소수점이 있는 수) | `0.5`, `3.14`, `-2.0` | 거리, 속도, 각도 |
| `str` | 문자열(글자) | `"RR-01"`, `'hello'` | 이름, 메시지, 명령 |
| `bool` | 불리언(참/거짓) | `True`, `False` | "GPS가 정상입니까?" |

VS Code 터미널에 `python3`를 입력하고 Enter를 누르세요. `>>>`가 나타나면 아래 `type(...)` 호출을 입력해서 각 값의 자료형을 확인하세요. 마치면 `exit()`을 입력해서 터미널 명령으로 돌아오세요.

```python
>>> type(7)
<class 'int'>
>>> type(0.5)
<class 'float'>
>>> type("7")
<class 'str'>
```

주의하세요. `7`과 `"7"`은 **다릅니다**. `7`은 숫자이고, `"7"`은 숫자처럼 생긴 문자열입니다.

---

## 3. 계산

| 연산자 | 의미 | 예 | 결과 |
|---|---|---|---|
| `+` | 더하기 | `7 + 2` | `9` |
| `-` | 빼기 | `7 - 2` | `5` |
| `*` | 곱하기 | `7 * 2` | `14` |
| `/` | 나누기(항상 실수가 나옵니다) | `7 / 2` | `3.5` |
| `//` | 나눗셈의 몫 | `7 // 2` | `3` |
| `%` | 나눗셈의 나머지 | `7 % 2` | `1` |
| `**` | 거듭제곱 | `2 ** 3` | `8` |

파이썬도 수학의 계산 순서를 따릅니다. `+`, `-`보다 `*`, `/`를 먼저 계산합니다. 괄호로 순서를 분명하게 나타내세요.

```python
average = (10 + 20) / 2
print(average)     # 15.0
```

### `//`와 `%` 함께 사용하기

단위를 나눌 때 아주 유용합니다. 135분은 몇 시간 몇 분입니까?

```python
total = 135
hours = total // 60      # 2  (온전한 시간의 수)
minutes = total % 60     # 15 (남은 분)
print(hours, minutes)    # 2 15
```

### `math` 모듈

**모듈**은 관련 도구를 모아 둔 묶음입니다. `math` 모듈은 파이썬에 기본으로 들어 있으므로 따로 설치하지 않습니다. 파일 맨 위에 `import math`를 쓰면 사용할 수 있습니다. `math.pi`처럼 점(`.`)을 찍으면 `math` 안의 도구를 고를 수 있습니다. `math.pi`는 원주율이고 `math.sqrt(16)`은 16의 제곱근입니다. `playground.py`의 내용을 아래 코드로 바꾸고 실행하세요. `import math`는 아래처럼 파일 맨 위에 씁니다.

```python
import math

print(math.pi)          # 3.141592653589793
print(math.sqrt(16))    # 4.0
```

ROS는 각도를 도 대신 **라디안**으로 나타내므로 `math.pi`를 자주 보게 됩니다.

### 직접 해 보기: 계산

VS Code 터미널에 `python3`를 입력하세요. 파이썬 `>>>` 프롬프트에서 다음 값을 계산한 뒤 `exit()`을 입력해서 VS Code 터미널로 돌아오세요.
1. 500초는 몇 분 몇 초입니까?
2. 로봇이 0.4 m/s로 90초 동안 움직이면 얼마나 이동합니까?
3. 2의 제곱근을 구하세요(먼저 `>>>`에 `import math`를 입력하세요).

---

## 4. 자료형 바꾸기

값을 다른 자료형으로 바꿔야 할 때가 있습니다. `python3`를 실행하세요.
**파이썬 `>>>` 프롬프트**에 아래 호출을 하나씩 입력하세요. 주석은 결과를 보여 줍니다.

마치면 `>>>`에 `exit()`을 입력하세요.

```python
int("42")       # 42     문자열 → 정수
float("3.5")    # 3.5    문자열 → 실수
str(42)         # '42'   숫자 → 문자열(따옴표는 문자열이라는 표시입니다)
int(3.9)        # 3      소수 부분을 버립니다(반올림하지 않습니다!)
round(3.9)      # 4      반올림합니다
round(3.14159, 2)  # 3.14
```

`round()`는 정확히 중간인 값(예: `2.5`)을 가까운 **짝수** 쪽으로 반올림합니다. `round(2.5)`는 `2`이고 `round(3.5)`는 `4`입니다.

문자열이 숫자가 아니면 오류가 납니다.

```python
>>> int("hello")
ValueError: invalid literal for int() with base 10: 'hello'
```

---

## 5. 사용자에게 입력받기: `input()`

`input()`은 메시지를 보여 주고, 사용자가 내용을 입력한 뒤 Enter를 누를 때까지 기다립니다. 그런 다음 입력한 내용을 돌려줍니다.

```python
name = input("Robot name: ")
print("Starting", name)
```

```
Robot name: RR-01
Starting RR-01
```

⚠️ 사용자가 숫자를 입력해도 **`input()`은 항상 `str`을 돌려줍니다**. `playground.py`의 내용을 아래 코드로 바꾸고 실행하세요. `Distance (m):`에 `10`을 입력하고 Enter를 누르세요.

```python
distance = input("Distance (m): ")    # 사용자가 10을 입력합니다
print(distance * 2)                   # 1010  ← 문자열을 두 번 반복합니다!
```

`playground.py`의 거리 예제를 아래 코드로 바꾸세요. 입력값을 `float`로 바꿉니다. **Ctrl + S**로 저장하고 VS Code 터미널에서 `python3 playground.py`를 실행하세요. `Distance (m):`에 `10`을 입력하고 Enter를 누르세요.

```python
distance = float(input("Distance (m): "))
print(distance * 2)                   # 20.0 ✅
```

---

## 6. f-문자열: 문자열에 값 넣기

**f-문자열**은 따옴표 앞에 `f`를 붙입니다. 안에서는 `{ }`에 변수를 넣습니다.

```python
robot = "RR-01"
battery = 87
print(f"Robot {robot} has {battery}% battery")
```

```
Robot RR-01 has 87% battery
```

### 숫자 표시 형식

값 뒤에 `:.2f`를 붙이면 소수점 아래 두 자리까지 표시합니다.

```python
voltage = 12.34567
print(f"Voltage: {voltage:.2f} V")     # Voltage: 12.35 V
print(f"Voltage: {voltage:.1f} V")     # Voltage: 12.3 V
print(f"Distance: {5:.2f} m")          # Distance: 5.00 m
```

ROS 로그 메시지를 비롯해 거의 모든 프로그램에서 f-문자열을 사용하게 됩니다.

### 직접 해 보기: 속도 변환

`playground.py`에 속도(m/s)를 입력받는 프로그램을 작성하세요. 속도를 km/h로 바꾸고 소수점 아래 한 자리까지 출력하세요. **Ctrl + S**로 저장하고 VS Code 터미널에서 `python3 playground.py`를 실행하세요.

`Speed (m/s):`에 `2.5`를 입력하고 Enter를 누르세요. 아래 결과가 나와야 합니다. (1 m/s = 3.6 km/h입니다.)

```
Speed (m/s): 2.5
2.5 m/s = 9.0 km/h
```

---

## 7. 자주 하는 실수

| 실수 | 해결 방법 |
|---|---|
| `"5" + 3`에서 `TypeError: can only concatenate str (not "int") to str`가 나옵니다 | 먼저 자료형을 바꾸세요: `int("5") + 3` |
| `input()` 값으로 계산하면 이상한 결과가 나옵니다 | `int(input(...))` 또는 `float(input(...))`로 감싸세요 |
| `print("Battery: {battery}")`가 `{battery}`를 그대로 출력합니다 | `f`가 빠졌습니다: `print(f"Battery: {battery}")` |
| `Speed = 1`로 저장했는데 `print(speed)`에서 `NameError`가 나옵니다 | 이름은 대소문자를 구분합니다. `Speed`와 `speed`는 서로 다른 변수입니다 |

---

## 8. 연습 문제

**연습 문제 진행 방법:** 한 번에 하나씩 **순서대로** 푸세요. 아래의 각 연습 문제에는 번호가 붙은 진행 순서가 있습니다. 1번부터 끝까지 따라 한 뒤 다음 연습 문제로 넘어가세요. 잘되지 않는 단계가 있으면 [연습 문제 진행 방법 5부](../../docs/02-how-exercises-work.md#5부-테스트-결과-읽기)를 참고하세요.

### 연습 문제 1/2: 배터리 사용 시간

> 📖 **시작하기 전에:** [연습 문제 진행 방법](../../docs/02-how-exercises-work.md)을 이 수업 옆에 여세요.
> [3부: 스크립트 연습 문제](../../docs/02-how-exercises-work.md#3부-스크립트-연습-문제-따라-하기-12일차)와 [5부: 테스트 결과 읽기](../../docs/02-how-exercises-work.md#5부-테스트-결과-읽기)를 따라 하세요.

**할 일:** 배터리 용량(mAh)과 로봇이 사용하는 전류(mA)를 입력받으세요. 용량 ÷ 전류로 배터리를 몇 시간 사용할 수 있는지 계산하고 소수점 아래 두 자리까지 출력하세요.

**실행 결과 예시**(`5000`과 `2000`을 입력합니다):

```
$ python3 exercises/week1/w1d2_battery_runtime.py
Capacity (mAh): 5000
Current (mA): 2000
Runtime: 2.50 hours
```

**따라 해 볼 예제:** 비슷한 문제입니다(이 연습 문제의 정답은 아닙니다).

이 프로그램은 거리와 속도를 입력받고 이동에 걸리는 시간을 출력합니다. 연습 문제와 같은 세 부분으로 구성됩니다. `int()`로 감싼 `input()` 두 번, 나눗셈 한 번, `:.2f`를 사용하는 f-문자열 한 개입니다.

```python
distance = int(input("Distance (m): "))
speed = int(input("Speed (m/min): "))
travel_time = distance / speed
print(f"Travel time: {travel_time:.2f} minutes")
```

예제를 실행해 보세요. VS Code 터미널에 `code playground.py`를 입력해서 같은 VS Code 창에 `playground.py`를 여세요.
VS Code 편집기에서 `playground.py`에 예제를 입력하세요. **Ctrl + S**로 `playground.py`를 저장하세요.
VS Code 터미널에서 `python3 playground.py`를 실행하세요.

입력을 요청하면 `100`을 입력하고 Enter를 누른 뒤 `40`을 입력하고 Enter를 누르세요.

```
$ python3 playground.py
Distance (m): 100
Speed (m/min): 40
Travel time: 2.50 minutes
```

예제가 어떻게 동작하는지 이해했다면 아래 순서대로 진행하세요. 연습 문제 코드는 직접 작성하세요. 할 일이 다르니 예제를 그대로 복사하지 마세요.

**진행 순서:**

1. **파일을 여세요.** VS Code 편집기에서 **Ctrl + P**를 누르세요.
   VS Code 위쪽에 나타난 입력 칸에 [`exercises/week1/w1d2_battery_runtime.py`](../../exercises/week1/w1d2_battery_runtime.py)를 입력하고 Enter를 누르세요. 편집기에 파일이 열립니다. 또는 VS Code 편집기 왼쪽 파일 목록(**Explorer**)에서 [`exercises`](../../exercises/) → [`week1`](../../exercises/week1/) → [`w1d2_battery_runtime.py`](../../exercises/week1/w1d2_battery_runtime.py)를 클릭하세요.
2. VS Code 편집기에서 `w1d2_battery_runtime.py` 맨 위의 안내를 읽으세요.
3. VS Code 편집기에서 `w1d2_battery_runtime.py`의 `TODO` 아래에 코드를 작성하세요. 다음 내용이 필요합니다.
   - 각각 `int()`로 감싼 `input()` 두 번(이 수업의 5절)
   - 나눗셈 한 번
   - f-문자열과 `:.2f`를 사용하는 `print()` 한 번(6절)
4. VS Code 편집기에서 **Ctrl + S**로 `w1d2_battery_runtime.py`를 저장하세요. 저장하면 파일 탭의 **●**가 사라집니다.
5. VS Code 터미널에서 `w1d2_battery_runtime.py`를 실행하세요. `Capacity (mAh):`에 `5000`을 입력하고 Enter를 누르세요. 그런 다음 `Current (mA):`에 `2000`을 입력하고 Enter를 누르세요.
   ```bash
   python3 exercises/week1/w1d2_battery_runtime.py
   ```
   ✔ 마지막 줄은 `Runtime: 2.50 hours`여야 합니다. `python3 exercises/week1/w1d2_battery_runtime.py`를 다시 실행하세요. `Capacity (mAh):`에 `1000`을 입력하세요.
   `Current (mA):`에 `3000`을 입력하세요. 각 값을 입력한 뒤 Enter를 누르세요. `Runtime: 0.33 hours`가 나와야 합니다.
   ✘ **아무것도 나타나지 않으면** 파일에 아직 코드가 없거나 저장하지 않은 것입니다. 3단계로 돌아가세요.
   ✘ 전류에 `0`을 입력하면 `ZeroDivisionError`(0으로 나눌 수 없음)가, `2.5`처럼 소수를 입력하면 `ValueError`가 나옵니다. 이 연습 문제에서는 0보다 큰 정수만 입력합니다. 코드는 그대로 두고 위의 값으로 다시 실행하세요.
6. VS Code 터미널에서 [`test_w1d2.py`](../../exercises/week1/tests/test_w1d2.py)로 `w1d2_battery_runtime.py`를 테스트하세요.
   ```bash
   pytest exercises/week1/tests/test_w1d2.py -k battery
   ```
   ✔ `3 passed, 3 deselected`가 나와야 합니다. 테스트는 서로 다른 숫자로 프로그램을 세 번 실행합니다.
7. VS Code 터미널에서 `python3 next.py`를 실행하세요. 테스트가 통과했으면 다음 단계가 나타납니다.

> `deselected`는 이 파일에 있는 **다른** 연습 문제의 테스트는 실행하지 않았다는 뜻입니다. `-k`를 사용하면 이렇게 되니 괜찮습니다.

### 연습 문제 2/2: 임무 타이머

> 📖 **시작하기 전에:** [연습 문제 진행 방법](../../docs/02-how-exercises-work.md)을 이 수업 옆에 여세요.
> [3부: 스크립트 연습 문제](../../docs/02-how-exercises-work.md#3부-스크립트-연습-문제-따라-하기-12일차)와 [5부: 테스트 결과 읽기](../../docs/02-how-exercises-work.md#5부-테스트-결과-읽기)를 따라 하세요.

**할 일:** 초 단위 시간을 입력받으세요. 시간, 분, 초로 나누어 출력하세요.

**실행 결과 예시**(`3725`를 입력합니다):

```
$ python3 exercises/week1/w1d2_time_format.py
Seconds: 3725
1 h 2 m 5 s
```

**따라 해 볼 예제:** 비슷한 문제입니다(이 연습 문제의 정답은 아닙니다).

이 프로그램은 `//`와 `%`로 센티미터 단위 길이를 미터와 센티미터로 나눕니다. 연습 문제에서는 시간, 분, 초 **세 가지** 단위를 사용하므로 한 단계가 더 필요합니다.

```python
total_cm = int(input("Length (cm): "))
meters = total_cm // 100
cm = total_cm % 100
print(f"{meters} m {cm} cm")
```

예제를 실행해 보세요. VS Code 터미널에 `code playground.py`를 입력해서 같은 VS Code 창에 `playground.py`를 여세요.
VS Code 편집기에서 `playground.py`에 예제를 입력하세요. **Ctrl + S**로 `playground.py`를 저장하세요.
VS Code 터미널에서 `python3 playground.py`를 실행하세요.

입력을 요청하면 `275`를 입력하고 Enter를 누르세요.

```
$ python3 playground.py
Length (cm): 275
2 m 75 cm
```

예제가 어떻게 동작하는지 이해했다면 아래 순서대로 진행하세요. 연습 문제 코드는 직접 작성하세요. 할 일이 다르니 예제를 그대로 복사하지 마세요.

**진행 순서:**

1. **파일을 여세요.** VS Code 편집기에서 **Ctrl + P**를 누르세요.
   VS Code 위쪽에 나타난 입력 칸에 [`exercises/week1/w1d2_time_format.py`](../../exercises/week1/w1d2_time_format.py)를 입력하고 Enter를 누르세요. 편집기에 파일이 열립니다. 또는 VS Code 편집기 왼쪽 파일 목록(**Explorer**)에서 [`exercises`](../../exercises/) → [`week1`](../../exercises/week1/) → [`w1d2_time_format.py`](../../exercises/week1/w1d2_time_format.py)를 클릭하세요.
2. VS Code 편집기에서 `w1d2_time_format.py` 맨 위의 안내를 읽으세요.
3. VS Code 편집기에서 `w1d2_time_format.py`의 `TODO` 아래에 코드를 작성하세요. `//`와 `%`를 사용하세요(이 수업 3절의 "`//`와 `%` 함께 사용하기"). 1시간은 3600초이고 1분은 60초입니다.
   도움말: 먼저 종이에 3725로 계산해 보세요. 3725초에서 1시간(3600초)을 빼면 125초가 남습니다. 분은 처음의 3725초가 아니라 **남은 125초**에서 구하세요. 125초는 2분 5초입니다.
4. VS Code 편집기에서 **Ctrl + S**로 `w1d2_time_format.py`를 저장하세요. 저장하면 파일 탭의 **●**가 사라집니다.
5. VS Code 터미널에서 `w1d2_time_format.py`를 실행하세요. `Seconds:`에 `3725`를 입력하고 Enter를 누르세요.
   ```bash
   python3 exercises/week1/w1d2_time_format.py
   ```
   ✔ `1 h 2 m 5 s`가 나와야 합니다. `python3 exercises/week1/w1d2_time_format.py`를 다시 실행하고 `Seconds:`에 `59`를 입력하세요(→ `0 h 0 m 59 s`). 같은 명령을 다시 실행하고 `Seconds:`에 `7200`을 입력하세요(→ `2 h 0 m 0 s`). 각 값을 입력한 뒤 Enter를 누르세요.
   ✘ **아무것도 나타나지 않으면** 파일에 아직 코드가 없거나 저장하지 않은 것입니다. 3단계로 돌아가세요.
6. VS Code 터미널에서 [`test_w1d2.py`](../../exercises/week1/tests/test_w1d2.py)로 `w1d2_time_format.py`를 테스트하세요.
   ```bash
   pytest exercises/week1/tests/test_w1d2.py -k time_format
   ```
   ✔ `3 passed, 3 deselected`가 나와야 합니다.
7. 아직 `python3 next.py`를 실행하지 마세요. 아래 **마지막으로: 오늘의 테스트 전체**로 가세요. `python3 next.py`는 그 절의 테스트를 실행한 다음에 실행합니다.

### 마지막으로: 오늘의 테스트 전체

VS Code 터미널에서 [`test_w1d2.py`](../../exercises/week1/tests/test_w1d2.py)의 오늘 테스트를 실행하세요.

```bash
pytest exercises/week1/tests/test_w1d2.py
```

✔ **`6 passed`**가 나와야 합니다. VS Code 터미널에서 `python3 next.py`를 실행하세요.

---

## 9. 오늘 마치기 전에

VS Code 터미널에서 `python3 next.py`를 실행하세요. 오늘 남은 단계를 하나씩 안내합니다.

- 수업 내용을 설명할 수 있는지 묻는 질문에 답하세요.
- 실습 일지를 **직접** 쓰세요. `python3 next.py`는 일지를 대신 써 주지 않고, 썼는지만 확인합니다. 제목의 날짜, 오늘 수업, 배운 내용, 연습 문제 표, 겪은 문제, 질문, 공부한 시간을 **모두** 채우세요.
- 멘토와 점검하세요. 멘토가 확인하면 점검 질문에 `y`로 답하세요.
- **마지막으로** 커밋하고 푸시하세요. 오늘의 코드, 실습 일지, 진도가 모두 GitHub로 갑니다. 푸시했는지는 다음에 `python3 next.py`를 실행할 때 자동으로 확인합니다.

푸시까지 마치면 오늘 공부는 끝입니다. `python3 next.py`에 **3일차**가 나타나도 오늘은 시작하지 마세요. 다음 학습일에 `python3 next.py`를 실행하고 3일차 수업을 시작하세요.

**다음:** [3일차: 조건에 따라 판단하기, 함수와 if 문](day3-functions-and-decisions.md)

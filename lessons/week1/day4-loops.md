# 1주차 · 4일차: 반복하기, `for` 문과 `while` 문

**배울 내용:** 정해진 횟수만큼 반복하는 `for` 문, 조건이 바뀔 때까지 반복하는 `while` 문, 반복문을 멈추거나 일부를 건너뛰는 방법을 배웁니다.

**로봇을 다룰 때 필요한 이유:** 로봇 프로그램은 큰 반복문 하나와 같습니다. *센서 읽기 → 판단하기 → 움직이기 → 반복하기*를 1초에도 여러 번 합니다. ROS에서는 이 반복문이 `rclpy.spin()` 안에 숨어 있지만, 여전히 반복문입니다.

---

## 1. `for` 문과 `range()`

```python
for i in range(5):
    print("Reading sensor", i)
```

```
Reading sensor 0
Reading sensor 1
Reading sensor 2
Reading sensor 3
Reading sensor 4
```

- `range(5)`는 `0, 1, 2, 3, 4`를 차례로 내놓습니다. **0에서 시작하고 5 직전에 끝납니다.**
- 반복할 때마다 `i`에 다음 숫자가 들어갑니다.
- 각 숫자마다 들여쓴 줄들이 한 번씩 실행됩니다.

### `range`의 여러 사용 방법

| 코드 | 나오는 숫자 |
|---|---|
| `range(5)` | 0, 1, 2, 3, 4 |
| `range(1, 6)` | 1, 2, 3, 4, 5 |
| `range(0, 10, 2)` | 0, 2, 4, 6, 8 (2씩 증가) |
| `range(5, 0, -1)` | 5, 4, 3, 2, 1 (거꾸로 세기) |

끝 값은 **절대** 포함되지 않습니다. `n`까지 포함하려면 `range(1, n + 1)`을 쓰세요.

### 직접 해 보기

`playground.py`에 10부터 0까지 2씩 줄여 가며 출력하는 반복문을 작성하세요.
**Ctrl + S**로 저장하고 VS Code 터미널에서 `python3 playground.py`를 실행하세요. 예상 숫자는 `10 8 6 4 2 0`입니다(한 줄에 하나씩 출력해도 됩니다).

---

## 2. 값을 누적하는 방법

여러 값을 차례로 살펴보며 결과 **하나**를 만드는 일은 아주 흔합니다. 반복문 **앞에서** 빈 결과로 시작하고, 반복문 **안에서** 결과를 갱신합니다.

```python
total = 0                    # 1. 반복문 앞에서 시작값을 정합니다
for i in range(1, 4):
    total = total + i        # 2. 반복문 안에서 갱신합니다
print(total)                 # 3. 반복문 뒤에서 사용합니다 → 6
```

단계별로 살펴보세요.

| 반복 회차 | `i` | 계산 후 `total` |
|---|---|---|
| 시작 | | 0 |
| 1 | 1 | 1 |
| 2 | 2 | 3 |
| 3 | 3 | 6 |

같은 방법으로 **개수를 셀 수도** 있습니다.

```python
count = 0
for i in range(1, 11):
    if i % 2 == 0:           # 짝수만 셉니다
        count = count + 1
print(count)                 # 5
```

**문자열을 만들 때도** 사용할 수 있습니다.

```python
text = ""
for i in range(3):
    text = text + "beep "
print(text)                  # "beep beep beep "
```

숫자를 문자열에 붙일 때는 `str(i)`를 사용하세요: `text = text + str(i)`.

> **짧게 쓰기:** `total += i`는 `total = total + i`와 같은 뜻입니다. 둘 다 써도 됩니다.

---

## 3. `while`: 조건이 True인 동안 반복하기

반복 횟수를 미리 **알 수 없을 때** `while`을 사용합니다.

```python
battery = 100
while battery > 20:
    print(f"Working... battery {battery}%")
    battery = battery - 30
print("Going to charger")
```

```
Working... battery 100%
Working... battery 70%
Working... battery 40%
Going to charger
```

파이썬은 매번 반복하기 전에 조건을 확인합니다. 조건이 `False`이면 반복문이 끝납니다.

⚠️ **반복문 안에서 조건에 영향을 주는 값이 바뀌어야 합니다.** 그렇지 않으면 영원히 반복합니다.

```python
battery = 100
while battery > 20:
    print("Working...")      # battery가 바뀌지 않으므로 끝나지 않습니다!
```

`while battery > 20` 반복문이 `Working...`을 계속 출력하면 VS Code 터미널에서 **Ctrl + C**를 눌러 프로그램을 멈추세요.

---

## 4. `break`와 `continue`

- `break`는 반복문을 **즉시** 빠져나옵니다.
- `continue`는 이번 반복의 나머지 부분을 건너뛰고 **다음** 반복을 시작합니다.

계속 반복하다가 할 일을 마치면 `break`로 나오는 방식을 자주 사용합니다. 메뉴 프로그램도 이렇게 동작합니다(주간 과제에서 필요합니다!).

```python
while True:
    command = input("Command (q to quit): ")
    if command == "q":
        break
    print("Running", command)
print("Bye")
```

`continue`로 잘못된 센서 값을 건너뛰는 예제입니다.

```python
for reading in range(-2, 4):
    if reading < 0:
        continue             # 음수는 센서 오류이므로 건너뜁니다
    print("Valid reading:", reading)
```

---

## 5. 함수 안의 반복문

```python
def count_even(limit):
    count = 0
    for i in range(1, limit + 1):
        if i % 2 == 0:
            count = count + 1
    return count             # 반복문 안이 아니라 반복문이 끝난 뒤에 반환합니다!


print(count_even(10))        # 5
```

⚠️ `return`의 들여쓰기를 확인하세요. 반복문 안으로 들여쓰면 첫 번째 반복 직후 함수가 끝납니다.

---

## 6. `for`와 `while` 중 무엇을 써야 합니까?

| 사용할 문법 | 사용 시점 | 예 |
|---|---|---|
| `for` | 반복 횟수를 알 때 | "센서 10개 확인하기", "1부터 n까지 세기" |
| `while` | 어떤 일이 일어날 때까지 반복할 때 | "배터리가 부족해질 때까지", "사용자가 q를 입력할 때까지" |

---

## 7. 자주 하는 실수

| 실수 | 해결 방법 |
|---|---|
| 한 번 덜 반복합니다 | `range`는 끝 값 **직전에** 멈춥니다. `range(1, n + 1)`을 사용하세요 |
| 프로그램이 끝나지 않습니다 | `while` 조건이 False가 되지 않습니다. VS Code 터미널에서 **Ctrl + C**를 누르세요. 그런 다음 VS Code 편집기에서 지금 실행한 파일(`playground.py` 또는 `w1d4_loops.py`)을 열고, 조건에 쓰는 변수가 반복문 안에서 바뀌도록 고치세요. 테스트 중에 Ctrl + C를 누르면 마지막에 멈춘 줄의 파일 이름과 줄 번호가 나옵니다 |
| 결과가 항상 0이거나 틀립니다 | 시작값(`total = 0`)이 반복문 안에 있어서 매번 초기화됩니다. VS Code 편집기에서 작성 중인 함수의 `total = 0`을 반복문 **앞으로** 옮기세요 |
| 첫 반복 후 함수가 반환합니다 | `return`이 반복문 안으로 들여써져 있습니다. VS Code 편집기에서 작성 중인 함수의 `return`을 반복문 밖으로 옮기세요 |

---

## 8. 연습 문제

**연습 문제 진행 방법:** 한 번에 하나씩 **순서대로** 푸세요. 아래의 각 연습 문제에는 번호가 붙은 진행 순서가 있습니다. 1번부터 끝까지 따라 한 뒤 다음 연습 문제로 넘어가세요. 잘되지 않는 단계가 있으면 [연습 문제 진행 방법 5부](../../docs/02-how-exercises-work.md#5부-테스트-결과-읽기)를 참고하세요.

세 함수는 모두 [`exercises/week1/w1d4_loops.py`](../../exercises/week1/w1d4_loops.py)에 있습니다. 아래에서 각 함수의 번호가 붙은 진행 순서를 따르세요.

### 연습 문제 1/3: `countdown(n)`

> 📖 **시작하기 전에:** [연습 문제 진행 방법](../../docs/02-how-exercises-work.md)을 이 수업 옆에 여세요.
> [4부: 함수 연습 문제](../../docs/02-how-exercises-work.md#4부-함수-연습-문제-따라-하기-35일차)와 [5부: 테스트 결과 읽기](../../docs/02-how-exercises-work.md#5부-테스트-결과-읽기)를 따라 하세요.

**할 일:** `n`부터 1까지 거꾸로 세고 끝에 `GO!`가 붙는 문자열을 반환하세요. 각 부분은 공백으로 구분하세요.

```python
>>> countdown(3)
'3 2 1 GO!'
>>> countdown(0)
'GO!'
```

**따라 해 볼 예제:** 비슷한 문제입니다(이 연습 문제의 정답은 아닙니다).

이 함수는 거꾸로 세는 대신 숫자를 **올려서** 세고 `DONE`으로 끝납니다. 연습 문제에서는 어떤 `range(...)`를 써야 **거꾸로** 셀 수 있을지 생각하세요(1절).

```python
def count_up(n):
    text = ""
    for i in range(1, n + 1):
        text = text + str(i) + " "
    return text + "DONE"
```

예제를 실행해 보세요. VS Code 터미널에 `code playground.py`를 입력해서 같은 VS Code 창에 `playground.py`를 여세요.
VS Code 편집기에서 `playground.py`에 예제를 입력하세요. **Ctrl + S**로 `playground.py`를 저장하세요.
VS Code 터미널에서 `python3 -i playground.py`를 실행하세요.

**파이썬 `>>>` 프롬프트**에 아래 호출을 입력하세요. `>>>`가 없는 줄은 나와야 할 결과입니다.

```python
$ python3 -i playground.py
>>> count_up(3)
'1 2 3 DONE'
>>> count_up(0)
'DONE'
>>> exit()
```

예제가 어떻게 동작하는지 이해했다면 아래 순서대로 진행하세요. 연습 문제 코드는 직접 작성하세요. 할 일이 다르니 예제를 그대로 복사하지 마세요.

**진행 순서:**

1. **파일을 여세요.** VS Code 편집기에서 **Ctrl + P**를 누르세요.
   VS Code 위쪽에 나타난 입력 칸에 [`exercises/week1/w1d4_loops.py`](../../exercises/week1/w1d4_loops.py)를 입력하고 Enter를 누르세요. 편집기에 파일이 열립니다. 또는 VS Code 편집기 왼쪽 파일 목록(**Explorer**)에서 [`exercises`](../../exercises/) → [`week1`](../../exercises/week1/) → [`w1d4_loops.py`](../../exercises/week1/w1d4_loops.py)를 클릭하세요.
2. VS Code 편집기에서 `w1d4_loops.py`의 `countdown` 안에 있는 `pass`를 코드로 바꾸세요. 2절의 "문자열 만들기" 방법을 사용하세요. `text = ""`로 시작하세요.
   거꾸로 세는 `range`를 사용하는 `for` 문 안에서 숫자를 붙이세요(1절).
   끝에 `"GO!"`를 붙이세요. 숫자를 문자열로 바꿀 때는 `str(i)`를 사용하세요.
3. VS Code 편집기에서 **Ctrl + S**로 `w1d4_loops.py`를 저장하세요. 파일 탭의 **●**가 사라집니다.

   VS Code 터미널에서 `python3 -i exercises/week1/w1d4_loops.py`를 실행하세요.
   **파이썬 `>>>` 프롬프트**에 위의 **할 일** 아래에 나온 `countdown(...)` 호출을 입력하고 결과를 비교하세요.

   `>>>`에 `exit()`을 입력해서 VS Code 터미널로 돌아오세요.
4. VS Code 터미널에서 [`test_w1d4.py`](../../exercises/week1/tests/test_w1d4.py)로 `countdown`을 테스트하세요.
   ```bash
   pytest exercises/week1/tests/test_w1d4.py -k countdown
   ```
   ✔ `4 passed, 8 deselected`가 나와야 합니다.
5. VS Code 터미널에서 `python3 next.py`를 실행하세요. 테스트가 통과했으면 다음 단계가 나타납니다.

> `deselected`는 이 파일에 있는 **다른** 연습 문제의 테스트는 실행하지 않았다는 뜻입니다. `-k`를 사용하면 이렇게 되니 괜찮습니다.

### 연습 문제 2/3: `sum_to(n)`

> 📖 **시작하기 전에:** [연습 문제 진행 방법](../../docs/02-how-exercises-work.md)을 이 수업 옆에 여세요.
> [4부: 함수 연습 문제](../../docs/02-how-exercises-work.md#4부-함수-연습-문제-따라-하기-35일차)와 [5부: 테스트 결과 읽기](../../docs/02-how-exercises-work.md#5부-테스트-결과-읽기)를 따라 하세요.

**할 일:** 반복문으로 1 + 2 + … + n을 계산해서 반환하세요.

```python
>>> sum_to(4)
10
>>> sum_to(0)
0
```

**따라 해 볼 예제:** 비슷한 문제입니다(이 연습 문제의 정답은 아닙니다).

이 함수는 1 × 2 × … × n을 **곱합니다**. `0`이 아니라 `1`로 시작한다는 점을 살펴보세요. 무엇이든 0을 곱하면 0입니다! 합을 구할 때는 어떤 시작값이 알맞을지 생각하세요.

```python
def product_to(n):
    result = 1
    for i in range(1, n + 1):
        result = result * i
    return result
```

예제를 실행해 보세요. VS Code 터미널에 `code playground.py`를 입력해서 같은 VS Code 창에 `playground.py`를 여세요.
VS Code 편집기에서 `playground.py`에 예제를 입력하세요. **Ctrl + S**로 `playground.py`를 저장하세요.
VS Code 터미널에서 `python3 -i playground.py`를 실행하세요.

**파이썬 `>>>` 프롬프트**에 아래 호출을 입력하세요. `>>>`가 없는 줄은 나와야 할 결과입니다.

```python
$ python3 -i playground.py
>>> product_to(4)
24
>>> product_to(0)
1
>>> exit()
```

예제가 어떻게 동작하는지 이해했다면 아래 순서대로 진행하세요. 연습 문제 코드는 직접 작성하세요. 할 일이 다르니 예제를 그대로 복사하지 마세요.

**진행 순서:**

1. **파일을 여세요.** VS Code 편집기에서 **Ctrl + P**를 누르세요.
   VS Code 위쪽에 나타난 입력 칸에 [`exercises/week1/w1d4_loops.py`](../../exercises/week1/w1d4_loops.py)를 입력하고 Enter를 누르세요. 편집기에 파일이 열립니다. 또는 VS Code 편집기 왼쪽 파일 목록(**Explorer**)에서 [`exercises`](../../exercises/) → [`week1`](../../exercises/week1/) → [`w1d4_loops.py`](../../exercises/week1/w1d4_loops.py)를 클릭하세요.
2. VS Code 편집기에서 `w1d4_loops.py`의 `sum_to` 안에 있는 `pass`를 코드로 바꾸세요. 2절에서 배운 누적 방법 그대로입니다. `n`을 포함하려면 `range(1, n + 1)`을 사용한다는 점을 기억하세요.
3. VS Code 편집기에서 **Ctrl + S**로 `w1d4_loops.py`를 저장하세요. 파일 탭의 **●**가 사라집니다.

   VS Code 터미널에서 `python3 -i exercises/week1/w1d4_loops.py`를 실행하세요.
   **파이썬 `>>>` 프롬프트**에 위의 **할 일** 아래에 나온 `sum_to(...)` 호출을 입력하고 결과를 비교하세요.

   `>>>`에 `exit()`을 입력해서 VS Code 터미널로 돌아오세요.
4. VS Code 터미널에서 [`test_w1d4.py`](../../exercises/week1/tests/test_w1d4.py)로 `sum_to`를 테스트하세요.
   ```bash
   pytest exercises/week1/tests/test_w1d4.py -k sum_to
   ```
   ✔ `4 passed, 8 deselected`가 나와야 합니다.
5. VS Code 터미널에서 `python3 next.py`를 실행하세요. 테스트가 통과했으면 다음 단계가 나타납니다.

### 연습 문제 3/3: `steps_until_low(battery, drain_per_step, low_level)`

> 📖 **시작하기 전에:** [연습 문제 진행 방법](../../docs/02-how-exercises-work.md)을 이 수업 옆에 여세요.
> [4부: 함수 연습 문제](../../docs/02-how-exercises-work.md#4부-함수-연습-문제-따라-하기-35일차)와 [5부: 테스트 결과 읽기](../../docs/02-how-exercises-work.md#5부-테스트-결과-읽기)를 따라 하세요.

**할 일:** 로봇은 한 단계마다 배터리를 `drain_per_step`만큼 사용합니다. 배터리가 `low_level` 이하가 될 때까지 몇 단계가 걸리는지 반환하세요.

```python
>>> steps_until_low(100, 10, 50)
5
>>> steps_until_low(10, 5, 20)
0
```

**따라 해 볼 예제:** 비슷한 문제입니다(이 연습 문제의 정답은 아닙니다).

이 함수는 연습 문제와 반대로 배터리가 가득 찰 때까지 **충전**하고, `while` 문으로 단계 수를 셉니다.

```python
def steps_until_full(battery, charge_per_step, full_level):
    steps = 0
    while battery < full_level:
        battery = battery + charge_per_step
        steps = steps + 1
    return steps
```

예제를 실행해 보세요. VS Code 터미널에 `code playground.py`를 입력해서 같은 VS Code 창에 `playground.py`를 여세요.
VS Code 편집기에서 `playground.py`에 예제를 입력하세요. **Ctrl + S**로 `playground.py`를 저장하세요.
VS Code 터미널에서 `python3 -i playground.py`를 실행하세요.

**파이썬 `>>>` 프롬프트**에 아래 호출을 입력하세요. `>>>`가 없는 줄은 나와야 할 결과입니다.

```python
$ python3 -i playground.py
>>> steps_until_full(50, 10, 100)
5
>>> steps_until_full(100, 10, 100)
0
>>> exit()
```

예제가 어떻게 동작하는지 이해했다면 아래 순서대로 진행하세요. 연습 문제 코드는 직접 작성하세요. 할 일이 다르니 예제를 그대로 복사하지 마세요.

**진행 순서:**

1. **파일을 여세요.** VS Code 편집기에서 **Ctrl + P**를 누르세요.
   VS Code 위쪽에 나타난 입력 칸에 [`exercises/week1/w1d4_loops.py`](../../exercises/week1/w1d4_loops.py)를 입력하고 Enter를 누르세요. 편집기에 파일이 열립니다. 또는 VS Code 편집기 왼쪽 파일 목록(**Explorer**)에서 [`exercises`](../../exercises/) → [`week1`](../../exercises/week1/) → [`w1d4_loops.py`](../../exercises/week1/w1d4_loops.py)를 클릭하세요.
2. VS Code 편집기에서 `w1d4_loops.py`의 `steps_until_low`를 읽으세요. **먼저 종이에** 2절처럼 `steps_until_low(100, 10, 50)`의 표를 그리세요. 열 이름은 *단계*와 *배터리*로 하세요. 첫 행은 '0단계, 배터리 100'입니다. 한 번 반복할 때마다 '1단계, 90', '2단계, 80'처럼 한 행씩 적고, '5단계, 50'에서 멈춥니다. 처음부터 배터리가 `low_level` 이하이면 한 번도 반복하지 않으므로 답은 0입니다.
3. VS Code 편집기에서 `w1d4_loops.py`의 `steps_until_low` 안에 있는 `pass`를 코드로 바꾸세요. `while` 문을 사용하세요(3절). 배터리가 `low_level`보다 큰 **동안** 계속 반복합니다. 반복문 안에서 배터리 소모량을 빼고 단계 수를 세는 변수에 1을 더하세요.
4. VS Code 편집기에서 **Ctrl + S**로 `w1d4_loops.py`를 저장하세요. 파일 탭의 **●**가 사라집니다.

   VS Code 터미널에서 `python3 -i exercises/week1/w1d4_loops.py`를 실행하세요.
   **파이썬 `>>>` 프롬프트**에 위의 **할 일** 아래에 나온 `steps_until_low(...)` 호출을 입력하고 결과를 비교하세요.

   `>>>`에 `exit()`을 입력해서 VS Code 터미널로 돌아오세요. `steps_until_low(...)` 호출이 끝나지 않으면 VS Code 터미널에서 **Ctrl + C**를 누르세요. 배터리가 줄어들지 않고 있는 것입니다.
5. VS Code 터미널에서 [`test_w1d4.py`](../../exercises/week1/tests/test_w1d4.py)로 `steps_until_low`를 테스트하세요.
   ```bash
   pytest exercises/week1/tests/test_w1d4.py -k steps_until_low
   ```
   ✔ `4 passed, 8 deselected`가 나와야 합니다.

   테스트가 끝나지 않고 아무것도 나오지 않으면 **Ctrl + C**를 누르세요. 마지막에 `w1d4_loops.py:48: KeyboardInterrupt`처럼 멈춘 줄의 번호가 나옵니다. 그 `while` 반복문 안에서 배터리 값이 줄어드는지 확인하세요.
6. 아직 `python3 next.py`를 실행하지 마세요. 아래 **마지막으로: 오늘의 테스트 전체**로 가세요. 추가 도전은 선택입니다. `python3 next.py`는 그 절의 테스트를 실행한 다음에 실행합니다.

### 추가 도전(선택): `count_multiples(limit, k)`

시간이 남을 때만 하세요. 테스트하지 않으며 `python3 next.py`의 단계에도 없습니다.

`playground.py`의 내용을 지우고, 1부터 `limit`까지(`limit` 포함) 중에서 `k`로 나누어떨어지는 숫자의 개수를 반환하는 `count_multiples(limit, k)` 함수를 작성하세요. `x % k == 0`이면 `x`가 `k`로 나누어떨어집니다. 2절의 개수 세기 예제와 같은 방법입니다.

VS Code 터미널에서 `python3 -i playground.py`를 실행하고 `>>>`에 `count_multiples(10, 3)`을 입력하세요. `3`이 나와야 합니다(3, 6, 9). 마치면 `exit()`을 입력하세요.

### 마지막으로: 오늘의 테스트 전체

VS Code 터미널에서 [`test_w1d4.py`](../../exercises/week1/tests/test_w1d4.py)의 오늘 테스트를 실행하세요.

```bash
pytest exercises/week1/tests/test_w1d4.py
```

✔ **`12 passed`**가 나와야 합니다. VS Code 터미널에서 `python3 next.py`를 실행하세요.

---

## 9. 오늘 마치기 전에

VS Code 터미널에서 `python3 next.py`를 실행하세요. 오늘 남은 단계를 하나씩 안내합니다.

- 수업 내용을 설명할 수 있는지 묻는 질문에 답하세요.
- 실습 일지를 **직접** 쓰세요. `python3 next.py`는 일지를 대신 써 주지 않고, 썼는지만 확인합니다. 제목의 날짜, 오늘 수업, 배운 내용, 겪은 문제, 질문, 공부한 시간을 **모두** 채우세요. 일지 양식에서 ✏️ 표시가 있는 곳이 채울 곳입니다.
- 멘토와 점검하세요. 멘토가 확인하면 점검 질문에 `y`로 답하세요.
- **마지막으로** 커밋하고 푸시하세요. 오늘의 코드, 실습 일지, 진도가 모두 GitHub로 갑니다. 푸시했는지는 다음에 `python3 next.py`를 실행할 때 자동으로 확인합니다.

푸시까지 마치면 오늘 공부는 끝입니다. `python3 next.py`에 **5일차**가 나타나도 오늘은 시작하지 마세요. 다음 학습일에 `python3 next.py`를 실행하고 5일차 수업을 시작하세요.

**다음:** [5일차: 문자열 다루기 + 주간 과제](day5-strings-and-checkpoint.md)

# 1주차 주간 과제: 로봇 콘솔 도구

이번 주를 마무리하는 주간 과제(체크포인트)입니다. 출력, 입력, 숫자, `if` 문, 반복문, 문자열 등 1주차에 배운 내용을 **모두** 사용합니다.

작은 프로그램 두 개를 만듭니다.

1. [`converter.py`](converter.py): 메뉴가 있는 단위 변환기
2. [`guess.py`](guess.py): 숫자 맞히기 게임

한 번에 모두 작성하지 마세요. 아래 네 단계마다 **작은 테스트 명령**이 있습니다. 한 단계를 작성하고 그 단계의 테스트가 통과하면 다음 단계로 넘어가세요.

| 단계 | 테스트 명령 | 나와야 할 결과 |
|---|---|---|
| 1부 1단계: 변환 함수 | `pytest checkpoints/week1 -k to_` | `4 passed, 7 deselected` |
| 1부 2단계: 메뉴 | `pytest checkpoints/week1 -k converter` | `2 passed, 9 deselected` |
| 2부 1단계: `check_guess` | `pytest checkpoints/week1 -k check_guess` | `3 passed, 8 deselected` |
| 2부 2단계: 게임 | `pytest checkpoints/week1 -k guess_game` | `2 passed, 9 deselected` |

두 프로그램을 모두 완성한 뒤 VS Code 터미널에 다음 테스트 명령을 입력하세요. 결과가 `11 passed`이면 완료입니다.

```bash
pytest checkpoints/week1
```

그런 다음 VS Code 터미널에서 `python3 checkpoints/week1/converter.py`를 실행하세요. 아래 변환기 예제의 입력값을 입력하세요.
`Choose:`에 `q`를 입력해서 VS Code 터미널로 돌아오세요.

이어서 VS Code 터미널에서 `python3 checkpoints/week1/guess.py`를 실행하세요. 게임을 해 보고 두 프로그램을 멘토에게 보여 주세요.
정답은 무작위이므로 추측한 숫자는 예제와 달라도 됩니다.

---

## 1부: `converter.py`

로봇은 여러 단위를 사용합니다. 센서 데이터의 단위와 ROS에 필요한 단위가 다를 때가 많습니다. 예를 들어 ROS는 항상 **미터**와 **라디안**을 사용합니다.

### 1단계: 변환 함수 네 개

먼저 VS Code 편집기에서 [`converter.py`](converter.py)를 여세요. **Ctrl + P**를 누르세요.
`checkpoints/week1/converter.py`를 입력하고 Enter를 누르면 시작 파일이 편집기에 열립니다. 또는 VS Code 편집기 왼쪽 파일 목록(**Explorer**)에서 [`checkpoints`](../) → [`week1`](./) → [`converter.py`](converter.py)를 클릭하세요.

VS Code 편집기에서 `converter.py`의 주석을 읽으세요. 각 변환 함수의 `pass`를 아래 값을 반환하는 코드로 바꾸세요.
함수 이름과 매개변수는 그대로 두세요. VS Code 편집기에서 **Ctrl + S**로 `converter.py`를 저장하세요.
파일 탭의 **●**가 사라집니다.

| 함수 | 공식 | 예 |
|---|---|---|
| `c_to_f(c)` | `c * 9 / 5 + 32` | `c_to_f(100)`은 `212.0`을 반환합니다 |
| `f_to_c(f)` | `(f - 32) * 5 / 9` | `f_to_c(32)`는 `0.0`을 반환합니다 |
| `mm_to_m(mm)` | `mm / 1000` | `mm_to_m(1500)`은 `1.5`를 반환합니다 |
| `deg_to_rad(deg)` | `deg * math.pi / 180` | `deg_to_rad(180)`은 `3.14159...`를 반환합니다 |

`math.pi`는 `math` 모듈에서 가져옵니다. 시작 파일 맨 위에 이미 `import math`가 있습니다.

**확인하기:** VS Code 터미널에서 `python3 -i checkpoints/week1/converter.py`를 실행하세요. `main()`은 아직 `pass`뿐이므로 바로 `>>>`가 나타납니다. `>>>`에 `c_to_f(100)`을 입력해서 `212.0`이 나오는지 확인하고, 다른 함수도 표의 예로 확인하세요. `exit()`으로 나온 뒤 `pytest checkpoints/week1 -k to_`를 실행하세요. `4 passed, 7 deselected`가 나와야 합니다.

### 2단계: `main()`의 메뉴

VS Code 편집기에서 `converter.py`의 `main()` 안에 있는 `pass`를 바꾸세요. `q`를 입력할 때까지 아래 동작을 순서대로 수행하는 반복문을 작성하세요.
프로그램을 실행하기 전에 VS Code 편집기에서 **Ctrl + S**로 `converter.py`를 저장하세요.
아래 내용은 터미널 명령이 아니라 프로그램이 해야 할 동작입니다.

1. 메뉴를 출력하세요.
   ```
   === Unit Converter ===
   1) Celsius -> Fahrenheit
   2) Fahrenheit -> Celsius
   3) Millimeters -> Meters
   4) Degrees -> Radians
   q) Quit
   ```
2. `Choose: `로 입력을 요청하세요.
3. 선택이 `q`이면 `Bye!`를 출력하고 반복문을 끝내세요.
4. 선택이 `1`, `2`, `3`, `4`이면 `Value: `로 값을 입력받고, 알맞은 함수로 변환한 뒤 소수점 아래 두 자리까지 결과를 출력하세요: `Result: 212.00`
   `input()`은 항상 문자열을 돌려주므로 선택값은 `"1"`, `"2"`처럼 **문자열**과 비교하세요(`choice == "1"`). `q`도 입력해야 하므로 선택값을 `int()`로 바꾸지 마세요. `Value:`로 받은 값만 `float()`로 바꾸세요.
5. 그 밖의 선택이면 `Unknown choice.`를 출력하세요.

실행 예제(`Choose:`와 `Value:` 뒤의 값은 직접 입력합니다):

```
=== Unit Converter ===
...
Choose: 1
Value: 100
Result: 212.00
=== Unit Converter ===
...
Choose: 7
Unknown choice.
=== Unit Converter ===
...
Choose: q
Bye!
```

힌트:
- "q를 입력할 때까지 반복"하려면 `while True:`와 `break`가 잘 맞습니다.
- `36.6` 같은 소수도 입력할 수 있도록 `main()`에서 `float(input("Value: "))`를 사용하세요.
- `main()`은 이 프로그램의 입력과 출력을 담당하는 함수입니다. 변환 함수는 값을 `return`으로 돌려주고, `main()`이 그 함수를 호출해서 결과를 출력합니다. `input()`은 파일 맨 아래가 아니라 `main()` 안에 작성하세요.

**확인하기:** `python3 checkpoints/week1/converter.py`로 위의 실행 예제처럼 입력해 보세요. 그런 다음 `pytest checkpoints/week1 -k converter`를 실행하세요. `2 passed, 9 deselected`가 나와야 합니다.

---

## 2부: `guess.py`

### 1단계: `check_guess(secret, guess)`

먼저 VS Code 편집기에서 [`guess.py`](guess.py)를 여세요. **Ctrl + P**를 누르세요.
`checkpoints/week1/guess.py`를 입력하고 Enter를 누르면 시작 파일이 편집기에 열립니다. 또는 VS Code 편집기 왼쪽 파일 목록(**Explorer**)에서 [`checkpoints`](../) → [`week1`](./) → [`guess.py`](guess.py)를 클릭하세요.

VS Code 편집기에서 `guess.py`의 주석을 읽으세요. `check_guess(secret, guess)` 안의 `pass`를 아래 값을 반환하는 코드로 바꾸세요.
함수 이름과 매개변수는 그대로 두세요. VS Code 편집기에서 **Ctrl + S**로 `guess.py`를 저장하세요.
파일 탭의 **●**가 사라집니다.

다음 값을 반환하세요.
- `guess`가 `secret`보다 작으면 `"Too low"`
- `guess`가 `secret`보다 크면 `"Too high"`
- 같으면 `"Correct!"`

**확인하기:** `pytest checkpoints/week1 -k check_guess`를 실행하세요. `3 passed, 8 deselected`가 나와야 합니다.

### 2단계: `main()`의 게임

VS Code 편집기에서 `guess.py`의 `main()` 안에 있는 `pass`를 바꾸세요. 아래 동작을 순서대로 수행하는 코드를 작성하세요.
프로그램을 실행하기 전에 VS Code 편집기에서 **Ctrl + S**로 `guess.py`를 저장하세요.
아래 내용은 터미널 명령이 아니라 프로그램이 해야 할 동작입니다.

1. 정답을 고르세요: `secret = random.randint(1, 100)`
   `random.randint(1, 100)`은 1부터 100까지(둘 다 포함) 정수 하나를 무작위로 고릅니다. 시작 파일 맨 위에 이미 `import random`이 있습니다. 이 줄은 반복문을 시작하기 **전에 한 번만** 실행하세요. 반복문 안에 두면 추측할 때마다 정답이 바뀝니다. 실행 예제의 42는 설명용이니 코드에 42를 쓰지 마세요.
   시도 횟수를 셀 변수(예: `tries = 0`)도 반복문 **앞에** 만드세요.
2. 다음 동작을 반복하세요.
   - `Your guess: `로 입력을 요청하세요.
   - 입력을 **문자열 그대로** 저장하세요. 여기서는 `int(input(...))`를 쓰지 마세요. `abc`를 `int()`로 바꾸면 오류가 나기 때문입니다.
   - 입력한 문자열이 숫자가 아니면(힌트: `.isdigit()`) `Please enter a number.`를 출력하고 `continue`로 다시 입력받으세요. **시도 횟수에는 포함하지 마세요.**
   - 숫자이면 입력한 문자열을 `int`로 바꾸고, 시도 횟수를 1 늘리고, `check_guess(secret, guess)`의 결과를 출력하세요.
   - `check_guess(secret, guess)`가 `"Correct!"`를 반환하면 f-문자열로 `You got it in N tries!`를 출력하고 `break`로 끝내세요. `N` 자리에 시도 횟수를 넣으세요(예: `You got it in 3 tries!`). 한 번에 맞혀도 `You got it in 1 tries!`를 그대로 출력하세요. 테스트가 이 문구를 확인하므로 `try`로 바꾸지 마세요.

실행 예제(정답이 42인 경우):

```
Your guess: 50
Too high
Your guess: abc
Please enter a number.
Your guess: 25
Too low
Your guess: 42
Correct!
You got it in 3 tries!
```

**확인하기:** `python3 checkpoints/week1/guess.py`로 게임을 해 보세요. 그런 다음 `pytest checkpoints/week1 -k guess_game`을 실행하세요. `2 passed, 9 deselected`가 나와야 합니다. 마지막으로 `pytest checkpoints/week1`에서 `11 passed`를 확인하세요.

> ⚠ 프로그램이나 테스트가 끝나지 않고 같은 줄을 계속 출력하거나 아무것도 나오지 않으면 VS Code 터미널에서 **Ctrl + C**를 누르세요. `input("Your guess: ")`가 반복문 **안에** 있는지 확인하세요. 반복문 앞에서 한 번만 입력받으면 같은 추측을 끝없이 반복합니다.

---

## 추가 도전(테스트하지 않습니다)

- [`converter.py`](converter.py)의 `main()` 메뉴에 `5) Meters -> Millimeters`와 `6) Radians -> Degrees`를 추가하세요.
- [`guess.py`](guess.py)에서 사용자가 먼저 범위(예: 1부터 1000까지)를 고를 수 있게 하세요.
- `guess.py`에서 게임이 끝난 뒤 `Play again? (y/n)`으로 다시 할지 물어보세요.

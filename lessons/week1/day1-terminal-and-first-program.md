# 1주차 · 1일차: 터미널과 첫 프로그램

**배울 내용:** VS Code 터미널에서 폴더를 이동하는 방법, 파이썬 실행 방법, 글자를 출력하는 방법, 오류 메시지 읽는 방법을 배웁니다.

**로봇을 다룰 때 필요한 이유:** ROS 2에서는 로봇을 시작하고, 센서 데이터를 살펴보고, 문제를 해결하는 일을 거의 모두 터미널에서 합니다. 터미널에 익숙한 로봇 엔지니어는 훨씬 빠르게 일할 수 있습니다.

---

## 1. 터미널

**Ctrl + `**(또는 **Terminal → New Terminal**)로 **VS Code 터미널**을 여세요. 과정 폴더에서 시작하고 가상 환경이 활성화되어 있습니다. [어디에 입력합니까?](../../docs/01-how-to-study.md#어디에-입력합니까)를 참고하세요. VS Code 터미널에 `pwd`를 입력하면 `/home/<name>/code/python-for-ros-crash-course`가 나옵니다. `<name>`은 Ubuntu 사용자 이름입니다. 커서 앞의 글자를 **프롬프트**라고 합니다. 사용자 이름과 현재 폴더를 보여 줍니다. 예를 들어 홈 폴더로 이동하면 다음과 같이 보일 수 있습니다.

```
minjun@robot-pc:~$
```

`~`는 **홈 폴더**(`/home/minjun`)를 뜻합니다.

### 폴더 이동하기

| 명령 | 하는 일 | 예 |
|---|---|---|
| `pwd` | 현재 작업 폴더를 표시합니다. 지금 어디에 있습니까? | `pwd` |
| `ls` | 현재 폴더의 파일 목록을 보여 줍니다 | `ls` |
| `cd folder` | 폴더 안으로 이동합니다 | `cd code` |
| `cd ..` | 한 단계 위 폴더로 이동합니다 | `cd ..` |
| `cd ~` | 홈 폴더로 돌아갑니다 | `cd ~` |
| `mkdir name` | 새 폴더를 만듭니다 | `mkdir test` |
| `cat file` | 파일 내용을 보여 줍니다 | `cat README.md` |
| `clear` | 화면을 깨끗이 지웁니다 | `clear` |

### 직접 해 보기: 폴더 이동

VS Code 터미널에 아래 내용을 한 줄씩 순서대로 입력하고, 각 줄 뒤에 Enter를 누르세요.

```bash
cd ~
pwd
ls
mkdir playground
cd playground
pwd
cd ..
ls
```

마지막 `ls`에서 새로 만든 `playground` 폴더가 보여야 합니다. `mkdir: cannot create directory 'playground': File exists`가 나오면 폴더가 이미 있다는 뜻이니 괜찮습니다. 계속 진행하세요.

이제 과정 폴더로 돌아가세요. VS Code 터미널에 다음 명령을 입력하세요.

```bash
cd ~/code/python-for-ros-crash-course
pwd
```

✔ `pwd`에 `/home/<name>/code/python-for-ros-crash-course`가 다시 나옵니다. 이후 과정은 이 폴더에서 계속 진행하세요.

VS Code 터미널에서 복사는 **Ctrl + Shift + C**, 붙여 넣기는 **Ctrl + Shift + V**로 합니다.

### 시간을 아껴 주는 단축키 세 가지

- **Tab**: 이름을 자동으로 완성해 줍니다. 과정 폴더에서 VS Code 터미널에 `cd les`를 입력하고 Tab을 누르면 `cd lessons/`로 완성됩니다. Enter를 눌렀다면 `cd ..`로 과정 폴더에 돌아오세요.
- **↑(위쪽 방향키)**: 이전 명령을 다시 보여 줍니다. 여러 번 누르면 더 이전 명령도 볼 수 있습니다.
- **Ctrl + C**: 실행 중인 프로그램을 멈춥니다(예: 끝나지 않는 프로그램). 파이썬 프로그램을 멈추면 마지막 줄에 `KeyboardInterrupt`가 나옵니다. 직접 멈췄다는 뜻이니 정상입니다.

ROS에서는 `/rail_robot/lidar/scan`처럼 긴 이름을 입력합니다. VS Code 터미널에서 Tab을 눌러 긴 명령 이름을 자동으로 완성하세요.


---

## 2. 파이썬과 대화하기

파이썬에는 **대화형 모드**가 있습니다. 한 줄을 입력하면 파이썬이 바로 답합니다. VS Code 터미널에 `python3`를 입력하고 Enter를 누르세요.

```bash
python3
```

`>>>`가 보입니다. 이 파이썬 프롬프트에 아래 `>>>` 뒤의 식을 하나씩 입력하고 Enter를 누르세요. `>>>`는 입력하지 마세요. 나머지 줄은 예상 결과입니다.

```python
>>> 2 + 3
5
>>> 10 * 7
70
>>> "robot"
'robot'
```

파이썬 `>>>` 프롬프트에 `exit()`을 입력하고 Enter를 눌러 VS Code 터미널로 돌아오세요.

```python
>>> exit()
```

`>>>`가 아닌 VS Code 터미널 프롬프트에 `exit()`을 입력하면 `>`만 보이고 명령이 실행되지 않습니다. 이때는 **Ctrl + C**를 누르세요. 프롬프트가 다시 나타납니다.

작은 아이디어를 빠르게 확인할 때 대화형 모드를 사용합니다. 실제 프로그램은 **파일**에 작성합니다.

---

## 3. 첫 프로그램 파일

파이썬 프로그램은 이름이 `.py`로 끝나는 텍스트 파일입니다. 파이썬은 파일을 **위에서 아래로** 읽으며 각 줄을 실행합니다.

VS Code 터미널에 다음 명령을 입력해서 같은 VS Code 창에 `playground.py`를 여세요.

```bash
code playground.py
```

`playground.py`는 아직 없는 파일입니다. 이 명령은 과정 폴더에 새 빈 파일을 열고, **Ctrl + S**로 저장할 때 파일이 만들어집니다. 1절에서 만든 `playground` 폴더와는 다른 것입니다.

VS Code 편집기에서 `playground.py`에 다음 코드를 입력하고 **Ctrl + S**로 저장하세요.

```python
print("Hello!")
print("I am a robot.")
```

VS Code 터미널에 `python3 playground.py`를 입력하세요.

```bash
python3 playground.py
```

출력:

```
Hello!
I am a robot.
```

### `print()`

`print()`는 화면에 내용을 보여 줍니다. 문자열은 따옴표 안에 써야 합니다. 큰따옴표 `"double"`과 작은따옴표 `'single'` 모두 사용할 수 있습니다.

```python
print("Battery OK")
print('Battery OK')       # 같은 결과입니다
print()                   # 빈 줄을 출력합니다
print("Speed:", 2.5)      # 쉼표를 쓰면 각 부분 사이에 공백이 들어갑니다
print(3 + 4)              # 파이썬이 먼저 계산한 뒤 7을 출력합니다
```

### 주석

`#` 뒤의 내용은 모두 **주석**입니다. 파이썬은 주석을 실행하지 않습니다. 사람이 읽는 메모입니다.

```python
# 이 프로그램은 로봇 배터리를 확인합니다
print("Battery OK")  # 주석은 줄 끝에도 쓸 수 있습니다
```

### 직접 해 보기: 출력

VS Code 편집기에서 `playground.py`의 내용을 아래 문구를 출력하는 프로그램으로 바꾸세요. **Ctrl + S**로 저장한 뒤 VS Code 터미널에 `python3 playground.py`를 입력하고 출력을 비교하세요.

```
=== Robot RR-01 ===
Speed: 0.5 m/s

Ready to start.
```

(`Ready to start.` 앞에는 빈 줄이 있습니다.)

---

## 4. 오류 메시지는 도움이 됩니다

누구나 실수합니다. 전문 엔지니어도 매일 오류를 만납니다. 중요한 것은 오류 메시지를 **읽는** 능력입니다.

VS Code 편집기에서 `playground.py`의 내용을 다음 코드로 바꾸고 **Ctrl + S**로 저장하세요(닫는 따옴표가 빠져 있습니다).

```python
print("Hello!)
```

VS Code 터미널에 `python3 playground.py`를 입력하세요. 다음 오류가 나와야 합니다.

```
  File "/home/minjun/code/python-for-ros-crash-course/playground.py", line 1
    print("Hello!)
          ^
SyntaxError: unterminated string literal (detected at line 1)
```

다음처럼 읽으세요.

1. **마지막 줄부터 읽으세요:** `SyntaxError: unterminated string literal`은 문자열을 닫지 않았다는 뜻입니다.
2. **줄 번호:** `line 1`은 1번째 줄에 오류가 있다는 뜻입니다.
3. **`^`**는 문제가 시작되는 위치를 가리킵니다.

자주 나오는 다른 오류도 확인해 보세요. VS Code에서 `playground.py`의 내용을 아래 코드로 바꾸고 **Ctrl + S**로 저장하세요. VS Code 터미널에 `python3 playground.py`를 입력하면 아래 `NameError`가 나옵니다.

```python
prnt("Hello!")
```

```
NameError: name 'prnt' is not defined. Did you mean: 'print'?
```

파이썬은 `prnt`를 알지 못합니다. 어떤 이름을 쓰려고 했는지 짐작해서 알려 주기도 합니다!

### 1일차에 자주 나오는 오류

| 오류 | 흔한 원인 |
|---|---|
| `SyntaxError` | 따옴표 `"` 또는 괄호 `)`가 빠졌습니다 |
| `SyntaxError: invalid character` | 비슷하게 보이지만 다른 문자가 들어 있습니다. 전각 괄호 `（ ）`나 둥근 따옴표 `“ ”`는 문서나 메신저에서 코드를 복사하면 자주 생깁니다. 표시된 문자를 지우고 키보드로 `(` `)` `"`를 다시 입력하세요 |
| `NameError` | 이름을 잘못 입력했거나 문자열에 따옴표가 없습니다: `print(Hello)` |
| `IndentationError` | 줄 시작 부분에 불필요한 공백이 있습니다 |
| `python3: can't open file` | 다른 폴더에 있거나 파일 이름을 잘못 입력했습니다. VS Code 터미널에서 `pwd`로 현재 폴더를, `ls`로 파일 목록을 확인하세요. |

---

## 5. 연습 문제

> 처음입니까? 시작하기 전에 [연습 문제 진행 방법](../../docs/02-how-exercises-work.md) 1–3부를 읽으세요.

`playground.py`는 아래 예제를 실행할 때 계속 사용합니다. Git이 이 파일을 무시하므로 커밋에는 포함되지 않습니다. 오류 실습에서 일부러 틀리게 쓴 `prnt("Hello!")` 줄은 이제 지우세요. **새 예제를 시작할 때마다 `playground.py`의 이전 내용을 모두 지우고 새 예제만 입력하세요.**

**연습 문제 진행 방법:** 한 번에 하나씩 **순서대로** 푸세요. 아래의 각 연습 문제에는 번호가 붙은 진행 순서가 있습니다. 1번부터 끝까지 따라 한 뒤 다음 연습 문제로 넘어가세요. 잘되지 않는 단계가 있으면 [연습 문제 진행 방법 5부](../../docs/02-how-exercises-work.md#5부-테스트-결과-읽기)를 참고하세요.

오늘 연습 문제는 출력을 **정확히** 확인합니다. 대문자, 공백, 문장 부호 하나하나가 중요합니다. `Hello, ROS!`는 `Hello ROS!`나 `hello, ros!`와 다릅니다.

### 연습 문제 1/2: Hello, ROS!

> 📖 **시작하기 전에:** [연습 문제 진행 방법](../../docs/02-how-exercises-work.md)을 이 수업 옆에 여세요.
> [3부: 스크립트 연습 문제](../../docs/02-how-exercises-work.md#3부-스크립트-연습-문제-따라-하기-12일차)와 [5부: 테스트 결과 읽기](../../docs/02-how-exercises-work.md#5부-테스트-결과-읽기)를 따라 하세요.

**할 일:** `Hello, ROS!` 한 줄을 출력하는 프로그램을 작성하세요.

**실행 결과 예시:**

```
$ python3 exercises/week1/w1d1_hello.py
Hello, ROS!
```

**따라 해 볼 예제:** 비슷한 문제입니다(이 연습 문제의 정답은 아닙니다).

이 프로그램은 로봇 팀에 인사합니다.

```python
print("Good morning, robot team!")
```

예제를 실행해 보세요. VS Code 터미널에 `code playground.py`를 입력해서 같은 VS Code 창에 `playground.py`를 여세요.
VS Code 편집기에서 `playground.py`에 예제를 입력하세요. **Ctrl + S**로 `playground.py`를 저장하세요.
VS Code 터미널에서 `python3 playground.py`를 실행하세요.

```
$ python3 playground.py
Good morning, robot team!
```

예제가 어떻게 동작하는지 이해했다면 아래 순서대로 진행하세요. 연습 문제 코드는 직접 작성하세요. 할 일이 다르니 예제를 그대로 복사하지 마세요.

**진행 순서:**

1. **파일을 여세요.** VS Code 편집기에서 **Ctrl + P**를 누르세요.
   VS Code 위쪽에 나타난 입력 칸에 [`exercises/week1/w1d1_hello.py`](../../exercises/week1/w1d1_hello.py)를 입력하고 Enter를 누르세요. 편집기에 파일이 열립니다. 또는 VS Code 편집기 왼쪽 파일 목록(**Explorer**)에서 [`exercises`](../../exercises/) → [`week1`](../../exercises/week1/) → [`w1d1_hello.py`](../../exercises/week1/w1d1_hello.py)를 클릭하세요.
2. VS Code 편집기에서 `w1d1_hello.py` 맨 위의 안내를 읽으세요.
3. VS Code 편집기에서 `w1d1_hello.py`의 `# TODO: 이 줄 아래에 코드를 작성하세요` 아래 빈 줄에 코드를 작성하세요. `print()` 하나가 필요합니다.
4. VS Code 편집기에서 **Ctrl + S**로 `w1d1_hello.py`를 저장하세요. 저장하면 파일 탭의 **●**가 사라집니다.
5. VS Code 터미널에서 `w1d1_hello.py`를 실행하세요.
   ```bash
   python3 exercises/week1/w1d1_hello.py
   ```
   ✔ `Hello, ROS!`가 나와야 합니다.
   ✘ **아무것도 나타나지 않으면** 파일에 아직 코드가 없거나 저장하지 않은 것입니다. 3단계로 돌아가세요.
6. VS Code 터미널에서 [`test_w1d1.py`](../../exercises/week1/tests/test_w1d1.py)로 `w1d1_hello.py`를 테스트하세요.
   ```bash
   pytest exercises/week1/tests/test_w1d1.py -k hello
   ```
   ✔ `1 passed, 1 deselected`가 나와야 합니다. 테스트가 실패하면 VS Code 터미널의 오류 메시지를 읽고 VS Code에서 `exercises/week1/w1d1_hello.py`를 고친 뒤 4단계로 돌아가세요.
7. VS Code 터미널에서 `python3 next.py`를 실행하세요. 테스트가 통과했으면 다음 단계가 나타납니다.

> `deselected`는 이 파일에 있는 **다른** 연습 문제의 테스트는 실행하지 않았다는 뜻입니다. `-k`를 사용하면 이렇게 되니 괜찮습니다.

### 연습 문제 2/2: 로봇 정보 카드

> 📖 **시작하기 전에:** [연습 문제 진행 방법](../../docs/02-how-exercises-work.md)을 이 수업 옆에 여세요.
> [3부: 스크립트 연습 문제](../../docs/02-how-exercises-work.md#3부-스크립트-연습-문제-따라-하기-12일차)와 [5부: 테스트 결과 읽기](../../docs/02-how-exercises-work.md#5부-테스트-결과-읽기)를 따라 하세요.

**할 일:** 다음 세 줄을 정확히 출력하는 프로그램을 작성하세요.

```
Robot: RR-01
Type: Rail robot
Status: READY
```

**따라 해 볼 예제:** 비슷한 문제입니다(이 연습 문제의 정답은 아닙니다).

이 프로그램은 한 줄마다 `print()` 하나를 사용해서 드론 정보 카드를 출력합니다.

```python
print("Drone: DR-07")
print("Type: Quadcopter")
print("Status: CHARGING")
```

예제를 실행해 보세요. VS Code 터미널에 `code playground.py`를 입력해서 같은 VS Code 창에 `playground.py`를 여세요.
VS Code 편집기에서 `playground.py`에 예제를 입력하세요. **Ctrl + S**로 `playground.py`를 저장하세요.
VS Code 터미널에서 `python3 playground.py`를 실행하세요.

```
$ python3 playground.py
Drone: DR-07
Type: Quadcopter
Status: CHARGING
```

예제가 어떻게 동작하는지 이해했다면 아래 순서대로 진행하세요. 연습 문제 코드는 직접 작성하세요. 할 일이 다르니 예제를 그대로 복사하지 마세요.

**진행 순서:**

1. **파일을 여세요.** VS Code 편집기에서 **Ctrl + P**를 누르세요.
   VS Code 위쪽에 나타난 입력 칸에 [`exercises/week1/w1d1_robot_card.py`](../../exercises/week1/w1d1_robot_card.py)를 입력하고 Enter를 누르세요. 편집기에 파일이 열립니다. 또는 VS Code 편집기 왼쪽 파일 목록(**Explorer**)에서 [`exercises`](../../exercises/) → [`week1`](../../exercises/week1/) → [`w1d1_robot_card.py`](../../exercises/week1/w1d1_robot_card.py)를 클릭하세요.
2. VS Code 편집기에서 `w1d1_robot_card.py` 맨 위의 안내를 읽으세요.
3. VS Code 편집기에서 `w1d1_robot_card.py`의 `TODO` 아래에 코드를 작성하세요. 각 줄마다 `print()` 하나를 사용하세요.
4. VS Code 편집기에서 **Ctrl + S**로 `w1d1_robot_card.py`를 저장하세요. 저장하면 파일 탭의 **●**가 사라집니다.
5. VS Code 터미널에서 `w1d1_robot_card.py`를 실행하세요.
   ```bash
   python3 exercises/week1/w1d1_robot_card.py
   ```
   ✔ 위의 세 줄이 나와야 합니다. VS Code 터미널의 출력을 **할 일** 아래의 세 줄과 한 글자씩 비교하세요.
   ✘ **아무것도 나타나지 않으면** 파일에 아직 코드가 없거나 저장하지 않은 것입니다. 3단계로 돌아가세요.
6. VS Code 터미널에서 [`test_w1d1.py`](../../exercises/week1/tests/test_w1d1.py)로 `w1d1_robot_card.py`를 테스트하세요.
   ```bash
   pytest exercises/week1/tests/test_w1d1.py -k robot_card
   ```
   ✔ `1 passed, 1 deselected`가 나와야 합니다.
7. 아직 `python3 next.py`를 실행하지 마세요. 아래 **마지막으로: 오늘의 테스트 전체**로 가세요. `python3 next.py`는 그 절의 테스트를 실행한 다음에 실행합니다.

### 마지막으로: 오늘의 테스트 전체

VS Code 터미널에서 [`test_w1d1.py`](../../exercises/week1/tests/test_w1d1.py)의 오늘 테스트를 실행하세요.

```bash
pytest exercises/week1/tests/test_w1d1.py
```

✔ **`2 passed`**가 나와야 합니다. VS Code 터미널에서 `python3 next.py`를 실행하세요.

---

## 6. 오늘 마치기 전에

VS Code 터미널에서 `python3 next.py`를 실행하세요. 오늘 남은 단계를 하나씩 안내합니다.

- 수업 내용을 설명할 수 있는지 묻는 질문에 답하세요.
- 실습 일지를 **직접** 쓰세요. `python3 next.py`는 일지를 대신 써 주지 않고, 썼는지만 확인합니다. 제목의 날짜, 오늘 수업, 배운 내용, 겪은 문제, 질문, 공부한 시간을 **모두** 채우세요. 일지 양식에서 ✏️ 표시가 있는 곳이 채울 곳입니다.
- 멘토와 점검하세요. 멘토가 확인하면 점검 질문에 `y`로 답하세요.
- **마지막으로** 커밋하고 푸시하세요. 오늘의 코드, 실습 일지, 진도가 모두 GitHub로 갑니다. 푸시했는지는 다음에 `python3 next.py`를 실행할 때 자동으로 확인합니다.

푸시까지 마치면 오늘 공부는 끝입니다. `python3 next.py`에 **2일차**가 나타나도 오늘은 시작하지 마세요. 다음 학습일에 `python3 next.py`를 실행하고 2일차 수업을 시작하세요.

**다음:** [2일차: 변수, 숫자, 입력](day2-variables-numbers-input.md)

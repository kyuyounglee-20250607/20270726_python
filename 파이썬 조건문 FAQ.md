📘 파이썬 조건문 FAQ

1. ✅ 파이썬 조건문이란 무엇이며, 언제 사용하나요?
조건문은 특정 조건이 True일 때 특정 코드 블록을 실행하도록 하는 프로그래밍 구문입니다.
예: 사용자 입력 값에 따라 메시지 출력, 점수에 따라 학점 부여 등.

---

2. ✅ 파이썬 조건문의 기본 구조는 어떻게 되나요?
기본 구조:
if 조건식:
    실행할 코드
elif 조건식:
    실행할 코드
else:
    실행할 코드

예시:
num = -5
if num > 0:
    print("양수입니다")
elif num < 0:
    print("음수입니다")
else:
    print("0입니다")

---

3. ✅ 조건문에서 사용할 수 있는 주요 연산자에는 어떤 것들이 있나요?
- 비교 연산자: ==, !=, >, <, >=, <=
- 논리 연산자: and, or, not
- 멤버 연산자: in, not in

예시:
num = 15
if num >= 10 and num <= 20:
    print("10 이상 20 이하입니다")

fruits = ["사과", "바나나", "귤"]
if "귤" in fruits:
    print("귤이 있습니다")

---

4. ✅ and, or, not과 같은 논리 연산자는 어떻게 활용되나요?
- and: 모두 참일 때 True
- or: 하나라도 참이면 True
- not: 결과를 반대로

예시:
is_logged_in = False
if not is_logged_in:
    print("로그인이 필요합니다")

year = 2024
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("윤년입니다")
else:
    print("윤년이 아닙니다")

---

5. ✅ "중첩 조건문"이란 무엇이며, 어떤 경우에 사용하나요?
조건문 안에 또 다른 조건문이 있는 구조입니다.

예시:
score = 87
if score >= 60:
    if score >= 90:
        print("A")
    elif score >= 80:
        print("B")
    else:
        print("C 또는 D")
else:
    print("F")

---

6. ✅ "조건 표현 간소화 (한 줄 if)"는 무엇이며, 어떻게 사용하나요?
간단한 조건문을 한 줄로 표현 (삼항 연산자)

형식:
결과1 if 조건 else 결과2

예시:
score = 80
result = "합격" if score >= 60 else "불합격"
print(result)

---

7. ✅ 문자열 비교나 자료형 판별도 조건문으로 가능한가요?
- 문자열 비교: == 사용 (대소문자 구분)
- 자료형 판별: isinstance(변수, 자료형)

예시:
input_id = "admin"
if input_id == "admin":
    print("관리자입니다")
else:
    print("일반 사용자입니다")

value = 123
if isinstance(value, int):
    print("정수입니다")
else:
    print("정수가 아닙니다")

---

8. ✅ 파이썬 조건문을 실생활 문제 해결에 어떻게 적용할 수 있나요?
- 로그인 시스템
- 학점 계산기
- 나이 판별기
- 윤년 계산기
- 쇼핑몰 할인 적용
- 데이터 유효성 검사

예시:
price = 120000
if price >= 100000:
    print("10% 할인 적용")
else:
    print("정가로 구매")

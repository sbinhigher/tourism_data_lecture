# -*- coding: utf-8 -*-
# Week4_Q.py : 컬렉션형 과제(순서형 4, 집합형 3, 매핑형 3)
from IPython.display import display, HTML, Markdown
import io
import contextlib

# ====== 글로벌 아이콘 (사용자가 변경 가능) ======
CORRECT_ICON = "✅"
WRONG_ICON   = "❌"

def set_icons(correct="✅", wrong="❌"):
    global CORRECT_ICON, WRONG_ICON
    CORRECT_ICON, WRONG_ICON = correct, wrong

# ====== 프리뷰 패널 공통 렌더러 ======
PANEL_CSS = """
<style>
.quiz-panel {border:1px solid #e5e7eb;border-left:6px solid #3b82f6;border-radius:10px;
             padding:14px 16px;margin:10px 0;background:#fafbff;font-family:ui-sans-serif,system-ui,-apple-system,Segoe UI,Roboto,Noto Sans,Apple SD Gothic Neo,Helvetica Neue,Arial;}
.quiz-title {font-weight:700;color:#1f2937;margin-bottom:6px;font-size:1.05rem;}
.quiz-body  {color:#374151;line-height:1.6;}
.quiz-code  {background:#111827;color:#e5e7eb;padding:10px 12px;border-radius:8px;
             font-family:ui-monospace,SFMono-Regular,Menlo,Monaco,Consolas,"Liberation Mono",monospace;margin-top:8px;white-space:pre-wrap;}
</style>
"""

def _panel(title, body_md, code=None):
    html = [PANEL_CSS, '<div class="quiz-panel">']
    html += [f'<div class="quiz-title">{title}</div>',
             f'<div class="quiz-body">{body_md}</div>']
    if code:
        html.append(f'<div class="quiz-code">{code}</div>')
    html.append('</div>')
    display(HTML("".join(html)))

# ====== 공용 헬퍼 ======
def _matches_any(user_input, *accepted):
    s = user_input.strip().lower().replace('`', '').replace('"', "'")
    s = " ".join(s.split())
    def norm(a):
        return " ".join(a.strip().lower().replace('`', '').replace('"', "'").split())
    return any(s == norm(a) for a in accepted)

def _ask_until_correct(checker, prompt="> "):
    while True:
        ans = input(prompt)
        ok, msg = checker(ans)
        if ok:
            print(f"{CORRECT_ICON} 정답입니다!\n")
            return ans
        else:
            print(f"{WRONG_ICON} {msg} 다시 시도하세요。\n")

# =========================
# Midterm 시험 문제 : show_qN()
# =========================
def show_q1():
    _panel("Q1", "다음 중 변수(Variable)에 대한 설명으로 틀린 것은?")
    display(Markdown(
        "보기\n\n"
        "1) 변수명에는 알파벳, 숫자, 밑줄(_), 한글 등을 사용할 수 있다\n\n"
        "2) 변수명은 숫자로 시작할 수 없다\n\n"
        "3) 공백이나 특수문자는 변수명으로 사용할 수 없다\n\n"
        "4) for나 True 같은 예약어도 변수명으로 사용할 수 있다\n\n"
        "5) 여러 변수를 동시에 할당할 수 있다"
    ))

def show_q2():
    _panel("Q2", "다음 코드를 실행했을 때, 결과는?", code='print(10+"20")')
    display(Markdown(
        "보기\n\n"
        "1) 30\n\n"
        "2) \"1020\"\n\n"
        "3) 1020\n\n"
        "4) Error 발생"
    ))

def show_q3():
    _panel("Q3", "다음 중 정수와 실수의 덧셈 결과 타입으로 옳은 것은?")
    display(Markdown(
        "보기\n\n"
        "1) int\n\n"
        "2) float\n\n"
        "3) str\n\n"
        "4) bool"
    ))

def show_q4():
    _panel("Q4", "다음 표현식의 결과로 옳은 것은?", code="0.1 + 0.2 == 0.3")
    display(Markdown(
        "보기\n\n"
        "1) True\n\n"
        "2) False"
    ))

def show_q5():
    _panel("Q5", "아래 코드를 실행했을 때, 제시된 변수와 변환 함수만을 사용해서 출력이 \"aB\"가 되도록 ?에 들어갈 구문을 작성하시오.",
           code='a = "A"\nb = "B"\nprint(?)\n-----\naB' )

def show_q6():
    _panel("Q6", "다음 중 문자열 리터럴로 올바른 것은 모두 고르시오.")
    display(Markdown(
        "보기\n\n"
        "1) '10'\n\n"
        "2) \"Hello\"\n\n"
        "3) 10\n\n"
        "4) True"
    ))

def show_q7():
    _panel("Q7", "다음 중 변수명으로 사용할 수 없는 것은?")
    display(Markdown(
        "보기\n\n"
        "1) _score\n\n"
        "2) value2\n\n"
        "3) 2value\n\n"
        "4) 변수"
    ))

def show_q8():
    _panel("Q8", "다음 중 예약어(변수명으로 사용 불가)에 해당하는 것은?")
    display(Markdown(
        "보기\n\n"
        "1) print\n\n"
        "2) True\n\n"
        "3) number\n\n"
        "4) hello"
    ))

def show_q9():
    _panel("Q9", "다음 코드의 출력 결과로 옳은 것은?", code='print("A", "B")')
    display(Markdown(
        "보기\n\n"
        "1) A B\n\n"
        "2) AB\n\n"
        "3) \"A B\"\n\n"
        "4) A, B"
    ))

def show_q10():
    _panel("Q10", "다음 중 print에서 여러 값을 출력할 때 값 사이에 들어갈 구분자를 지정하는 파라미터 이름은?")
    display(Markdown(
        "보기\n\n"
        "1) sep\n\n"
        "2) end\n\n"
        "3) seq\n\n"
        "4) delimiter\n\n"
        "5) split"
    ))

def show_q11():
    _panel(
        "Q11",
        "다음 출력 결과가 정수 10이 되도록, 변수 s를 활용하여 print 내부의 코드를 작성하시오.",
        code="s = '10'\nprint(    )"
    )


def show_q12():
    _panel("Q12", "다음 표현식의 결과로 옳은 것은?", code="type(10) == type(10.0)")
    display(Markdown(
        "보기\n\n"
        "1) True\n\n"
        "2) False"
    ))

def show_q13():
    _panel(
        "Q13",
        "아래 코드를 실행했을 때, 출력이 8이 되도록 ?에 들어갈 구문을 고르시오.",
        code="a = 2\nb = 3\nprint(a ? b)\n-----\n8"
    )
    display(Markdown(
        "보기\n\n"
        "1) \\+\n\n"
        "2) \\*\n\n"
        "3) \\*\\*\n\n"
        "4) <<"
    ))


def show_q14():
    _panel(
        "Q14",
        "다음 코드를 실행했을 때, 출력 값을 정확히 쓰시오.",
        code='s = "Python"\nprint(s[:3])'
    )

def show_q15():
    _panel(
        "Q15",
        "다음 코드를 실행했을 때, 출력 값을 정확히 쓰시오.",
        code='print("aaaaab".replace("a","b",3))'
    )

def show_q16():
    _panel(
        "Q16",
        "다음 중 올바른 설명을 고르시오."
    )
    display(Markdown(
        "보기\n\n"
        "1) \"abc\"[0] = 'a' 는 정상 동작한다\n\n"
        "2) type(10 + 10.0) 는 float 이다\n\n"
        "3) 인덱싱은 1부터 시작한다\n\n"
        "4) \"x\".append('y') 는 문자열에 원소를 추가한다"
    ))


def show_q17():
    _panel(
        "Q17",
        "다음 코드를 실행했을 때, 계산 결과를 숫자로 정확히 쓰시오.",
        code="a=9\nb=5\nc=2\nd=3.0\nexpr=(a//c)+(b%c)-d+2**c\nprint(expr)"
    )


def show_q18():
    _panel(
        "Q18",
        "다음 중 결과가 다른 것은?",
        code='city = "Jeju"\nvisitors = 15200000\nrating = 4.8'
    )
    display(Markdown(
        "보기\n\n"
        "1) print(\"{}는 연간 {}명이 방문합니다.\".format(city, visitors))\n\n"
        "2) print(f\"{city}는 연간 {visitors}명이 방문합니다.\")\n\n"
        "3) print(\"%s는 연간 %d명이 방문합니다.\" % (city, visitors))\n\n"
        "4) print(city, \"는 연간\", visitors, \"명이 방문합니다.\")"
    ))



def show_q19():
    _panel(
        "Q19",
        "다음 중 str(...)로 문자열화한 뒤 원래 값과 동일하게 복원되는 식을 고르시오."
    )
    display(Markdown(
        "보기\n\n"
        "1) int(str(3.14))\n\n"
        "2) float(str(3.14))\n\n"
        "3) bool(str(False))\n\n"
        "4) dict(str({'a':1}))"
    ))


def show_q20():
    _panel(
        "Q20",
        "다음 중 기본형이 아닌 것을 고르시오."
    )
    display(Markdown(
        "보기\n\n"
        "1) set\n\n"
        "2) int\n\n"
        "3) str\n\n"
        "4) bool"
    ))


def show_q21():
    _panel(
        "Q21",
        "다음 중 숫자형 변환 함수 적용 시 에러가 나는 것을 고르시오."
    )
    display(Markdown(
        "보기\n\n"
        "1) int(\"  -12  \")\n\n"
        "2) float(\"12.0\")\n\n"
        "3) int(\"12.0\")\n\n"
        "4) float(\" 12 \")"
    ))

def show_q22():
    _panel(
        "Q22",
        "다음 선택지 중 다른 결과가 나오는 코드를 고르시오.",
        code="s = 'Python'"
    )
    display(Markdown(
        "보기\n\n"
        "1) print(s[:2].upper())\n\n"
        "2) print(s.upper() - s.upper()[2:4])\n\n"
        "3) print(s[0] + s[1].upper())\n\n"
        "4) print(s.replace('Py', 'PY')[0:2])"
    ))


def show_q23():
    _panel(
        "Q23",
        "다음 코드의 출력 결과로 옳은 것을 고르시오.",
        code="a = [0,1,2,3,4]\na[1:4] = [9,9]\nprint(a)"
    )
    display(Markdown(
        "보기\n\n"
        "1) [0,9,9,4]\n\n"
        "2) [0,9,9,3,4]\n\n"
        "3) [0,1,2,3,4]\n\n"
        "4) 오류"
    ))

def show_q24():
    _panel(
        "Q24",
        "다음 코드의 실행 결과로 옳은 것을 고르시오.",
        code="A = {1,2,3}\nB = {3,4}\nC = {4,5,6}\nprint(A.union(B) - C)"
    )
    display(Markdown(
        "보기\n\n"
        "1) {1, 2, 3}\n\n"
        "2) {1, 2}\n\n"
        "3) {1, 2, 3, 3}\n\n"
        "4) {1, 2, 4}"
    ))

def show_q25():
    _panel(
        "Q25",
        "다음 중 딕셔너리의 키로 사용할 수 있는 것을 모두 고르시오."
    )
    display(Markdown(
        "보기\n\n"
        "1) [1, 2]\n\n"
        "2) (1, 2)\n\n"
        "3) {\"a\": 1}\n\n"
        "4) \"key\"\n\n"
        "5) {1, 2}"
    ))

def show_q26():
    _panel(
        "Q26",
        "다음 코드를 실행한 후, 올바른 출력이 되는 것을 모두 고르시오.",
        code=(
            "person = {\"name\": \"Alice\", \"age\": 25, \"city\": \"Seoul\"}\n"
            "person[\"name\"] = \"James\"\n"
            "person[\"job\"] = \"Engineer\"\n"
            "person[\"age\"] = 30\n"
            "del person[\"city\"]\n"
            "# 최종 person: {'name': 'James', 'age': 30, 'job': 'Engineer'}"
        )
    )
    display(Markdown(
        "보기\n\n"
        "1) print(person.keys())    → dict_keys(['name', 'age', 'job', 'city'])\n\n"
        "2) print(person.values())  → dict_values(['James', 30, 'Engineer', 'N/A'])\n\n"
        "3) print(person.items())   → dict_items([('name', 'James'), ('age', 30), ('job', 'Engineer')])\n\n"
        "4) print(person)           → {'name': ['Alice', 'James'], 'age': [25, 30], 'job': ['N/A', 'Engineer']}"
    ))

def show_q27():
    _panel(
        "Q27",
        "다음 중 코드 실행 후의 결과로 옳은 것을 고르시오.",
        code="t = (1, [2, 3])\nt[1].append(4)\nprint(t)"
    )
    display(Markdown(
        "보기\n\n"
        "1) (1, [2, 3, 4])\n\n"
        "2) (1, [2, 3])\n\n"
        "3) 오류\n\n"
        "4) (1, (2, 3, 4))"
    ))

def show_q28():
    _panel(
        "Q28",
        "다음 코드의 출력 결과로 옳은 것을 고르시오.",
        code="print(list(range(2, 8, 2)))"
    )
    display(Markdown(
        "보기\n\n"
        "1) [2,4,6,8]\n\n"
        "2) [2,4,6]\n\n"
        "3) [2,3,4,5,6,7]\n\n"
        "4) [3,5,7]"
    ))

def show_q29():
    _panel(
        "Q29",
        "다음 코드를 실행했을 때, 출력 값을 정확히 쓰시오.",
        code="d = {'x': 1}\nprint(d.get('z', 'N/A'))"
    )

def show_q30():
    _panel(
        "Q30",
        "다음 중 집합 s = {1,2,2,3} 의 길이(요소의 개수)로 옳은 것을 고르시오."
    )
    display(Markdown(
        "보기\n\n"
        "1) 3\n\n"
        "2) 4\n\n"
        "3) 2\n\n"
        "4) 1"
    ))

def show_q31():
    _panel(
        "Q31",
        "다음 중 set에 활용될 수 없는 함수를 고르시오."
    )
    display(Markdown(
        "보기\n\n"
        "1) add\n\n"
        "2) remove\n\n"
        "3) discard\n\n"
        "4) append"
    ))

def show_q32():
    _panel(
        "Q32",
        "다음 중 딕셔너리 관련 설명으로 옳은 것을 모두 고르시오."
    )
    display(Markdown(
        "보기\n\n"
        "1) get은 키가 없을 때 기본값을 반환할 수 있다\n\n"
        "2) 키는 해시 가능해야 한다\n\n"
        "3) 빈 딕셔너리는 set()로 만든다\n\n"
        "4) 리스트는 키로 사용할 수 있다\n\n"
        "5) update는 기존 키의 값을 바꿀 수 있다"
    ))

def show_q33():
    _panel(
        "Q33",
        "다음 중 컬렉션 형이 아닌 데이터를 고르시오."
    )
    display(Markdown(
        "보기\n\n"
        "1) [1, 2, 3]\n\n"
        "2) (1, 2)\n\n"
        "3) {'a': 1, 'b': 2}\n\n"
        "4) 42"
    ))

def show_q34():
    _panel(
        "Q34",
        "다음 코드의 출력 결과로 옳은 것을 고르시오.",
        code=(
            "tensor = [\n"
            "    [1, 2, 3, 4],\n"
            "    [5, 6, 7, 8],\n"
            "    [9, 10, 11, 12]\n"
            "]\n"
            "print(tensor[0:2][1][1:3])"
        )
    )
    display(Markdown(
        "보기\n\n"
        "1) [6, 7]\n\n"
        "2) [1, 2]\n\n"
        "3) [5, 6, 7]\n\n"
        "4) [7, 8]"
    ))


def show_q35():
    _panel(
        "Q35",
        "[1, 2, 3, 4, 5] 가 출력되도록 빈칸에 들어갈 코드를 작성하시오.",
        code="nums = [1, 2, 2, 3, 4, 4, 5]\nprint(    )"
    )


# =========================
# 답안 : answer_qN()
# =========================

def answer_q1(show_explanation: bool = True):
    def checker(src):
        return (src.strip() == "4", "")
    ans = _ask_until_correct(checker)
    if show_explanation: explain_q1()
    return ans

def answer_q2(show_explanation: bool = True):
    def checker(src):
        return (src.strip() == "4", "")
    ans = _ask_until_correct(checker)
    if show_explanation: explain_q2()
    return ans

def answer_q3(show_explanation: bool = True):
    def checker(src):
        return (src.strip() == "2", "")
    ans = _ask_until_correct(checker)
    if show_explanation: explain_q3()
    return ans

def answer_q4(show_explanation: bool = True):
    def checker(src):
        return (src.strip() == "2", "")
    ans = _ask_until_correct(checker)
    if show_explanation: explain_q4()
    return ans

def answer_q5(show_explanation: bool = True):
    a = "A"; b = "B"
    def checker(src):
        try:
            result = eval(src, {}, {"a": a, "b": b})
        except Exception:
            return (False, "")
        return (result == "AB", "")
    ans = _ask_until_correct(checker)
    if show_explanation: explain_q5()
    return ans

def answer_q6(show_explanation: bool = True):
    def checker(src):
        tokens = [t for t in src.replace(",", " ").split() if t]
        return (set(tokens) == {"1", "2"} and len(tokens) == 2, "")
    ans = _ask_until_correct(checker)
    if show_explanation: explain_q6()
    return ans

def answer_q7(show_explanation: bool = True):
    def checker(src):
        return (src.strip() == "3", "")
    ans = _ask_until_correct(checker)
    if show_explanation: explain_q7()
    return ans

def answer_q8(show_explanation: bool = True):
    def checker(src):
        return (src.strip() == "2", "")
    ans = _ask_until_correct(checker)
    if show_explanation: explain_q8()
    return ans

def answer_q9(show_explanation: bool = True):
    def checker(src):
        return (src.strip() == "1", "")
    ans = _ask_until_correct(checker)
    if show_explanation: explain_q9()
    return ans

def answer_q10(show_explanation: bool = True):
    def checker(src):
        return (src.strip() == "1", "")
    ans = _ask_until_correct(checker)
    if show_explanation: explain_q10()
    return ans

def answer_q11(show_explanation: bool = True):
    s = "10"
    def checker(src):
        ns = {"s": s}
        try:
            # 변수 s를 사용했는지 확인(리터럴 '10' 하드코딩 금지)
            if "'10'" in src or '"10"' in src:
                return (False, "")
            val = eval(src, {}, ns)
        except Exception:
            return (False, "")
        ok = (isinstance(val, int) and val == 10)
        # 정답은 변수 s를 이용한 정수 변환만 인정
        # 공백을 무시하고 정확히 int(s) 형태만 허용
        form_ok = "".join(src.split()) == "int(s)"
        return (ok and form_ok, "")
    ans = _ask_until_correct(checker)
    if show_explanation:
        explain_q11()
    return ans

def answer_q12(show_explanation: bool = True):
    def checker(src):
        return (src.strip() == "2", "")
    ans = _ask_until_correct(checker)
    if show_explanation: explain_q12()
    return ans

def answer_q13(show_explanation: bool = True):
    def checker(src):
        return (src.strip() == "3", "")
    ans = _ask_until_correct(checker)
    if show_explanation:
        explain_q13()
    return ans

def answer_q14(show_explanation: bool = True):
    # 예상 맥락: s = "Python" 에서 s[:3]의 값
    def checker(src):
        val = src.strip().strip('"').strip("'")
        return (val == "Pyt", "")
    ans = _ask_until_correct(checker)
    if show_explanation: explain_q14()
    return ans

def answer_q15(show_explanation: bool = True):
    def checker(src):
        val = src.strip().strip('"').strip("'")
        return (val == "bbbaab", "")
    ans = _ask_until_correct(checker)
    if show_explanation:
        explain_q15()
    return ans

def answer_q16(show_explanation: bool = True):
    ans = _ask_until_correct(lambda s: (_matches_any(s, "2", "type(10 + 10.0) 는 float 이다"), ""))
    if show_explanation: explain_q16()
    return ans

def answer_q17(show_explanation: bool = True):
    def checker(s):
        expected = (9 // 2) + (5 % 2) - 3.0 + 2**2  # 6.0
        try:
            return (float(s.strip()) == expected, "")
        except:
            return (False, "")
    ans = _ask_until_correct(checker)
    if show_explanation: explain_q17()
    return ans

def answer_q18(show_explanation: bool = True):
    # 최종 확정: 결과가 다른 것은? (1,2,3 동일 / 4만 다름) → "4"
    ans = _ask_until_correct(lambda s: (s.strip() == "4", ""))
    if show_explanation: explain_q18()
    return ans

def answer_q19(show_explanation: bool = True):
    ans = _ask_until_correct(lambda s: (_matches_any(s, "2", "float(str(3.14))"), ""))
    if show_explanation: explain_q19()
    return ans

def answer_q20(show_explanation: bool = True):
    ans = _ask_until_correct(lambda s: (_matches_any(s, "1", "set"), ""))
    if show_explanation: explain_q20()
    return ans

def answer_q21(show_explanation: bool = True):
    ans = _ask_until_correct(lambda s: (_matches_any(s, "3", "int(\"12.0\")"), ""))
    if show_explanation: explain_q21()
    return ans

def answer_q22(show_explanation: bool = True):
    ans = _ask_until_correct(lambda s: (s.strip() == "2", ""))
    if show_explanation:
        explain_q22()
    return ans

def answer_q23(show_explanation: bool = True):
    def checker(src):
        return (src.strip() == "1", "")
    ans = _ask_until_correct(checker)
    if show_explanation: explain_q23()
    return ans

def answer_q24(show_explanation: bool = True):
    ans = _ask_until_correct(lambda s: (s.strip() == "1", ""))
    if show_explanation:
        explain_q24()
    return ans

def answer_q25(show_explanation: bool = True):
    def checker(src):
        tokens = [t for t in src.replace(",", " ").split() if t]
        ok = set(tokens) == {"2", "4"} and len(tokens) == 2
        return (ok, "")
    ans = _ask_until_correct(checker)
    if show_explanation: explain_q25()
    return ans

def answer_q26(show_explanation: bool = True):
    def checker(src):
        tokens = [t for t in src.replace(",", " ").split() if t]
        return (set(tokens) == {"3"} and len(tokens) == 1, "")
    ans = _ask_until_correct(checker)
    if show_explanation:
        explain_q26()
    return ans

def answer_q27(show_explanation: bool = True):
    def checker(src):
        return (src.strip() == "1", "")
    ans = _ask_until_correct(checker)
    if show_explanation: explain_q27()
    return ans

def answer_q28(show_explanation: bool = True):
    def checker(src):
        return (src.strip() == "2", "")
    ans = _ask_until_correct(checker)
    if show_explanation: explain_q28()
    return ans

def answer_q29(show_explanation: bool = True):
    def checker(src):
        return (src.strip() == "N/A", "")
    ans = _ask_until_correct(checker)
    if show_explanation:
        explain_q29()
    return ans

def answer_q30(show_explanation: bool = True):
    def checker(src):
        return (src.strip() == "1", "")
    ans = _ask_until_correct(checker)
    if show_explanation: explain_q30()
    return ans

def answer_q31(show_explanation: bool = True):
    def checker(src):
        return (src.strip() == "4" or src.strip().lower() == "append", "")
    ans = _ask_until_correct(checker)
    if show_explanation:
        explain_q31()
    return ans

def answer_q32(show_explanation: bool = True):
    def checker(src):
        tokens = [t for t in src.replace(",", " ").split() if t]
        ok = set(tokens) == {"1", "2", "5"} and len(tokens) == 3
        return (ok, "")
    ans = _ask_until_correct(checker)
    if show_explanation: explain_q32()
    return ans

def answer_q33(show_explanation: bool = True):
    def checker(src):
        return (src.strip() == "4", "")
    ans = _ask_until_correct(checker)
    if show_explanation:
        explain_q33()
    return ans

def answer_q34(show_explanation: bool = True):
    def checker(src):
        return (src.strip() == "1", "")
    ans = _ask_until_correct(checker)
    if show_explanation:
        explain_q34()
    return ans

def answer_q35(show_explanation: bool = True):
    nums = [1, 2, 2, 3, 4, 4, 5]
    def checker(src):
        s = "".join(src.split())
        # 정확히 list(set(nums))만 정답으로 인정
        if s != "list(set(nums))":
            return (False, "")
        # 실행 검증(에러만 체크)
        try:
            _ = eval(src, {}, {"nums": nums})
        except Exception:
            return (False, "")
        return (True, "")
    ans = _ask_until_correct(checker)
    if show_explanation:
        explain_q35()
    return ans

# =========================
# 해설 함수 : explain_qN()
# =========================
def explain_q1():
    print("Q1 해설: 예약어(for, True 등)는 변수명으로 사용할 수 없습니다.")
    print("나머지 선택지는 변수 규칙에 부합합니다.")

def explain_q2():
    print("Q2 해설: int와 str를 +로 더하면 타입이 달라서 TypeError가 발생합니다.")
    print('예: 10 + "20" → Error')

def explain_q3():
    print("Q3 해설: 정수(int)와 실수(float)의 혼합 연산 결과는 float로 승격됩니다.")

def explain_q4():
    print("Q4 해설: 부동소수 표현 오차 때문에 0.1 + 0.2 == 0.3은 False가 됩니다.")

def explain_q5():
    print('Q5 해설: 문자열 결합은 + 연산자를 사용합니다.')
    print('a = "A", b = "B" 이므로 a + b의 결과는 "AB" 입니다.')

def explain_q6():
    print("Q6 해설: 문자열 리터럴은 따옴표로 감싼 값입니다.")
    print("따라서 '10'과 \"Hello\"만 문자열이며, 10은 숫자, True는 불리언입니다.")

def explain_q7():
    print("Q7 해설: 변수명은 숫자로 시작할 수 없습니다.")
    print("따라서 2value는 사용할 수 없습니다.")

def explain_q8():
    print("Q8 해설: True는 파이썬 예약어(키워드)로 변수명으로 사용할 수 없습니다.")
    print("print는 내장함수이지만 키워드는 아닙니다.")

def explain_q9():
    print('Q9 해설: print의 기본 구분자 sep는 공백입니다.')
    print('print("A", "B")는 A와 B 사이에 공백이 들어가므로 A B가 출력됩니다.')

def explain_q10():
    print("Q10 해설: 여러 값을 출력할 때 값 사이 구분자를 지정하는 파라미터는 sep 입니다.")
    print('예: print("A","B", sep="-") → A-B')

def explain_q11():
    print("Q11 해설:")
    print("문자열로 된 숫자를 정수로 변환할 때는 int()를 사용합니다.")
    print("s = '10' 이므로 int(s) 는 10을 반환합니다.")


def explain_q12():
    print("Q12 해설: type(10)은 int, type(10.0)은 float이므로 두 타입은 다릅니다.")
    print("따라서 type(10) == type(10.0)은 False 입니다.")

def explain_q13():
    print("a=2, b=3 에서 a ** b 는 2의 3제곱으로 8입니다.")
    print("+: 5, *: 6, **: 8, <<: 16 이므로 정답은 3) ** 입니다.")

def explain_q14():
    print("슬라이싱 s[:3]은 시작부터 인덱스 3 직전까지입니다. 'Pyt'가 됩니다.")

def explain_q15():
    print('replace(old, new, count)는 왼쪽부터 count회만 치환합니다.')
    print('"aaaaab"에서 "a"를 "b"로 3회 치환 → "bbbaab"')

def explain_q16():
    print("Q16 해설:")
    print("- 문자열은 불변(immutable)하므로 직접 수정할 수 없습니다.")
    print("- 10 + 10.0 → 정수 + 실수 → 결과 타입은 float 입니다.")
    print("- append()는 리스트 전용 메서드로 문자열에는 사용할 수 없습니다.")


def explain_q17():
    print("Q17 해설:")
    print("a//c = 4, b%c = 1, d = 3.0, 2**c = 4")
    print("→ (4 + 1) - 3 + 4 = 6.0")

def explain_q18():
    print("Q18 해설:")
    print("1), 2), 3)은 모두 동일한 문자열 'Jeju는 연간 15200000명이 방문합니다.' 를 출력합니다.")
    print("4)는 print에 여러 인자를 콤마로 전달해 토큰 사이에 공백이 추가되어 'Jeju 는 연간 15200000 명이 방문합니다.'처럼 다르게 출력됩니다.")

def explain_q19():
    print("Q19 해설:")
    print("float(str(3.14)) → '3.14' → 3.14 로 복원 가능.")
    print("하지만 bool, dict, list 등은 문자열화 후 원래 타입으로 직접 복원이 불가합니다.")


def explain_q20():
    print("Q20 해설:")
    print("기본형(primitive type)은 int, float, bool, str 입니다.")
    print("set은 집합형 자료로 복합 자료형에 해당하므로 기본형이 아닙니다.")


def explain_q21():
    print("Q21 해설:")
    print("int('12.0') 은 ValueError 발생 → 정수형 변환은 소수 문자열을 처리할 수 없습니다.")
    print("float('12.0') 은 정상 변환됩니다.")

def explain_q22():
    print("Q22 해설:")
    print("1), 3), 4)는 모두 'PY'를 출력합니다.")
    print("2)는 문자열끼리 뺄셈 연산을 시도하여 TypeError가 발생하므로 다른 결과입니다.")
    
def explain_q23():
    print("슬라이스 치환은 끝 인덱스를 포함하지 않습니다.")
    print("a[1:4] 구간(1,2,3)을 [9,9]로 바꿔서 [0,9,9,4]가 됩니다.")

def explain_q24():
    print("A.union(B) = {1,2,3,4}, C = {4,5,6} 이므로 (A∪B)−C = {1,2,3} 입니다.")

def explain_q25():
    print("딕셔너리 키는 해시 가능해야 합니다.")
    print("리스트/딕셔너리/집합은 불가, 튜플/문자열은 가능하므로 (1,2)와 'key'가 정답입니다.")

def explain_q26():
    print("최종 person은 {'name':'James','age':30,'job':'Engineer'} 입니다.")
    print("1) keys에 'city'는 존재하지 않습니다(이미 삭제).")
    print("2) values에 'N/A' 같은 값은 없습니다.")
    print("3) items는 ('name','James'), ('age',30), ('job','Engineer') 가 맞습니다. ← 정답")
    print("4) print(person)은 값 변경이지 이력 누적이 아니므로 ['Alice','James']처럼 출력되지 않습니다.")

def explain_q27():
    print("튜플은 불변이지만 내부에 있는 리스트의 내용 변경은 가능합니다.")
    print("t=(1,[2,3]); t[1].append(4) → (1,[2,3,4]) 입니다.")

def explain_q28():
    print("range(2,8,2)는 2부터 시작해 8 직전까지 2씩 증가합니다.")
    print("따라서 [2,4,6] 입니다.")

def explain_q29():
    print("d.get('z', 'N/A') 는 키가 없을 때 기본값을 반환합니다.")
    print("print(...) 의 실제 출력에는 따옴표가 포함되지 않습니다. → N/A")

def explain_q30():
    print("집합은 중복을 제거합니다.")
    print("s={1,2,2,3} → {1,2,3} 이므로 길이는 3입니다.")

def explain_q31():
    print("append는 리스트 메서드이며, set에는 사용할 수 없습니다.")
    print("set에는 add, remove, discard 등이 제공됩니다.")

def explain_q32():
    print("get은 기본값을 줄 수 있고, 키는 해시 가능해야 하며, update는 기존 값을 바꿀 수 있습니다.")
    print("따라서 1, 2, 5가 옳고, 빈 딕셔너리는 {} 이며 리스트는 키로 사용할 수 없습니다.")

def explain_q33():
    print("Q33 해설:")
    print("컬렉션 형(여러 요소를 담는 자료형) 예시: 리스트[], 튜플(), 딕셔너리{키:값}.")
    print("42는 정수(int)로 컬렉션이 아니므로 정답은 4) 입니다.")

def explain_q34():
    print("Q34 해설:")
    print("tensor[0:2] → [[1,2,3,4], [5,6,7,8]] (첫 두 행)")
    print("[...][1]   → [5,6,7,8] (그 중 두 번째 행)")
    print("[...][1:3] → [6,7] (인덱스 1부터 3 직전까지)")

def explain_q35():
    print("Q35 해설:")
    print("중복 제거는 set으로 하고, 리스트 형태로 출력하기 위해 list로 감쌉니다.")
    print("정답 형태: list(set(nums))")


def show_all_explanations(show_answer=True):
    for i in range(1, 11):
        print(f"\n### Q{i}")
        if show_answer:
            print("정답:", _answer_key()[i])
        _explain_func_map()[i]()
    print("\n✅ 모든 해설 출력 완료")

# ...기존 키 유지, 29번만 교체
def _answer_key():
    return {
        1: "4",
        2: "4",
        3: "2",
        4: "2",
        5: "a.lower() + b",
        6: "1 2",
        7: "3",
        8: "2",
        9: "1",
        10: "1",
        11: "int",
        12: "2",
        13: "3",
        14: "Pyt",
        15: "bbbaab",
        16: "2",
        17: "6.0",
        18: "4",
        19: "2",
        20: "1",
        21: "3",
        22: "hi",
        23: "1",
        24: "1",
        25: "2 4",
        26: "3",
        27: "1",
        28: "2",
        29: "N/A",
        30: "1",
        31: "4",
        32: "1 2 5",
        33: "4",
        34: "1",
        35: "list(set(nums))",
    }


def _explain_func_map():
    m = {}
    for i in range(1, 36):  # Q1 ~ Q35
        fn = globals().get(f"explain_q{i}")
        if callable(fn):
            m[i] = fn
    return m

def show_all():
    # Q1 ~ Q35 전체 프리뷰
    for i in range(1, 36):
        fn = globals().get(f"show_q{i}")
        if callable(fn):
            fn()
    try:
        display(Markdown("모든 문제 프리뷰가 표시되었습니다."))
    except NameError:
        print("모든 문제 프리뷰가 표시되었습니다.")


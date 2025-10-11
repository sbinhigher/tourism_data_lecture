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
# Week4 과제: 컬렉션형 (Q1~Q10)
# =========================
# --- Q1 ---
def show_q1():
    _panel(
        "Q1",
        "다음 중 변수(Variable)에 대한 설명으로 틀린 것은?\n보기\n1) 변수명에는 알파벳, 숫자, 밑줄(_), 한글 등을 사용할 수 있다\n2) 변수명은 숫자로 시작할 수 없다\n3) 공백이나 특수문자는 변수명으로 사용할 수 없다\n4) for나 True 같은 예약어도 변수명으로 사용할 수 있다\n5) 여러 변수를 동시에 할당할 수 있다",
    )
def answer_q1(show_explanation: bool = True):
    def checker(src):
        return (src.strip() == "4", "")
    ans = _ask_until_correct(checker)
    if show_explanation: explain_q1()
    return ans
def explain_q1(): pass

# --- Q2 ---
def show_q2():
    _panel(
        "Q2",
        "다음 코드를 실행했을 때, 결과는?\nprint(10+\"20\")\n보기\n1) 30\n2) \"1020\"\n3) 1020\n4) Error 발생",
    )
def answer_q2(show_explanation: bool = True):
    def checker(src):
        return (src.strip() == "4", "")
    ans = _ask_until_correct(checker)
    if show_explanation: explain_q2()
    return ans
def explain_q2(): pass

# --- Q3 ---
def show_q3():
    _panel(
        "Q3",
        "다음 중 정수와 실수의 덧셈 결과 타입으로 옳은 것은?\n보기\n1) int\n2) float\n3) str\n4) bool",
    )
def answer_q3(show_explanation: bool = True):
    def checker(src):
        return (src.strip() == "2", "")
    ans = _ask_until_correct(checker)
    if show_explanation: explain_q3()
    return ans
def explain_q3(): pass

# --- Q4 ---
def show_q4():
    _panel(
        "Q4",
        "다음 표현식의 결과로 옳은 것은?\n0.1 + 0.2 == 0.3\n보기\n1) True\n2) False",
    )
def answer_q4(show_explanation: bool = True):
    def checker(src):
        return (src.strip() == "2", "")
    ans = _ask_until_correct(checker)
    if show_explanation: explain_q4()
    return ans
def explain_q4(): pass

# --- Q5 ---
def show_q5():
    _panel(
        "Q5",
        "아래 코드를 실행했을 때, 출력이 \"AB\"가 되도록 ?에 들어갈 구문을 작성하시오.",
        code='a = "A"\nb = "B"\nprint(?)\n-----\nAB',
    )
def answer_q5(show_explanation: bool = True):
    a = "A"
    b = "B"
    def checker(src):
        try:
            expr = src
            result = eval(expr, {}, {"a": a, "b": b})
        except Exception:
            return (False, "")
        return (result == "AB", "")
    ans = _ask_until_correct(checker)
    if show_explanation: explain_q5()
    return ans
def explain_q5(): pass

# --- Q6 ---
def show_q6():
    _panel(
        "Q6",
        "다음 중 문자열 리터럴로 올바른 것은 모두 고르시오.\n보기\n1) '10'\n2) \"Hello\"\n3) 10\n4) True",
    )
def answer_q6(show_explanation: bool = True):
    def checker(src):
        tokens = [t for t in src.replace(",", " ").split() if t]
        ok = set(tokens) == {"1", "2"} and len(tokens) == 2
        return (ok, "")
    ans = _ask_until_correct(checker)
    if show_explanation: explain_q6()
    return ans
def explain_q6(): pass

# --- Q7 ---
def show_q7():
    _panel(
        "Q7",
        "다음 중 변수명으로 사용할 수 없는 것은?\n보기\n1) _score\n2) value2\n3) 2value\n4) 변수",
    )
def answer_q7(show_explanation: bool = True):
    def checker(src):
        return (src.strip() == "3", "")
    ans = _ask_until_correct(checker)
    if show_explanation: explain_q7()
    return ans
def explain_q7(): pass

# --- Q8 ---
def show_q8():
    _panel(
        "Q8",
        "다음 중 예약어(변수명으로 사용 불가)에 해당하는 것은?\n보기\n1) print\n2) True\n3) number\n4) hello",
    )
def answer_q8(show_explanation: bool = True):
    def checker(src):
        return (src.strip() == "2", "")
    ans = _ask_until_correct(checker)
    if show_explanation: explain_q8()
    return ans
def explain_q8(): pass

# --- Q9 ---
def show_q9():
    _panel(
        "Q9",
        "다음 코드의 출력 결과로 옳은 것은?\nprint(\"A\", \"B\")\n보기\n1) A B\n2) AB\n3) \"A B\"\n4) A, B",
    )
def answer_q9(show_explanation: bool = True):
    def checker(src):
        return (src.strip() == "1", "")
    ans = _ask_until_correct(checker)
    if show_explanation: explain_q9()
    return ans
def explain_q9(): pass

# --- Q10 ---
def show_q10():
    _panel(
        "Q10",
        "다음 중 print에서 여러 값을 출력할 때 값 사이에 들어갈 구분자를 지정하는 파라미터 이름은?\n보기\n1) sep\n2) end\n3) seq\n4) delimiter\n5) split",
    )
def answer_q10(show_explanation: bool = True):
    def checker(src):
        return (src.strip() == "1", "")
    ans = _ask_until_correct(checker)
    if show_explanation: explain_q10()
    return ans
def explain_q10(): pass

# --- Q11 ---
def show_q11():
    _panel(
        "Q11",
        "아래 한 줄을 완성하여, 문자열 \"10\"을 정수 10으로 변환하시오.",
        code="__________(\"10\")",
    )
def answer_q11(show_explanation: bool = True):
    def checker(src):
        s = src.strip()
        try:
            result = eval(f"{s}('10')", {}, {})
        except Exception:
            return (False, "")
        return (result == 10, "")
    ans = _ask_until_correct(checker)
    if show_explanation: explain_q11()
    return ans
def explain_q11(): pass

# --- Q12 ---
def show_q12():
    _panel(
        "Q12",
        "다음 표현식의 결과로 옳은 것은?\ntype(10) == type(10.0)\n보기\n1) True\n2) False",
    )
def answer_q12(show_explanation: bool = True):
    def checker(src):
        return (src.strip() == "2", "")
    ans = _ask_until_correct(checker)
    if show_explanation: explain_q12()
    return ans
def explain_q12(): pass

# =========================
# 해설 함수 (생략하지 않고 그대로)
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
    print('Q11 해설: 문자열 "10"을 정수 10으로 변환하려면 int 함수를 사용합니다.')
    print('예: int("10") → 10')

def explain_q12():
    print("Q12 해설: type(10)은 int, type(10.0)은 float이므로 두 타입은 다릅니다.")
    print("따라서 type(10) == type(10.0)은 False 입니다.")


def show_all_explanations(show_answer=True):
    for i in range(1, 11):
        print(f"\n### Q{i}")
        if show_answer:
            print("정답:", _answer_key()[i])
        _explain_func_map()[i]()
    print("\n✅ 모든 해설 출력 완료")

def _answer_key():
    return {
        1: "4",
        2: "4",
        3: "2",
        4: "2",
        5: "a + b",
        6: "1 2",
        7: "3",
        8: "2",
        9: "1",
        10: "1",
        11: "int",
        12: "2",
    }


def _explain_func_map():
    return {1:explain_q1,2:explain_q2,3:explain_q3,4:explain_q4,5:explain_q5,6:explain_q6,7:explain_q7,8:explain_q8,9:explain_q9,10:explain_q10}

def show_all():
    show_q1(); show_q2(); show_q3(); show_q4()
    show_q5(); show_q6(); show_q7()
    show_q8(); show_q9(); show_q10()
    show_q11; show_q12()
    display(Markdown("> 모든 문제 프리뷰가 표시되었습니다."))

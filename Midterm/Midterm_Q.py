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
    _panel("Q11", "아래 한 줄을 완성하여, 문자열 \"10\"을 정수 10으로 변환하시오.",
           code='__________("10")')

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
        "다음 코드를 실행했을 때, 출력 값을 정확히 쓰시오.",
        code='s = "Python"\nprint(s[0])'
    )

def show_q14():
    _panel(
        "Q14",
        "다음 코드를 실행했을 때, 출력 값을 정확히 쓰시오.",
        code='s = "Python"\nprint(s[:3])'
    )

def show_q15():
    _panel(
        "Q15",
        "다음 표현식의 계산 결과로 옳은 것을 고르시오."
    )
    display(Markdown(
        "보기\n\n"
        "1) 11\n\n"
        "2) 12\n\n"
        "3) 9\n\n"
        "4) 10"
    ))
    display(Markdown("식\n\n3 + 5*2 - 4/2"))

def show_q16():
    _panel(
        "Q16",
        "문자열 \"3.14\"를 실수 3.14로 변환하도록, 빈칸에 들어갈 함수를 한 단어로 쓰시오.",
        code='print(______("3.14"))'
    )

def show_q17():
    _panel(
        "Q17",
        "다음 코드의 평가 결과로 옳은 것을 고르시오.",
        code='"10".isdigit()'
    )
    display(Markdown(
        "보기\n\n"
        "1) True\n\n"
        "2) False"
    ))

def show_q18():
    _panel(
        "Q18",
        "다음 코드를 실행했을 때, 출력 값을 정확히 쓰시오.",
        code='print("aaaa".replace("a", "b", 2))'
    )

def show_q19():
    _panel(
        "Q19",
        "다음 코드를 실행했을 때, 출력 값을 정확히 쓰시오.",
        code='print("abcde"[::-1])'
    )

def show_q20():
    _panel(
        "Q20",
        "다음 코드의 평가 결과로 옳은 것을 고르시오.",
        code='"Python".find("th")'
    )
    display(Markdown(
        "보기\n\n"
        "1) 0\n\n"
        "2) 1\n\n"
        "3) 2\n\n"
        "4) -1"
    ))

def show_q21():
    _panel(
        "Q21",
        "다음 코드의 평가 결과로 옳은 것을 고르시오.",
        code='int(float("10.0")) == 10'
    )
    display(Markdown(
        "보기\n\n"
        "1) True\n\n"
        "2) False"
    ))

def show_q22():
    _panel(
        "Q22",
        "다음 코드를 실행했을 때, 출력 값을 정확히 쓰시오.",
        code='print("  hi  ".strip())'
    )

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
        "집합 A={1,2,3}, B={3,4} 일 때 A ^ B 의 결과로 옳은 것을 고르시오."
    )
    display(Markdown(
        "보기\n\n"
        "1) {3}\n\n"
        "2) {1,2,4}\n\n"
        "3) {1,2,3,4}\n\n"
        "4) {1,2}"
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
        "다음 코드를 실행했을 때, 출력 값을 정확히 쓰시오.",
        code="x = {'a':1, 'b':2}\nx.update({'b':5, 'c':9})\nprint(x)"
    )

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
        "다음 중 집합 s = {1,2,2,3} 의 길이로 옳은 것을 고르시오."
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
        "아래 코드를 실행했을 때, student 딕셔너리에 email 키를 추가하도록 ?에 들어갈 한 줄을 작성하시오.",
        code="student = {'name':'Kim', 'id':1001}\n?\nprint('email' in student)"
    )

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

def answer_q12(show_explanation: bool = True):
    def checker(src):
        return (src.strip() == "2", "")
    ans = _ask_until_correct(checker)
    if show_explanation: explain_q12()
    return ans

def answer_q13(show_explanation: bool = True):
    # 예상 맥락: s = "Python" 에서 s[0]의 값
    def checker(src):
        val = src.strip().strip('"').strip("'")
        return (val == "P", "")
    ans = _ask_until_correct(checker)
    if show_explanation: explain_q13()
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
    # 예상 맥락: 3 + 5*2 - 4/2 의 결과
    def checker(src):
        s = src.strip()
        try:
            n = float(s) if "." in s else int(s)
        except Exception:
            return (False, "")
        return (n == 11, "")
    ans = _ask_until_correct(checker)
    if show_explanation: explain_q15()
    return ans

def answer_q16(show_explanation: bool = True):
    # 예상 맥락: 문자열 "3.14"를 실수로 변환하는 함수 이름
    def checker(src):
        s = "".join(src.split()).lower()
        try:
            ok = (eval(f"{s}('3.14')", {}, {}) == 3.14)
        except Exception:
            return (False, "")
        return (ok, "")
    ans = _ask_until_correct(checker)
    if show_explanation: explain_q16()
    return ans

def answer_q17(show_explanation: bool = True):
    # 예상 맥락: "10".isdigit() 평가 결과
    def checker(src):
        s = src.strip().lower()
        return (s in ("true", "t"), "")
    ans = _ask_until_correct(checker)
    if show_explanation: explain_q17()
    return ans

def answer_q18(show_explanation: bool = True):
    # 예상 맥락: "aaaa".replace("a","b",2) 의 결과
    def checker(src):
        val = src.strip().strip('"').strip("'")
        return (val == "bbaa", "")
    ans = _ask_until_correct(checker)
    if show_explanation: explain_q18()
    return ans

def answer_q19(show_explanation: bool = True):
    # 예상 맥락: "abcde"[::-1] 의 결과
    def checker(src):
        val = src.strip().strip('"').strip("'")
        return (val == "edcba", "")
    ans = _ask_until_correct(checker)
    if show_explanation: explain_q19()
    return ans

def answer_q20(show_explanation: bool = True):
    # 예상 맥락: "Python".find("th") 의 결과
    def checker(src):
        s = src.strip()
        try:
            n = int(s)
        except Exception:
            return (False, "")
        return (n == 2, "")
    ans = _ask_until_correct(checker)
    if show_explanation: explain_q20()
    return ans

def answer_q21(show_explanation: bool = True):
    # 예상 맥락: int(float("10.0")) == 10 의 평가 결과
    def checker(src):
        s = src.strip().lower()
        return (s in ("true", "t"), "")
    ans = _ask_until_correct(checker)
    if show_explanation: explain_q21()
    return ans

def answer_q22(show_explanation: bool = True):
    # 예상 맥락: "  hi  ".strip() 의 결과
    def checker(src):
        val = src.strip().strip('"').strip("'")
        return (val == "hi", "")
    ans = _ask_until_correct(checker)
    if show_explanation: explain_q22()
    return ans

def answer_q23(show_explanation: bool = True):
    def checker(src):
        return (src.strip() == "1", "")
    ans = _ask_until_correct(checker)
    if show_explanation: explain_q23()
    return ans

def answer_q24(show_explanation: bool = True):
    def checker(src):
        return (src.strip() == "2", "")
    ans = _ask_until_correct(checker)
    if show_explanation: explain_q24()
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
        expect = "{'a': 1, 'b': 5, 'c': 9}"
        return (src.strip() == expect, "")
    ans = _ask_until_correct(checker)
    if show_explanation: explain_q26()
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
        return (src.strip() == "'N/A'", "")
    ans = _ask_until_correct(checker)
    if show_explanation: explain_q29()
    return ans

def answer_q30(show_explanation: bool = True):
    def checker(src):
        return (src.strip() == "1", "")
    ans = _ask_until_correct(checker)
    if show_explanation: explain_q30()
    return ans

def answer_q31(show_explanation: bool = True):
    def checker(src):
        student = {'name':'Kim', 'id':1001}
        try:
            exec(src, {}, {"student": student})
        except Exception:
            return (False, "")
        return ('email' in student, "")
    ans = _ask_until_correct(checker)
    if show_explanation: explain_q31()
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
        expect = "[0, 9, 3, 7] [0, 9, 3, 7]"
        return (src.strip() == expect, "")
    ans = _ask_until_correct(checker)
    if show_explanation: explain_q33()
    return ans

def answer_q34(show_explanation: bool = True):
    def checker(src):
        return (src.strip() == "2", "")
    ans = _ask_until_correct(checker)
    if show_explanation: explain_q34()
    return ans

def answer_q35(show_explanation: bool = True):
    def checker(src):
        return (src.strip() == "1", "")
    ans = _ask_until_correct(checker)
    if show_explanation: explain_q35()
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
    print('Q11 해설: 문자열 "10"을 정수 10으로 변환하려면 int 함수를 사용합니다.')
    print('예: int("10") → 10')

def explain_q12():
    print("Q12 해설: type(10)은 int, type(10.0)은 float이므로 두 타입은 다릅니다.")
    print("따라서 type(10) == type(10.0)은 False 입니다.")

def explain_q13():
    print("문자열 인덱싱에서 s[0]은 첫 글자입니다. s = 'Python' 이므로 결과는 'P'입니다.")

def explain_q14():
    print("슬라이싱 s[:3]은 시작부터 인덱스 3 직전까지입니다. 'Pyt'가 됩니다.")

def explain_q15():
    print("연산자 우선순위에 따라 5*2=10, 4/2=2.0 이고 3+10-2.0=11.0 입니다. 결과는 11에 해당합니다.")

def explain_q16():
    print("문자열 '3.14'를 실수로 바꾸는 함수는 float 입니다. float('3.14') → 3.14")

def explain_q17():
    print("문자열 '10'은 숫자 문자만으로 구성되어 isdigit()이 True입니다.")

def explain_q18():
    print("replace(old,new,count)에서 count=2이면 앞에서부터 두 번만 치환합니다. 'aaaa'→'bbaa'입니다.")

def explain_q19():
    print("슬라이싱 [::-1]은 역순입니다. 'abcde'→'edcba'입니다.")

def explain_q20():
    print("find는 부분 문자열의 첫 시작 인덱스를 반환합니다. 'Python'에서 'th'는 인덱스 2부터 시작합니다.")

def explain_q21():
    print("float('10.0')은 10.0, int(10.0)은 10이므로 비교 결과는 True입니다.")

def explain_q22():
    print("strip()은 양쪽 공백 제거입니다. '  hi  '→'hi'가 됩니다.")

def explain_q23():
    print("슬라이스 치환은 끝 인덱스를 포함하지 않습니다.")
    print("a[1:4] 구간(1,2,3)을 [9,9]로 바꿔서 [0,9,9,4]가 됩니다.")

def explain_q24():
    print("대칭차 A ^ B 는 공통 원소를 제외한 합집합입니다.")
    print("A={1,2,3}, B={3,4} → {1,2,4} 입니다.")

def explain_q25():
    print("딕셔너리 키는 해시 가능해야 합니다.")
    print("리스트/딕셔너리/집합은 불가, 튜플/문자열은 가능하므로 (1,2)와 'key'가 정답입니다.")

def explain_q26():
    print("update는 기존 키를 갱신하고 새로운 키를 추가합니다.")
    print("{'a':1,'b':2} 에서 b→5로 바뀌고 c:9가 추가되어 {'a':1,'b':5,'c':9}가 됩니다.")

def explain_q27():
    print("튜플은 불변이지만 내부에 있는 리스트의 내용 변경은 가능합니다.")
    print("t=(1,[2,3]); t[1].append(4) → (1,[2,3,4]) 입니다.")

def explain_q28():
    print("range(2,8,2)는 2부터 시작해 8 직전까지 2씩 증가합니다.")
    print("따라서 [2,4,6] 입니다.")

def explain_q29():
    print("get('z','N/A')는 키가 없으면 기본값을 반환합니다.")
    print("z가 없으므로 'N/A'가 출력됩니다.")

def explain_q30():
    print("집합은 중복을 제거합니다.")
    print("s={1,2,2,3} → {1,2,3} 이므로 길이는 3입니다.")

def explain_q31():
    print("딕셔너리에 키를 추가하려면 대괄호 대입을 사용합니다.")
    print("student['email']='...' 과 같이 넣으면 'email' in student 가 True가 됩니다.")

def explain_q32():
    print("get은 기본값을 줄 수 있고, 키는 해시 가능해야 하며, update는 기존 값을 바꿀 수 있습니다.")
    print("따라서 1, 2, 5가 옳고, 빈 딕셔너리는 {} 이며 리스트는 키로 사용할 수 없습니다.")

def explain_q33():
    print("a와 b는 같은 리스트를 참조합니다.")
    print("a[1:3]=[9]로 [0,9,3]이 되고 b.append(7)로 둘 다 [0,9,3,7]이 됩니다.")

def explain_q34():
    print("a[2:2]=[...] 는 삽입입니다(치환 아님).")
    print("[8,9]가 인덱스 2 위치에 끼어들어 [0,1,8,9,2,3]이 됩니다.")

def explain_q35():
    print("딕셔너리의 in 연산은 키 존재 여부를 검사합니다.")
    print("'id'는 키로 존재하므로 결과는 True 입니다.")



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
        5: "a.lower() + b",
        6: "1 2",
        7: "3",
        8: "2",
        9: "1",
        10: "1",
        11: "int",
        12: "2",
        13: "P",
        14: "Pyt",
        15: "1",
        16: "float",
        17: "1",
        18: "bbaa",
        19: "edcba",
        20: "3",
        21: "1",
        22: "hi",
        23: "1",
        24: "2",
        25: "2 4",
        26: "{'a': 1, 'b': 5, 'c': 9}",
        27: "1",
        28: "2",
        29: "'N/A'",
        30: "1",
        31: "student['email']='...'",
        32: "1 2 5",
        33: "[0, 9, 3, 7] [0, 9, 3, 7]",
        34: "2",
        35: "1",
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


# -*- coding: utf-8 -*-
# Midterm_Q.py : 중간시험(Week2~Week4) — 20문항(쉬움 13, 중간 5, 어려움 2)
# Week4_Q.py의 구조/포맷을 참조하되, 독립적으로 동작하도록 구현함.
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
             padding:14px 16px;margin:10px 0;background:#fafbff;}
.quiz-title {margin-bottom:6px;font-size:1.05rem;}
.quiz-body  {line-height:1.6;white-space:pre-wrap;}
.quiz-code  {background:#111827;color:#e5e7eb;padding:10px 12px;border-radius:8px;overflow:auto;margin-top:10px;font-size:0.95rem;}
</style>
"""

_css_injected = False
def _ensure_css():
    global _css_injected
    if not _css_injected:
        display(HTML(PANEL_CSS))
        _css_injected = True

def _panel(title, body, code=None):
    _ensure_css()
    html = []
    html.append("<div class='quiz-panel'>")
    html.append(f"<div class='quiz-title'>{title}</div>")
    html.append(f"<div class='quiz-body'>{body}</div>")
    if code is not None:
        html.append(f"<pre class='quiz-code'>{code}</pre>")
    html.append("</div>")
    display(HTML("".join(html)))

# ====== 입력 체크 유틸 ======
def _norm_token(s: str):
    return " ".join(s.strip().lower().replace('`','').replace('"',"'").split())

def _one_of(ans: str, accepted):
    a = _norm_token(ans)
    return any(a == _norm_token(x) for x in accepted)

def _ask_until_correct(checker, prompt="> "):
    while True:
        ans = input(prompt)
        ok, _msg = checker(ans)
        if ok:
            print(f"{CORRECT_ICON} 정답입니다!\n")
            return ans
        else:
            print(f"{WRONG_ICON} 오답입니다. 다시 시도하세요.\n")

# =========================
# 문항 정의: show_qN / answer_qN / explain_qN (해설은 모듈 내 보관, 시험 중 사용 안 함)
# =========================

# ------ 쉬움 13 ------
def show_q1():
    _panel("Q1) 객관식: 불린 리터럴",
           "다음 중 파이썬에서 불린 참을 나타내는 리터럴을 고르시오.\nA) true  B) True  C) 'True'  D) 1")

def answer_q1(show_explanation: bool = False):
    return _ask_until_correct(lambda a: (a.strip() == 'B', ""))

def explain_q1():
    return "파이썬 불린 리터럴은 True, False 이다."

def show_q2():
    _panel("Q2) 객관식: 타입 승격",
           "다음 표현식의 타입을 고르시오: type(10 + 10.0)\nA) int  B) float  C) str  D) bool")

def answer_q2(show_explanation: bool = False):
    return _ask_until_correct(lambda a: (a.strip() == 'B', ""))

def explain_q2():
    return "정수와 부동소수 합은 float로 승격된다."

def show_q3():
    _panel("Q3) 객관식: 대입 연산자",
           "다음 중 대입 연산을 나타내는 기호를 고르시오.\nA) ==  B) =  C) :=  D) ===")

def answer_q3(show_explanation: bool = False):
    return _ask_until_correct(lambda a: (a.strip() == 'B', ""))

def explain_q3():
    return "= 는 대입, == 는 동등 비교, := 는 할당식, === 는 없다."

def show_q4():
    _panel("Q4) 객관식: 부동소수점 비교",
           "표현식 0.1 + 0.2 == 0.3 의 평가 결과를 고르시오.\nA) True  B) False")

def answer_q4(show_explanation: bool = False):
    return _ask_until_correct(lambda a: (a.strip() == 'B', ""))

def explain_q4():
    return "부동소수 이진 표현 오차로 False가 된다."

def show_q5():
    _panel("Q5) 객관식: 불변 시퀀스",
           "다음 중 불변(immutable) 시퀀스를 고르시오.\nA) list  B) tuple  C) set  D) dict")

def answer_q5(show_explanation: bool = False):
    return _ask_until_correct(lambda a: (a.strip() == 'B', ""))

def explain_q5():
    return "tuple은 불변, list/dict는 가변, set은 집합."

def show_q6():
    _panel("Q6) 객관식: 슬라이싱",
           "문자열 s = 'Data' 에서 s[1:3] 의 값은 무엇인가?\nA) 'Da'  B) 'at'  C) 'ta'  D) 'dt'")

def answer_q6(show_explanation: bool = False):
    return _ask_until_correct(lambda a: (a.strip() in ('B', "at", "'at'", '"at"'), ""))

def explain_q6():
    return "슬라이싱은 시작 포함, 끝 미포함 → 'at'."

def show_q7():
    _panel("Q7) 객관식: 리스트 치환",
           "리스트 nums = [1,2,3]; nums[0] = 9 이후 nums는?\nA) [1,2,3]  B) [9,2,3]  C) [1,9,3]  D) 오류")

def answer_q7(show_explanation: bool = False):
    return _ask_until_correct(lambda a: (a.strip() == 'B', ""))

def explain_q7():
    return "리스트는 가변이므로 첫 원소가 9로 치환된다."

def show_q8():
    _panel("Q8) 객관식: 세트 길이",
           "세트 s = {1,2,2,3} 의 길이는?\nA) 3  B) 4  C) 2  D) 1")

def answer_q8(show_explanation: bool = False):
    return _ask_until_correct(lambda a: (a.strip() == 'A', ""))

def explain_q8():
    return "중복이 제거되어 {1,2,3}이므로 길이는 3."

def show_q9():
    _panel("Q9) 객관식: 딕셔너리 키",
           "d = {'a':1}; d['b']=2 수행 후 키 목록에 포함되지 않는 것은?\nA) a  B) b  C) c  D) 둘 다 포함")

def answer_q9(show_explanation: bool = False):
    return _ask_until_correct(lambda a: (a.strip() == 'C', ""))

def explain_q9():
    return "키는 'a','b'만 존재한다."

def show_q10():
    _panel("Q10) 객관식: range",
           "range(2,8,2) 를 리스트로 변환한 결과를 고르시오.\nA) [2,4,6,8]  B) [2,4,6]  C) [2,3,4,5,6,7]  D) [3,5,7]")

def answer_q10(show_explanation: bool = False):
    return _ask_until_correct(lambda a: (a.strip() == 'B', ""))

def explain_q10():
    return "끝은 포함되지 않으므로 2,4,6."

def show_q11():
    _panel("Q11) 객관식: 문자열→정수 변환",
           "문자열 '10'을 int로 안전 변환하려면 무엇을 사용하는가?\nA) int('10')  B) float('10')  C) str(10)  D) bool('10')")

def answer_q11(show_explanation: bool = False):
    return _ask_until_correct(lambda a: (a.strip() == 'A', ""))

def explain_q11():
    return "정수 문자열은 int()로 변환."

def show_q12():
    _panel("Q12) 객관식: 빈 set 생성",
           "다음 중 빈 세트를 만드는 올바른 방법은?\nA) {}  B) set()  C) []  D) empty_set()")

def answer_q12(show_explanation: bool = False):
    return _ask_until_correct(lambda a: (a.strip() == 'B', ""))

def explain_q12():
    return "{}는 빈 dict, set()이 빈 set."

def show_q13():
    _panel("Q13) 객관식: 슬라이스 치환 축소",
           "리스트 a = [0,1,2,3,4]; a[1:4] = [9,9] 이후 a는?\nA) [0,9,9,4]  B) [0,9,9,3,4]  C) [0,1,2,3,4]  D) 오류")

def answer_q13(show_explanation: bool = False):
    return _ask_until_correct(lambda a: (a.strip() == 'A', ""))

def explain_q13():
    return "슬라이스 치환은 길이가 달라도 가능하며 해당 구간이 축소된다."

# ------ 중간 5 ------
def show_q14():
    _panel("Q14) 객관식: 대칭차",
           "집합 A={1,2,3}, B={3,4} 일 때 A ^ B 의 결과를 고르시오.\nA) {3}  B) {1,2,4}  C) {1,2,3,4}  D) {1,2}")

def answer_q14(show_explanation: bool = False):
    return _ask_until_correct(lambda a: (a.strip() == 'B', ""))

def explain_q14():
    return "대칭차: 공통 원소를 제외한 합집합, {1,2,4}."

def show_q15():
    _panel("Q15) 주관식: dict 업데이트 결과",
           "다음 코드 실행 후 x의 값을 정확히 쓰시오.",
           code="x = {'a':1, 'b':2}\nx.update({'b':5, 'c':9})\nx.get('d', -1)\nprint(x)")

def answer_q15(show_explanation: bool = False):
    expect = "{'a': 1, 'b': 5, 'c': 9}"
    return _ask_until_correct(lambda a: (a.strip() == expect, ""))

def explain_q15():
    return "update로 b가 5로 바뀌고 c가 추가. get은 조회만 하며 x를 바꾸지 않는다."

def show_q16():
    _panel("Q16) 객관식: 튜플과 가변 내부",
           "튜플 t=(1,[2,3]); t[1].append(4) 이후 t의 값은?\nA) (1,[2,3,4])  B) (1,[2,3])  C) 오류  D) (1,(2,3,4))")

def answer_q16(show_explanation: bool = False):
    return _ask_until_correct(lambda a: (a.strip() == 'A', ""))

def explain_q16():
    return "튜플은 불변이지만 내부 가변 객체의 내용 변경은 가능."

def show_q17():
    _panel("Q17) 객관식: 음수 인덱스 슬라이싱",
           "문자열 s='abcdefg'에서 s[-6:-1:2]의 결과를 고르시오.\nA) 'bdf'  B) 'bde'  C) 'ace'  D) 'bdfg'")

def answer_q17(show_explanation: bool = False):
    return _ask_until_correct(lambda a: (a.strip() == 'A', ""))

def explain_q17():
    return "인덱스 -6..-1(미포함), step 2 → b,d,f."

def show_q18():
    _panel("Q18) 객관식: dict 키로 가능한 것",
           "다음 중 dict 키로 유효한 것은 모두 고르시오.\nA) [1,2]  B) (1,2)  C) {'a':1}  D) 'key'")

def answer_q18(show_explanation: bool = False):
    ok = lambda s: _one_of(s, ['B D','D B','B, D',"(1,2) and 'key'","(1,2) and \"key\""])
    return _ask_until_correct(lambda a: (ok(a), ""))

def explain_q18():
    return "키는 해시가능해야 하므로 불변형(예: 튜플, 문자열)은 가능. 리스트, dict는 불가."

# ------ 어려움 2 ------
def show_q19():
    _panel("Q19) 주관식: 참조 공유와 슬라이스 치환",
           "다음 코드 실행 결과를 정확히 쓰시오.",
           code="a = [0,1,2,3]\nb = a\na[1:3] = [9]\nb.append(7)\nprint(a, b)")

def answer_q19(show_explanation: bool = False):
    expect = "[0, 9, 3, 7] [0, 9, 3, 7]"
    return _ask_until_correct(lambda a: (a.strip() == expect, ""))

def explain_q19():
    return "a와 b는 같은 리스트를 참조. 슬라이스 치환 후 append로 동일 결과."

def show_q20():
    _panel("Q20) 주관식: 집합 조건",
           "집합 연산에서 다음을 만족하는 모든 x를 공백으로 구분해 쓰시오.\n조건: A={1,2,3,4}, B={2,4,6}, x ∈ A 이고 x not in (A & B)")

def answer_q20(show_explanation: bool = False):
    ok = lambda s: _one_of(s, ['1 3','3 1'])
    return _ask_until_correct(lambda a: (ok(a), ""))

def explain_q20():
    return "A∩B={2,4}. A에서 이를 제외하면 {1,3}."

# ------ 편의 함수 ------
def _answer_map():
    return {
        1:'B',2:'B',3:'B',4:'B',5:'B',6:'B',7:'B',8:'A',9:'C',10:'B',
        11:'A',12:'B',13:'A',14:'B',15:"{'a': 1, 'b': 5, 'c': 9}",
        16:'A',17:'A',18:'B D',19:"[0, 9, 3, 7] [0, 9, 3, 7]",20:'1 3'
    }

def _explain_map():
    return {
        1:explain_q1,2:explain_q2,3:explain_q3,4:explain_q4,5:explain_q5,
        6:explain_q6,7:explain_q7,8:explain_q8,9:explain_q9,10:explain_q10,
        11:explain_q11,12:explain_q12,13:explain_q13,14:explain_q14,15:explain_q15,
        16:explain_q16,17:explain_q17,18:explain_q18,19:explain_q19,20:explain_q20
    }

def show_all():
    for i in range(1,21):
        globals()[f"show_q{i}"]()

def answers():
    return _answer_map()

def explanations(qnum=None):
    if qnum is None:
        return {k: v() for k,v in _explain_map().items()}
    return _explain_map()[qnum]()

if __name__ == "__main__":
    show_all()
    print("정답 맵:", answers())

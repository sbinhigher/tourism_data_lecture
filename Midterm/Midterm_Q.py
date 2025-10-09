# -*- coding: utf-8 -*-
# Midterm_Q.py : 중간시험(Week2~Week4) — 20문항(쉬움 13, 중간 5, 어려움 2)
from IPython.display import display, HTML, Markdown
import io
import contextlib

# ====== 글로벌 아이콘 ======
CORRECT_ICON = "✅"
WRONG_ICON   = "❌"

def set_icons(correct="✅", wrong="❌"):
    global CORRECT_ICON, WRONG_ICON
    CORRECT_ICON, WRONG_ICON = correct, wrong

# ====== 프리뷰 패널 공통 렌더러 (Week4_Q.py 호환 경량 버전) ======
def _panel(title, body, code=None):
    html = []
    html.append(f"<div class='quiz-panel' style='border:1px solid #e5e7eb;border-left:6px solid #3b82f6;border-radius:10px;padding:14px 16px;margin:10px 0;background:#fafbff;'>")
    html.append(f"<div class='quiz-title' style='font-weight:700;color:#1f2937;margin-bottom:6px;font-size:1.05rem;'>{title}</div>")
    html.append(f"<div class='quiz-body' style='color:#374151;line-height:1.6;white-space:pre-wrap;'>{body}</div>")
    if code is not None:
        html.append("<pre style='background:#111827;color:#e5e7eb;padding:10px 12px;border-radius:8px;overflow:auto;margin-top:10px;font-size:0.95rem;'>")
        html.append(code)
        html.append("</pre>")
    html.append("</div>")
    display(HTML("".join(html)))

# ====== 입력 체크 유틸 ======
def _eq(ans, expect):
    if isinstance(expect, (list, tuple, set)):
        return ans.strip() in [str(x).strip() for x in expect], f"정답은 {expect} 중 하나입니다."
    return ans.strip() == str(expect).strip(), f"정답은 {expect} 입니다."

def _norm_token(a):
    return " ".join(a.strip().lower().replace('`','').replace('"',"'").split())

def _one_of(ans, accepted):
    return any(_norm_token(ans) == _norm_token(a) for a in accepted)

def _ask_until_correct(checker, prompt="> "):
    while True:
        ans = input(prompt)
        ok, msg = checker(ans)
        if ok:
            print(f"{CORRECT_ICON} 정답입니다!\n")
            return ans
        else:
            print(f"{WRONG_ICON} {msg} 다시 시도하세요.\n")

# ====== 문제 정의 ======
# 각 문제는 show_qN(), ask_qN(), explain_qN()로 구성
# 정답 맵과 해설 맵 제공: _answer_map(), _explain_map()

def show_q1():
    _panel("Q1 (쉬움)",
           "다음 중 파이썬에서 불린 참을 나타내는 리터럴을 고르시오.\nA) true  B) True  C) 'True'  D) 1")

def ask_q1():
    return _ask_until_correct(lambda a: _eq(a, 'B'))

def explain_q1():
    return "파이썬 불린 리터럴은 True, False 이다. 문자열 'True'나 소문자 true는 다르다."

def show_q2():
    _panel("Q2 (쉬움)",
           "다음 표현식의 타입을 고르시오: type(10 + 10.0)\nA) int  B) float  C) str  D) bool")

def ask_q2():
    return _ask_until_correct(lambda a: _eq(a, 'B'))

def explain_q2():
    return "정수와 부동소수 합은 부동소수(float)로 승격된다."

def show_q3():
    _panel("Q3 (쉬움)",
           "다음 중 대입 연산을 나타내는 기호를 고르시오.\nA) ==  B) =  C) :=  D) ===")

def ask_q3():
    return _ask_until_correct(lambda a: _eq(a, 'B'))

def explain_q3():
    return "= 는 대입, == 는 동등 비교, := 는 할당식, === 는 파이썬에 없다."

def show_q4():
    _panel("Q4 (쉬움)",
           "표현식 0.1 + 0.2 == 0.3 의 평가 결과를 고르시오.\nA) True  B) False")

def ask_q4():
    return _ask_until_correct(lambda a: _eq(a, 'B'))

def explain_q4():
    return "부동소수 이진 표현 오차로 인해 False가 된다."

def show_q5():
    _panel("Q5 (쉬움)",
           "다음 중 불변(immutable) 시퀀스를 고르시오.\nA) list  B) tuple  C) set  D) dict")

def ask_q5():
    return _ask_until_correct(lambda a: _eq(a, 'B'))

def explain_q5():
    return "tuple은 불변, list는 가변, set은 집합, dict는 매핑 가변."

def show_q6():
    _panel("Q6 (쉬움)",
           "문자열 s = 'Data' 에서 s[1:3] 의 값은 무엇인가?\nA) 'Da'  B) 'at'  C) 'ta'  D) 'at'")

def ask_q6():
    return _ask_until_correct(lambda a: _eq(a, ['C','ta']))

def explain_q6():
    return "인덱스 1부터 3-1까지로 'a','t'가 아닌 'at'이 아니라 'at'? 주의: 'Data'에서 [1:3]은 'at'이 아니라 'at'? 정확히는 s='Data' -> s[1:3]=='at'이다."

def show_q7():
    _panel("Q7 (쉬움)",
           "리스트 nums = [1,2,3]; nums[0] = 9 이후 nums는?\nA) [1,2,3]  B) [9,2,3]  C) [1,9,3]  D) 오류")

def ask_q7():
    return _ask_until_correct(lambda a: _eq(a, 'B'))

def explain_q7():
    return "리스트는 가변이므로 첫 원소가 9로 치환된다."

def show_q8():
    _panel("Q8 (쉬움)",
           "세트 s = {1,2,2,3} 의 길이는?\nA) 3  B) 4  C) 2  D) 1")

def ask_q8():
    return _ask_until_correct(lambda a: _eq(a, 'A'))

def explain_q8():
    return "중복이 제거되어 {1,2,3}이므로 길이는 3."

def show_q9():
    _panel("Q9 (쉬움)",
           "딕셔너리 d = {'a':1}; d['b']=2 수행 후 키 목록에 포함되지 않는 것은?\nA) a  B) b  C) c  D) 둘 다 포함")

def ask_q9():
    return _ask_until_correct(lambda a: _eq(a, 'C'))

def explain_q9():
    return "키는 'a','b'만 존재한다."

def show_q10():
    _panel("Q10 (쉬움)",
           "range(2,8,2) 를 리스트로 변환한 결과를 고르시오.\nA) [2,4,6,8]  B) [2,4,6]  C) [2,3,4,5,6,7]  D) [3,5,7]")

def ask_q10():
    return _ask_until_correct(lambda a: _eq(a, 'B'))

def explain_q10():
    return "끝은 포함되지 않으므로 2,4,6."

def show_q11():
    _panel("Q11 (쉬움)",
           "문자열 '10'을 int로 안전 변환하려면 무엇을 사용하는가?\nA) int('10')  B) float('10')  C) str(10)  D) bool('10')")

def ask_q11():
    return _ask_until_correct(lambda a: _eq(a, 'A'))

def explain_q11():
    return "정수 문자열은 int()로 변환."

def show_q12():
    _panel("Q12 (쉬움)",
           "다음 중 빈 세트를 만드는 올바른 방법은?\nA) {}  B) set()  C) []  D) empty_set()")

def ask_q12():
    return _ask_until_correct(lambda a: _eq(a, 'B'))

def explain_q12():
    return "{}는 빈 dict이다. 빈 set은 set()."

def show_q13():
    _panel("Q13 (쉬움)",
           "리스트 a = [0,1,2,3,4]; a[1:4] = [9,9] 이후 a는?\nA) [0,9,9,4]  B) [0,9,9,3,4]  C) [0,1,2,3,4]  D) 오류")

def ask_q13():
    return _ask_until_correct(lambda a: _eq(a, 'A'))

def explain_q13():
    return "슬라이스 치환은 길이가 달라도 가능하며 해당 구간이 축소된다."

# ====== 중간 난이도 (5) ======

def show_q14():
    _panel("Q14 (중간)",
           "집합 A={1,2,3}, B={3,4} 일 때 A ^ B 의 결과를 고르시오.\nA) {3}  B) {1,2,4}  C) {1,2,3,4}  D) {1,2}")

def ask_q14():
    return _ask_until_correct(lambda a: _eq(a, 'B'))

def explain_q14():
    return "대칭차: 공통 원소를 제외한 합집합, {1,2,4}."

def show_q15():
    _panel("Q15 (중간)",
           "다음 코드 실행 후 x의 값은?\n코드:\n"
           "x = {'a':1, 'b':2}\n"
           "x.update({'b':5, 'c':9})\n"
           "x.get('d', -1)")
def ask_q15():
    return _ask_until_correct(lambda a: _eq(a, \"{'a': 1, 'b': 5, 'c': 9}\"))

def explain_q15():
    return "update로 b가 5로 바뀌고 c가 추가된다. get은 조회만 하며 x를 바꾸지 않는다."

def show_q16():
    _panel("Q16 (중간)",
           "튜플 t=(1,[2,3]); t[1].append(4) 이후 t의 값은?\nA) (1,[2,3,4])  B) (1,[2,3])  C) 오류  D) (1,(2,3,4))")

def ask_q16():
    return _ask_until_correct(lambda a: _eq(a, 'A'))

def explain_q16():
    return "튜플은 불변이지만 내부 가변 객체의 내용 변경은 가능하다."

def show_q17():
    _panel("Q17 (중간)",
           "문자열 s='abcdefg'에서 s[-6:-1:2]의 결과를 고르시오.\nA) 'bdf'  B) 'bde'  C) 'ace'  D) 'bdfg'")

def ask_q17():
    return _ask_until_correct(lambda a: _eq(a, 'A'))

def explain_q17():
    return "인덱스 -6..-1(미포함), 간격 2 → b,d,f."

def show_q18():
    _panel("Q18 (중간)",
           "다음 중 dict 키로 유효한 것은 모두 고르시오.\nA) [1,2]  B) (1,2)  C) {'a':1}  D) 'key'")

def ask_q18():
    return _ask_until_correct(lambda a: _one_of(a, ['B D', 'D B', 'B, D', '(1,2) and \"key\"']))

def explain_q18():
    return "키는 해시가능해야 하므로 불변형(예: 튜플, 문자열)은 가능. 리스트, dict는 불가."

# ====== 어려움 (2) ======

def show_q19():
    _panel("Q19 (어려움)",
           "다음 코드 실행 결과를 정확히 쓰시오.\n코드:\n"
           "a = [0,1,2,3]\n"
           "b = a\n"
           "a[1:3] = [9]\n"
           "b.append(7)\n"
           "print(a, b)")

def ask_q19():
    return _ask_until_correct(lambda a: _eq(a, \"[0, 9, 3, 7] [0, 9, 3, 7]\"))

def explain_q19():
    return "a와 b는 같은 리스트를 참조. 슬라이스 치환으로 [1:3]이 하나의 9로 대체되어 [0,9,3]. append로 7 추가."

def show_q20():
    _panel("Q20 (어려움)",
           "집합 연산에서 다음을 만족하는 모든 x를 공백으로 구분해 쓰시오.\n조건: A={1,2,3,4}, B={2,4,6}, x ∈ A 이고 x not in (A & B)")

def ask_q20():
    return _ask_until_correct(lambda a: _one_of(a, ['1 3','3 1']))

def explain_q20():
    return "A∩B={2,4}. A에서 교집합을 제외하면 {1,3}."

# ====== 맵 ======
def _answer_map():
    return {
        1:'B',2:'B',3:'B',4:'B',5:'B',6:'C',7:'B',8:'A',9:'C',10:'B',
        11:'A',12:'B',13:'A',14:'B',15:\"{'a': 1, 'b': 5, 'c': 9}\",
        16:'A',17:'A',18:'B D',19:\"[0, 9, 3, 7] [0, 9, 3, 7]\",20:'1 3'
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
    # 미리보기
    show_all()
    print("정답 맵:", answers())

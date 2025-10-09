# -*- coding: utf-8 -*-
# Midterm_Q.py : 중간시험(Week2~Week4) — 20문항(쉬움 13, 중간 5, 어려움 2)
# UI와 매개변수는 Week4_Q.py의 _panel / _ask_until_correct / set_icons 등을 그대로 사용
from Week4_Q import _panel, _ask_until_correct, set_icons, CORRECT_ICON, WRONG_ICON

# ============== 쉬움 13 ==============
def show_q1():
    _panel("Q1) 객관식: 불린 리터럴",
           "다음 중 파이썬에서 불린 참을 나타내는 리터럴을 고르시오.\nA) true  B) True  C) 'True'  D) 1")

def answer_q1(show_explanation: bool = False):
    return _ask_until_correct(lambda a: (a.strip() == 'B', "정답은 B 입니다."))

def show_q2():
    _panel("Q2) 객관식: 타입 승격",
           "다음 표현식의 타입을 고르시오: type(10 + 10.0)\nA) int  B) float  C) str  D) bool")

def answer_q2(show_explanation: bool = False):
    return _ask_until_correct(lambda a: (a.strip() == 'B', "정답은 B 입니다."))

def show_q3():
    _panel("Q3) 객관식: 대입 연산자",
           "다음 중 대입 연산을 나타내는 기호를 고르시오.\nA) ==  B) =  C) :=  D) ===")

def answer_q3(show_explanation: bool = False):
    return _ask_until_correct(lambda a: (a.strip() == 'B', "정답은 B 입니다."))

def show_q4():
    _panel("Q4) 객관식: 부동소수점 비교",
           "표현식 0.1 + 0.2 == 0.3 의 평가 결과를 고르시오.\nA) True  B) False")

def answer_q4(show_explanation: bool = False):
    return _ask_until_correct(lambda a: (a.strip() == 'B', "정답은 B 입니다."))

def show_q5():
    _panel("Q5) 객관식: 불변 시퀀스",
           "다음 중 불변(immutable) 시퀀스를 고르시오.\nA) list  B) tuple  C) set  D) dict")

def answer_q5(show_explanation: bool = False):
    return _ask_until_correct(lambda a: (a.strip() == 'B', "정답은 B 입니다."))

def show_q6():
    _panel("Q6) 객관식: 슬라이싱",
           "문자열 s = 'Data' 에서 s[1:3] 의 값은 무엇인가?\nA) 'Da'  B) 'at'  C) 'ta'  D) 'dt'")

def answer_q6(show_explanation: bool = False):
    return _ask_until_correct(lambda a: (a.strip() in ('B', '\"at\"', "'at'", "at"), "정답은 B 입니다."))

def show_q7():
    _panel("Q7) 객관식: 리스트 치환",
           "리스트 nums = [1,2,3]; nums[0] = 9 이후 nums는?\nA) [1,2,3]  B) [9,2,3]  C) [1,9,3]  D) 오류")

def answer_q7(show_explanation: bool = False):
    return _ask_until_correct(lambda a: (a.strip() == 'B', "정답은 B 입니다."))

def show_q8():
    _panel("Q8) 객관식: 세트 길이",
           "세트 s = {1,2,2,3} 의 길이는?\nA) 3  B) 4  C) 2  D) 1")

def answer_q8(show_explanation: bool = False):
    return _ask_until_correct(lambda a: (a.strip() == 'A', "정답은 A 입니다."))

def show_q9():
    _panel("Q9) 객관식: 딕셔너리 키",
           "d = {'a':1}; d['b']=2 수행 후 키 목록에 포함되지 않는 것은?\nA) a  B) b  C) c  D) 둘 다 포함")

def answer_q9(show_explanation: bool = False):
    return _ask_until_correct(lambda a: (a.strip() == 'C', "정답은 C 입니다."))

def show_q10():
    _panel("Q10) 객관식: range",
           "range(2,8,2) 를 리스트로 변환한 결과를 고르시오.\nA) [2,4,6,8]  B) [2,4,6]  C) [2,3,4,5,6,7]  D) [3,5,7]")

def answer_q10(show_explanation: bool = False):
    return _ask_until_correct(lambda a: (a.strip() == 'B', "정답은 B 입니다."))

def show_q11():
    _panel("Q11) 객관식: 문자열->정수 변환",
           "문자열 '10'을 int로 안전 변환하려면 무엇을 사용하는가?\nA) int('10')  B) float('10')  C) str(10)  D) bool('10')")

def answer_q11(show_explanation: bool = False):
    return _ask_until_correct(lambda a: (a.strip() == 'A', "정답은 A 입니다."))

def show_q12():
    _panel("Q12) 객관식: 빈 set 생성",
           "다음 중 빈 세트를 만드는 올바른 방법은?\nA) {}  B) set()  C) []  D) empty_set()")

def answer_q12(show_explanation: bool = False):
    return _ask_until_correct(lambda a: (a.strip() == 'B', "정답은 B 입니다."))

def show_q13():
    _panel("Q13) 객관식: 슬라이스 치환 축소",
           "리스트 a = [0,1,2,3,4]; a[1:4] = [9,9] 이후 a는?\nA) [0,9,9,4]  B) [0,9,9,3,4]  C) [0,1,2,3,4]  D) 오류")

def answer_q13(show_explanation: bool = False):
    return _ask_until_correct(lambda a: (a.strip() == 'A', "정답은 A 입니다."))

# ============== 중간 5 ==============
def show_q14():
    _panel("Q14) 객관식: 대칭차",
           "집합 A={1,2,3}, B={3,4} 일 때 A ^ B 의 결과를 고르시오.\nA) {3}  B) {1,2,4}  C) {1,2,3,4}  D) {1,2}")

def answer_q14(show_explanation: bool = False):
    return _ask_until_correct(lambda a: (a.strip() == 'B', "정답은 B 입니다."))

def show_q15():
    _panel("Q15) 주관식: dict 업데이트 결과",
           "다음 코드 실행 후 x의 값을 정확히 쓰시오.",
           code="x = {'a':1, 'b':2}\nx.update({'b':5, 'c':9})\nx.get('d', -1)\nprint(x)")

def answer_q15(show_explanation: bool = False):
    expect = "{'a': 1, 'b': 5, 'c': 9}"
    return _ask_until_correct(lambda a: (a.strip() == expect, f"정답은 {expect} 입니다."))

def show_q16():
    _panel("Q16) 객관식: 튜플과 가변 내부",
           "튜플 t=(1,[2,3]); t[1].append(4) 이후 t의 값은?\nA) (1,[2,3,4])  B) (1,[2,3])  C) 오류  D) (1,(2,3,4))")

def answer_q16(show_explanation: bool = False):
    return _ask_until_correct(lambda a: (a.strip() == 'A', "정답은 A 입니다."))

def show_q17():
    _panel("Q17) 객관식: 음수 인덱스 슬라이싱",
           "문자열 s='abcdefg'에서 s[-6:-1:2]의 결과를 고르시오.\nA) 'bdf'  B) 'bde'  C) 'ace'  D) 'bdfg'")

def answer_q17(show_explanation: bool = False):
    return _ask_until_correct(lambda a: (a.strip() == 'A', "정답은 A 입니다."))

def show_q18():
    _panel("Q18) 객관식: dict 키로 가능한 것",
           "다음 중 dict 키로 유효한 것은 모두 고르시오.\nA) [1,2]  B) (1,2)  C) {'a':1}  D) 'key'")

def answer_q18(show_explanation: bool = False):
    ok = lambda s: s.strip() in ("B D", "D B", "B, D", "(1,2) and 'key'", "(1,2) and \"key\"")
    return _ask_until_correct(lambda a: (ok(a), "정답은 B D 입니다."))

# ============== 어려움 2 ==============
def show_q19():
    _panel("Q19) 주관식: 참조 공유와 슬라이스 치환",
           "다음 코드 실행 결과를 정확히 쓰시오.",
           code="a = [0,1,2,3]\nb = a\na[1:3] = [9]\nb.append(7)\nprint(a, b)")

def answer_q19(show_explanation: bool = False):
    expect = "[0, 9, 3, 7] [0, 9, 3, 7]"
    return _ask_until_correct(lambda a: (a.strip() == expect, f"정답은 {expect} 입니다."))

def show_q20():
    _panel("Q20) 주관식: 집합 조건",
           "집합 연산에서 다음을 만족하는 모든 x를 공백으로 구분해 쓰시오.\n조건: A={1,2,3,4}, B={2,4,6}, x ∈ A 이고 x not in (A & B)")

def answer_q20(show_explanation: bool = False):
    ok = lambda s: s.strip() in ("1 3", "3 1")
    return _ask_until_correct(lambda a: (ok(a), "정답은 1 3 입니다."))

# ============== 편의 함수 ==============
def show_all():
    for i in range(1, 21):
        globals()[f"show_q{i}"]()

def answer_all():
    # 반환은 문제 번호 -> 정답 문자열
    return {
        1:'B',2:'B',3:'B',4:'B',5:'B',6:'B',7:'B',8:'A',9:'C',10:'B',
        11:'A',12:'B',13:'A',14:'B',15:"{'a': 1, 'b': 5, 'c': 9}",
        16:'A',17:'A',18:'B D',19:"[0, 9, 3, 7] [0, 9, 3, 7]",20:'1 3'
    }

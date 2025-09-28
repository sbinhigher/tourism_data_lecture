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

def show_q1():
    _panel(
        "Q1) 주관식: 리스트 중복 제거",
        "다음 리스트의 중복을 제거하여 새로운 리스트로 출력하세요.",
        code="nums = [1, 2, 2, 3, 4, 4, 5]\nprint(    )"
    )
def answer_q1(show_explanation: bool = True):
    nums = [1, 2, 2, 3, 4, 4, 5]
    def checker(src):
        ns = {"nums": nums}
        try:
            result = eval(src, {}, ns)
        except Exception:
            return (False, "실행 오류, list(set(nums)) 형태로 입력하세요.")
        if isinstance(result, list) and set(result) == set(nums):
            return (True, "")
        return (False, "중복 제거가 되지 않았거나 리스트 형태가 아닙니다.")
    ans = _ask_until_correct(checker)
    if show_explanation: explain_q1()
    return ans

def show_q2():
    _panel(
        "Q2) 객관식: 3차원 인덱싱/슬라이싱",
        "다음에서 `tensor[1][0][1:]` 의 결과를 고르세요.",
        code=(
            "tensor = [\n"
            "  [[1, 2, 3], [4, 5, 6]],\n"
            "  [[7, 8, 9], [10, 11, 12]]\n"
            "]"
        )
    )
    display(Markdown(
        "보기\n\n"
        "1) [8, 9]\n\n"
        "2) 8\n\n"
        "3) [7, 8]\n\n"
        "4) [10, 11, 12]"
    ))

def answer_q2(show_explanation: bool = True):
    # 정답: 1) [8, 9]
    ans = _ask_until_correct(
        lambda s: (_matches_any(s, "1", "[8, 9]", "[8,9]"),
                   "정답은 1) [8, 9] 입니다.")
    )
    if show_explanation:
        explain_q2()
    return ans

def show_q3():
    _panel(
        "Q3) 객관식: 튜플의 불변성",
        "다음 중 실행 시 오류가 발생하는 코드는?",
        code="t = (1, 2, 3)"
    )
    display(Markdown("1) print(t[1])\n\n2) t[1] = 5\n\n3) new_t = t + (4,)\n\n4) print(len(t))"))
def answer_q3(show_explanation: bool = True):
    ans = _ask_until_correct(lambda s: (_matches_any(s, "2", "t[1] = 5"), "정답은 2) 입니다. 튜플은 원소 변경 불가."))
    if show_explanation: explain_q3()
    return ans

def show_q4():
    _panel(
        "Q4) 주관식: range → list 변환",
        "다음 range 객체를 리스트로 변환하여 출력하세요.",
        code="r = range(2, 11, 2)\nprint(    )"
    )
def answer_q4(show_explanation: bool = True):
    ans = _ask_until_correct(lambda s: (_matches_any(s, "list(r)"), "예: list(r)"))
    if show_explanation: explain_q4()
    return ans

def show_q5():
    _panel(
        "Q5) 주관식: 집합에 원소 추가",
        '"orange" 를 집합에 추가하고 출력하세요.',
        code='fruits = {"apple", "banana"}\nprint(fruits)'
    )
def answer_q5(show_explanation: bool = True):
    def checker(line):
        ns = {"fruits": {"apple", "banana"}}
        try: exec(line, {}, ns)
        except Exception as e: return (False, f"실행 에러: {e}")
        return ("orange" in ns["fruits"], "fruits.add('orange') 형태로 추가하세요.")
    ans = _ask_until_correct(checker)
    if show_explanation: explain_q5()
    return ans

def show_q6():
    _panel(
        "Q6) 객관식: 집합 연산",
        "`set_a & set_b` 의 결과를 고르세요.",
        code='set_a = {"a", "b", "c"}\nset_b = {"b", "c", "d"}'
    )
    display(Markdown("1) {'a', 'b'}\n\n2) {'b', 'c'}\n\n3) {'c', 'd'}\n\n4) {'a', 'd'}"))
def answer_q6(show_explanation: bool = True):
    ans = _ask_until_correct(lambda s: (_matches_any(s, "2", "{'b','c'}", "{'b', 'c'}"), "정답은 2) 입니다."))
    if show_explanation: explain_q6()
    return ans

def show_q7():
    _panel(
        "Q7) 주관식: 안전 삭제 discard",
        '"rabbit" 을 안전하게 삭제하고 결과를 출력하세요.',
        code='animals = {"cat", "dog"}\nprint(animals)'
    )
def answer_q7(show_explanation: bool = True):
    def checker(line):
        ns = {"animals": {"cat", "dog"}}
        try: exec(line, {}, ns)
        except Exception as e: return (False, f"실행 에러: {e}")
        return (True, "")
    ans = _ask_until_correct(checker)
    if show_explanation: explain_q7()
    return ans

def show_q8():
    _panel(
        "Q8) 주관식: 딕셔너리에 키-값 추가",
        '"email" 키에 "lee@example.com" 을 추가하고 출력하세요.',
        code='student = {"name": "Lee", "age": 21, "major": "Data Science"}\nprint(student)'
    )
def answer_q8(show_explanation: bool = True):
    def checker(line):
        ns = {"student": {"name":"Lee", "age":21, "major":"Data Science"}}
        try: exec(line, {}, ns)
        except Exception as e: return (False, f"실행 에러: {e}")
        return (ns["student"].get("email")=="lee@example.com", "student['email'] 추가 필요")
    ans = _ask_until_correct(checker)
    if show_explanation: explain_q8()
    return ans

def show_q9():
    _panel(
        "Q9) 객관식: get 기본값",
        '`info.get("email", "N/A")` 의 결과를 고르세요.',
        code='info = {"id": 1001, "name": "Park"}'
    )
    display(Markdown("1) None\n\n2) \"N/A\"\n\n3) Error\n\n4) {\"email\": \"N/A\"}"))
def answer_q9(show_explanation: bool = True):
    ans = _ask_until_correct(lambda s: (_matches_any(s, "2", "n/a", '"n/a"'), "정답은 2) \"N/A\" 입니다."))
    if show_explanation: explain_q9()
    return ans

def show_q10():
    _panel(
        "Q10) 객관식: 컬렉션형 특징 연결",
        "다음 중 특징 연결이 잘못된 것을 고르세요."
    )
    display(Markdown("1) list : 순서 있음, 수정 가능\n\n2) tuple : 순서 있음, 수정 가능\n\n3) set : 순서 없음, 중복 불가\n\n4) dict : 키-값 쌍 저장, 키는 중복 불가"))
def answer_q10(show_explanation: bool = True):
    ans = _ask_until_correct(lambda s: (_matches_any(s, "2", "tuple : 순서 있음, 수정 가능"), "정답은 2) 입니다."))
    if show_explanation: explain_q10()
    return ans

# =========================
# 해설 함수 (생략하지 않고 그대로)
# =========================
def explain_q1(): print("Q1 해설: list(set(nums)) 로 중복 제거 후 리스트 변환")
def explain_q2():
    print("Q2 해설: 3차원 인덱싱/슬라이싱")
    print("- tensor[1]           → [[7, 8, 9], [10, 11, 12]]  (두 번째 '층')")
    print("- tensor[1][0]        → [7, 8, 9]                   (그 층의 첫 번째 '행')")
    print("- tensor[1][0][1:]    → [8, 9]                      (그 행의 인덱스 1부터 끝까지)")
def explain_q3(): print("Q3 해설: 튜플은 불변이라 t[1]=5는 오류")
def explain_q4(): print("Q4 해설: range 객체는 list()로 변환해야 원소 출력")
def explain_q5(): print("Q5 해설: fruits.add('orange') 로 원소 추가")
def explain_q6(): print("Q6 해설: & 는 교집합, 결과는 {'b','c'}")
def explain_q7(): print("Q7 해설: discard는 원소 없어도 오류 없음")
def explain_q8(): print("Q8 해설: student['email']='...' 으로 추가")
def explain_q9(): print("Q9 해설: get(key,default) → 없으면 'N/A'")
def explain_q10(): print("Q10 해설: tuple은 수정 불가, 나머지는 맞음")

def show_all_explanations(show_answer=True):
    for i in range(1, 11):
        print(f"\n### Q{i}")
        if show_answer:
            print("정답:", _answer_key()[i])
        _explain_func_map()[i]()
    print("\n✅ 모든 해설 출력 완료")

def _answer_key():
    return {
        1: "list(set(nums))",
        2: "1. [8, 9]",
        3: "t[1] = 5",
        4: "list(r)",
        5: "fruits.add('orange')",
        6: "{'b', 'c'}",
        7: "animals.discard('rabbit')",
        8: "student['email'] = 'lee@example.com'",
        9: "'N/A'",
        10:"2 (tuple은 수정 불가)"
    }

def _explain_func_map():
    return {1:explain_q1,2:explain_q2,3:explain_q3,4:explain_q4,5:explain_q5,6:explain_q6,7:explain_q7,8:explain_q8,9:explain_q9,10:explain_q10}

def show_all():
    show_q1(); show_q2(); show_q3(); show_q4()
    show_q5(); show_q6(); show_q7()
    show_q8(); show_q9(); show_q10()
    display(Markdown("> 모든 문제 프리뷰가 표시되었습니다."))

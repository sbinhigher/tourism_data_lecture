# -*- coding: utf-8 -*-
# Week4_Q.py : 컬렉션형 과제(순서형 4, 집합형 3, 매핑형 3)
# Week3_Q 포맷을 그대로 계승 (패널 UI, 정답/해설 분리, show_explanation 옵션)
from IPython.display import display, HTML, Markdown
import io
import contextlib

# ====== 글로벌 아이콘 (사용자가 변경 가능) ======
CORRECT_ICON = "✅"
WRONG_ICON   = "❌"

def set_icons(correct="✅", wrong="❌"):
    """정답/오답 아이콘 변경 (예: set_icons(correct='🎉', wrong='🚫'))"""
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
.quiz-hint  {color:#6b7280;font-size:0.92rem;margin-top:8px;}
</style>
"""

def _panel(title, body_md, code=None, hint=None):
    html = [PANEL_CSS, '<div class="quiz-panel">']
    html += [f'<div class="quiz-title">{title}</div>',
             f'<div class="quiz-body">{body_md}</div>']
    if code:
        html.append(f'<div class="quiz-code">{code}</div>')
    if hint:
        html.append(f'<div class="quiz-hint">힌트: {hint}</div>')
    html.append('</div>')
    display(HTML("".join(html)))

# ====== 공용 헬퍼 ======
def _matches_any(user_input, *accepted):
    """번호/문구를 대소문자/공백 차이 허용하여 비교"""
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

# ====== (선택) 도메인 데이터 (필요 시 활용) ======
destination = "Jeju"
spots = ["Hallasan", "Seongsan Ilchulbong", "Hyeopjae Beach"]

# =========================
# Week4 과제: 컬렉션형 (Q1~Q10)
# - 순서형 4, 집합형 3, 매핑형 3
# =========================

# ---------- [Sequence 1/4] ----------
def show_q1():
    _panel(
        "Q1) 주관식: 리스트 중복 제거",
        "다음 리스트의 **중복을 제거**하여 새로운 리스트로 출력하세요.",
        code="nums = [1, 2, 2, 3, 4, 4, 5]\nprint(    )",
        hint="list(set(nums)) 또는 sorted(set(nums)) 등 결과 원소 집합이 같으면 정답 처리"
    )
def answer_q1(show_explanation: bool = True):
    nums = [1, 2, 2, 3, 4, 4, 5]
    expected_set = set(nums)
    def checker(src):
        src = src.strip()
        if not src:
            return (False, "표현식을 한 줄 입력하세요. 예: list(set(nums))")
        # 실행/평가
        ns = {"nums": nums}
        buf = io.StringIO()
        result = None
        try:
            result = eval(src, {}, ns)
        except SyntaxError:
            try:
                with contextlib.redirect_stdout(buf):
                    exec(src, {}, ns)
            except Exception as e:
                return (False, f"실행 에러: {e}")
        except Exception as e:
            return (False, f"실행 에러: {e}")

        out = buf.getvalue().strip()
        candidate = None
        if isinstance(result, list):
            candidate = result
        elif out:
            try:
                candidate = eval(out, {}, {})
            except Exception:
                candidate = None

        if isinstance(candidate, list) and set(candidate) == set(nums):
            return (True, "")
        return (False, "중복 제거가 되지 않았거나 리스트 형태가 아닙니다. 예: list(set(nums))")
    ans = _ask_until_correct(checker)
    if show_explanation:
        explain_q1()
    return ans

# ---------- [Sequence 2/4] ----------
def show_q2():
    _panel(
        "Q2) 객관식: 다차원 인덱싱/슬라이싱",
        "다음에서 `matrix[1][0:2]` 의 결과를 고르세요.",
        code="matrix = [[10, 20], [30, 40], [50, 60]]",
        hint="행 인덱스 1 → [30, 40] 에서 0:2 슬라이싱"
    )
    display(Markdown(
        "보기\n\n"
        "1) 20\n\n"
        "2) [30, 40]\n\n"
        "3) 50\n\n"
        "4) [10, 20]"
    ))
def answer_q2(show_explanation: bool = True):
    ans = _ask_until_correct(lambda s: (_matches_any(s, "2", "[30, 40]"), "정답은 2) [30, 40] 입니다."))
    if show_explanation:
        explain_q2()
    return ans

# ---------- [Sequence 3/4] ----------
def show_q3():
    _panel(
        "Q3) 객관식: 튜플의 불변성",
        "다음 중 **실행 시 오류가 발생하는 코드**는?",
        code="t = (1, 2, 3)",
        hint="튜플은 불변(immutable)"
    )
    display(Markdown(
        "보기\n\n"
        "1) print(t[1])\n\n"
        "2) t[1] = 5\n\n"
        "3) new_t = t + (4,)\n\n"
        "4) print(len(t))"
    ))
def answer_q3(show_explanation: bool = True):
    ans = _ask_until_correct(lambda s: (_matches_any(s, "2", "t[1] = 5"), "정답은 2) 입니다. 튜플은 원소 변경 불가."))
    if show_explanation:
        explain_q3()
    return ans

# ---------- [Sequence 4/4] ----------
def show_q4():
    _panel(
        "Q4) 주관식: range → list 변환",
        "다음 range 객체를 **리스트로 변환**하여 출력하세요.",
        code="r = range(2, 11, 2)\nprint(    )",
        hint="list(r)"
    )
def answer_q4(show_explanation: bool = True):
    ans = _ask_until_correct(lambda s: (_matches_any(s, "list(r)"), "예: list(r)"))
    if show_explanation:
        explain_q4()
    return ans

# ---------- [Set 1/3] ----------
def show_q5():
    _panel(
        "Q5) 주관식: 집합에 원소 추가",
        '"orange" 를 집합에 **추가**하고 출력하세요.',
        code='fruits = {"apple", "banana"}\n# 여기에 코드를 작성\nprint(fruits)',
        hint="fruits.add('orange')"
    )
def answer_q5(show_explanation: bool = True):
    fruits = {"apple", "banana"}
    def checker(line):
        src = line.strip()
        if not src:
            return (False, "한 줄로 입력하세요. 예: fruits.add('orange')")
        ns = {"fruits": set(fruits)}
        try:
            exec(src, {}, ns)
        except Exception as e:
            return (False, f"실행 에러: {e}")
        ok = "orange" in ns["fruits"]
        return (ok, "fruits.add('orange') 형태로 추가하세요.")
    ans = _ask_until_correct(checker)
    if show_explanation:
        explain_q5()
    return ans

# ---------- [Set 2/3] ----------
def show_q6():
    _panel(
        "Q6) 객관식: 집합 연산",
        "`set_a & set_b` 의 결과를 고르세요.",
        code='set_a = {"a", "b", "c"}\nset_b = {"b", "c", "d"}',
        hint="& 는 교집합"
    )
    display(Markdown(
        "보기\n\n"
        "1) {'a', 'b'}\n\n"
        "2) {'b', 'c'}\n\n"
        "3) {'c', 'd'}\n\n"
        "4) {'a', 'd'}"
    ))
def answer_q6(show_explanation: bool = True):
    ans = _ask_until_correct(lambda s: (_matches_any(s, "2", "{'b','c'}", "{'b', 'c'}"), "정답은 2) 입니다."))
    if show_explanation:
        explain_q6()
    return ans

# ---------- [Set 3/3] ----------
def show_q7():
    _panel(
        "Q7) 주관식: 안전 삭제 discard",
        '"rabbit" 을 **안전하게 삭제**하고 결과를 출력하세요.',
        code='animals = {"cat", "dog"}\n# 여기에 코드를 작성\nprint(animals)',
        hint="discard는 없어도 오류가 나지 않습니다."
    )
def answer_q7(show_explanation: bool = True):
    def checker(line):
        src = line.strip()
        if not src:
            return (False, "한 줄로 입력하세요. 예: animals.discard('rabbit')")
        ns = {"animals": {"cat", "dog"}}
        try:
            exec(src, {}, ns)
        except Exception as e:
            return (False, f"실행 에러: {e}")
        # 성공 조건: 오류 없이 실행되고, 원소 유지(또는 변화 없음)
        return (True, "")
    ans = _ask_until_correct(checker)
    if show_explanation:
        explain_q7()
    return ans

# ---------- [Dict 1/3] ----------
def show_q8():
    _panel(
        "Q8) 주관식: 딕셔너리에 키-값 추가",
        '"email" 키에 "lee@example.com" 을 **추가**하고 출력하세요.',
        code='student = {"name": "Lee", "age": 21, "major": "Data Science"}\n# 여기에 코드를 작성\nprint(student)',
        hint='student["email"] = "lee@example.com"'
    )
def answer_q8(show_explanation: bool = True):
    def checker(line):
        src = line.strip()
        if not src:
            return (False, '한 줄로 입력하세요. 예: student["email"] = "lee@example.com"')
        ns = {"student": {"name":"Lee", "age":21, "major":"Data Science"}}
        try:
            exec(src, {}, ns)
        except Exception as e:
            return (False, f"실행 에러: {e}")
        ok = ns["student"].get("email") == "lee@example.com"
        return (ok, 'student["email"] = "lee@example.com" 형태로 추가하세요.')
    ans = _ask_until_correct(checker)
    if show_explanation:
        explain_q8()
    return ans

# ---------- [Dict 2/3] ----------
def show_q9():
    _panel(
        "Q9) 객관식: get 기본값",
        '`info.get("email", "N/A")` 의 결과를 고르세요.',
        code='info = {"id": 1001, "name": "Park"}',
        hint="키가 없으면 기본값 반환"
    )
    display(Markdown(
        "보기\n\n"
        "1) None\n\n"
        "2) \"N/A\"\n\n"
        "3) Error\n\n"
        "4) {\"email\": \"N/A\"}"
    ))
def answer_q9(show_explanation: bool = True):
    ans = _ask_until_correct(lambda s: (_matches_any(s, "2", "n/a", '"n/a"'), "정답은 2) \"N/A\" 입니다."))
    if show_explanation:
        explain_q9()
    return ans

# ---------- [Dict 3/3] ----------
def show_q10():
    _panel(
        "Q10) 객관식: 컬렉션형 특징 연결",
        "다음 중 **특징 연결이 잘못된 것**을 고르세요.",
        hint="튜플의 수정 가능 여부/순서/중복/키-값 등 기본 성질 점검"
    )
    display(Markdown(
        "보기\n\n"
        "1) list : 순서 있음, 수정 가능\n\n"
        "2) tuple : 순서 있음, 수정 가능\n\n"
        "3) set : 순서 없음, 중복 불가\n\n"
        "4) dict : 키-값 쌍 저장, 키는 중복 불가"
    ))
def answer_q10(show_explanation: bool = True):
    ans = _ask_until_correct(lambda s: (_matches_any(s, "2", "tuple : 순서 있음, 수정 가능"), "정답은 2) 입니다. 튜플은 수정 불가."))
    if show_explanation:
        explain_q10()
    return ans

# =========================
# 해설 함수들
# =========================
def explain_q1():
    print("Q1 해설: list는 중복을 허용하므로 set으로 바꿔 중복 제거 후 다시 list로 만드는 방식이 흔합니다.")
    print("예: list(set(nums))  / 정렬이 필요하면 sorted(set(nums))")

def explain_q2():
    print("Q2 해설: matrix[1] 은 [30, 40], 여기에 [0:2] 슬라이싱을 적용하면 [30, 40] 이 됩니다.")

def explain_q3():
    print("Q3 해설: 튜플은 불변(immutable)이라 원소 변경(t[1]=5)이 불가합니다.")
    print("print(t[1]), t+(4,), len(t)는 모두 정상 동작합니다.")

def explain_q4():
    print("Q4 해설: range는 지연(sequence) 객체라 직접 출력하면 range(시작,끝,간격) 형태로 보입니다.")
    print("원소를 보려면 list(r)로 변환하세요. 예: list(range(2,11,2)) → [2,4,6,8,10]")

def explain_q5():
    print("Q5 해설: set.add(x) 로 원소 추가. 집합은 중복을 허용하지 않고, 순서가 없습니다.")

def explain_q6():
    print("Q6 해설: & 는 교집합. {'a','b','c'} & {'b','c','d'} → {'b','c'}")

def explain_q7():
    print("Q7 해설: discard(x)는 x가 없어도 에러가 나지 않습니다. remove(x)는 없으면 KeyError가 납니다.")

def explain_q8():
    print('Q8 해설: student[\"email\"] = \"lee@example.com\" 처럼 대괄호로 키를 지정해 값을 할당합니다.')

def explain_q9():
    print('Q9 해설: dict.get(key, default)는 키가 없을 때 default를 반환합니다. 여기서는 \"N/A\"')

def explain_q10():
    print("Q10 해설: tuple은 순서가 있지만 수정 불가(immutable)입니다. 나머지 보기는 올바른 연결입니다.")

# =========================
# 정답 + 해설 출력 유틸 (가독성)
# =========================
def _answer_key() -> dict[int, str]:
    return {
        1: "list(set(nums))  (또는 sorted(set(nums)))",
        2: "2  ([30, 40])",
        3: "2  (t[1] = 5 는 오류)",
        4: "list(r)",
        5: "fruits.add('orange')",
        6: "2  ({'b','c'})",
        7: "animals.discard('rabbit')",
        8: 'student["email"] = "lee@example.com"',
        9: '2  ("N/A")',
        10:"2  (tuple은 수정 불가)",
    }

def _explain_func_map():
    return {
        1: explain_q1,
        2: explain_q2,
        3: explain_q3,
        4: explain_q4,
        5: explain_q5,
        6: explain_q6,
        7: explain_q7,
        8: explain_q8,
        9: explain_q9,
        10: explain_q10,
    }

def _title_of(qnum: int) -> str:
    return f"### Q{qnum} 해설"

def _render_block(title_md: str, answer_text: str | None):
    try:
        body = []
        body.append(title_md)
        if answer_text is not None:
            body.append(f"> **정답:** `{answer_text}`  \n")
        display(Markdown("\n\n".join(body)))
    except Exception:
        print(title_md.replace("### ", "").replace("## ", ""))
        if answer_text is not None:
            print(f"[정답] {answer_text}")
        print("-" * 50)

def print_explanation(qnum: int, show_answer: bool = True):
    answers = _answer_key()
    explains = _explain_func_map()
    if qnum not in explains:
        print(f"Q{qnum} 은(는) 존재하지 않습니다. 1~{max(explains)} 사이로 입력하세요.")
        return
    ans_text = answers.get(qnum) if show_answer else None
    _render_block(_title_of(qnum), ans_text)
    explains[qnum]()

def show_all_explanations(show_answer: bool = True):
    explains = _explain_func_map()
    answers = _answer_key()
    try:
        display(Markdown("## 📘 Week4 전체 해설"))
    except Exception:
        print("📘 Week4 전체 해설")
        print("=" * 50)
    for q in range(1, len(explains) + 1):
        ans_text = answers.get(q) if show_answer else None
        _render_block(_title_of(q), ans_text)
        explains[q]()
        try:
            display(Markdown("---"))
        except Exception:
            print("-" * 50)
    try:
        display(Markdown("✅ **모든 해설이 출력되었습니다.**"))
    except Exception:
        print("✅ 모든 해설이 출력되었습니다.")

# ====== 프리뷰 전체 보기 (선택) ======
def show_all():
    show_q1(); show_q2(); show_q3(); show_q4()
    show_q5(); show_q6(); show_q7()
    show_q8(); show_q9(); show_q10()
    display(Markdown("> 프리뷰가 모두 표시되었습니다. 이제 각 문항의 `answer_qX()`를 실행해서 답만 입력하세요!"))

# -*- coding: utf-8 -*-
# Jupyter/콘솔 겸용 모듈: 프리뷰 패널 + 답안 입력 분리, 아이콘 커스터마이즈
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
spot_info = {
    "Hallasan": {"height_m": 1947, "rating": 4.8},
    "Seongsan": {"height_m": 182, "rating": 4.9},
}

# =========================
# Week3 과제: 문자열 (Q1~Q10)
# =========================

# Q1. 인덱싱
def show_q1():
    _panel(
        "Q1) 인덱싱",
        "문자열 s = 'Python' 에서 첫 번째 글자를 출력하는 코드를 작성하세요.",
        code="s = 'Python'\nprint(    )"
    )
def answer_q1(show_explanation: bool = True):
    ans = _ask_until_correct(lambda s: (_matches_any(s, "s[0]"), "힌트: 인덱싱은 0부터 시작합니다."))
    if show_explanation:
        explain_q1()
    return ans

# Q2. 슬라이싱
def show_q2():
    _panel(
        "Q2) 슬라이싱",
        "문자열 s = 'Python' 에서 'Pyt'을 출력하는 코드를 작성하세요.",
        code="s = 'Python'\nprint(    )"
    )
def answer_q2(show_explanation: bool = True):
    ans = _ask_until_correct(lambda s: (_matches_any(s, "s[0:3]", "s[:3]"), "힌트: 끝 인덱스는 포함되지 않습니다."))
    if show_explanation:
        explain_q2()
    return ans

# Q3. 데이터 형 특성 (객관식)
def show_q3():
    _panel(
        "Q3) 객관식: 데이터 형의 기본 특성",
        "다음 중 **올바른 설명**을 고르세요.",
        hint="문자열은 불변, 인덱싱은 0부터."
    )
    display(Markdown(
        "보기\n\n"
        "1) 문자열(str)은 불변(immutable)이다.\n\n"
        "2) 10 + 10.0 의 결과 타입은 int 이다.\n\n"
        "3) 인덱싱은 1부터 시작한다.\n\n"
        "4) '3' + 4 는 7 이 된다."
    ))
def answer_q3(show_explanation: bool = True):
    ans = _ask_until_correct(lambda s: (_matches_any(s, "1", "문자열(str)은 불변(immutable)이다."), "정답은 1번입니다."))
    if show_explanation:
        explain_q3()
    return ans

# Q4. 숫자형 연산식 (주관식)
def show_q4():
    _panel(
        "Q4) 주관식: 숫자형 연산 결과",
        "다음 변수들을 사용하여 식을 계산한 결과값을 숫자로 입력하세요.",
        code=(
            "a = 7\n"
            "b = 10\n"
            "c = 4\n"
            "d = 5\n"
            "e = 3\n\n"
            "# 식: a + b/c - d//2 + e**2"
        ),
        hint="/ 는 실수 나눗셈, // 는 몫(정수 나눗셈), ** 는 거듭제곱"
    )
def answer_q4(show_explanation: bool = True):
    a, b, c, d, e = 7, 10, 4, 5, 3
    expected = a + b/c - d//2 + e**2  # 16.5
    def checker(s):
        try:
            return (float(s.strip()) == expected, f"정답은 {expected} 입니다.")
        except:
            return (False, "숫자로 입력하세요. 예: 16.5")
    ans = _ask_until_correct(checker)
    if show_explanation:
        explain_q4()
    return ans

# Q5. 연산 결과의 타입 (객관식)
def show_q5():
    _panel(
        "Q5) 객관식: 연산 결과의 타입",
        "`10 + 10.0` 의 **결과 타입**으로 알맞은 것은?",
        hint="정수 + 실수 = ?"
    )
    display(Markdown(
        "보기\n\n"
        "1) int\n\n"
        "2) float\n\n"
        "3) str\n\n"
        "4) bool"
    ))
def answer_q5(show_explanation: bool = True):
    ans = _ask_until_correct(lambda s: (_matches_any(s, "2", "float"), "정답은 2) float 입니다."))
    if show_explanation:
        explain_q5()
    return ans

# Q6. 포맷팅
def show_q6():
    _panel(
        "Q6) 문자열 포맷팅",
        "다음 변수를 사용하여 **'Jeju has 4.8 rating.'** 을 출력하는 코드를 작성하세요. (포맷팅 1가지 방식만 쓰면 됩니다)",
        code="city = 'Jeju'\nrating = 4.8\nprint(    )",
        hint="권장: f-string. 예) f\"{변수} ... {변수}\""
    )
def answer_q6(show_explanation: bool = True):
    accepts = [
        'f"{city} has {rating} rating."',
        '"{} has {} rating.".format(city, rating)',
        "'{} has {} rating.'.format(city, rating)"
    ]
    ans = _ask_until_correct(lambda s: (_matches_any(s, *accepts), "예: f\"{city} has {rating} rating.\" 또는 \"{} has {} rating.\".format(city, rating)"))
    if show_explanation:
        explain_q6()
    return ans

# Q8. 문자열의 역변환 (객관식)
def show_q7():
    _panel(
        "Q7) 객관식: str() 변환 후 다시 복원 가능한 경우",
        "다음 중 **str()로 변환 후 다시 원래 타입으로 복원이 가능한 것**을 고르시오.",
        hint="실수(float)는 복원이 가능합니다."
    )
    display(Markdown(
        "보기\n\n"
        "1) float( str(3.14) ) → float\n\n"
        "2) bool( str(True) ) → bool\n\n"
        "3) list( str([1, 2, 3]) ) → list\n\n"
        "4) dict( str({'a': 1}) ) → dict"
    ))

def answer_q7(show_explanation: bool = True):
    def checker(ans):
        a = ans.strip()
        correct = "1"
        return (a == correct,
                "정답은 1) 입니다. float는 str()로 변환 후 다시 복원 가능합니다.")
    result = _ask_until_correct(checker)
    if show_explanation:
        print("Q7 해설:")
        print("1) float( str(3.14) ) ✅ 가능 → '3.14' → 3.14 (실수)")
        print("2) bool( str(True) ) ❌ 'True'라는 문자열은 bool()로 직접 변환 불가, 모든 문자열은 True 처리됨")
        print("3) list( str([1,2,3]) ) ❌ '[1, 2, 3]'은 문자열일 뿐 리스트가 아님 → 변환 불가")
        print("4) dict( str({'a':1}) ) ❌ \"{'a':1}\"은 문자열 → dict()로 변환 불가")
    return result

# Q8. 기본형이 아닌 것 (객관식)
def show_q8():
    _panel(
        "Q8) 객관식: 다음 중 **기본형이 아닌 것**은?",
        "파이썬의 기본형은 숫자형(int, float), 불리안(bool), 문자열(str) 입니다.",
        hint="기본형이 아닌 것 = 컬렉션이나 매핑 같은 복합 자료형"
    )
    display(Markdown(
        "보기\n\n"
        "1) list\n\n"
        "2) int\n\n"
        "3) float\n\n"
        "4) bool\n\n"
        "5) str"
    ))
def answer_q8(show_explanation: bool = True):
    ans = _ask_until_correct(lambda s: (_matches_any(s, "1", "list"), "정답은 1) list 입니다."))
    if show_explanation:
        explain_q8()
    return ans

# Q9. 숫자형 변환 에러 (객관식)
def show_q9():
    _panel(
        "Q9) 객관식: 숫자형 변환 에러",
        "다음 중 **숫자형 변환 함수를 사용하면 에러가 나는 것**은?"
    )
    display(Markdown(
        "보기\n\n"
        "1) int(\"123\")\n\n"
        "2) float(\"3.14\")\n\n"
        "3) int(\"3.14\")\n\n"
        "4) float(\"10\")"
    ))
def answer_q9(show_explanation: bool = True):
    ans = _ask_until_correct(lambda s: (_matches_any(s, "3", "int(\"3.14\")"), "정답은 3) int(\"3.14\") 입니다."))
    if show_explanation:
        explain_q9()
    return ans

# Q10. replace() 메서드 활용
def show_q10():
    _panel(
        "Q10) 객관식: replace() 메서드",
        "다음 코드의 실행 결과로 알맞은 것은?",
        code=(
            "text = 'banana banana banana'\n"
            "print(text.replace('banana', 'apple', 2))"
        ),
        hint="count=2 → 앞에서부터 2번만 바꿉니다."
    )
    display(Markdown(
        "보기\n\n"
        "1) apple apple apple\n\n"
        "2) apple apple banana\n\n"
        "3) apple banana banana\n\n"
        "4) banana banana apple"
    ))

def answer_q10(show_explanation: bool = True):
    def checker(ans):
        return (_matches_any(ans, "2", "apple apple banana"), "정답은 2) apple apple banana 입니다.")
    result = _ask_until_correct(checker)
    if show_explanation:
        print("Q10 해설:")
        print("replace('banana','apple',2)는 앞에서부터 두 번만 'banana'를 'apple'로 바꿉니다.")
        print("따라서 결과는 'apple apple banana' 입니다.")
    return result


# =========================
# 해설 전용 함수들 (업데이트)
# =========================

def explain_q1():
    print("Q1 해설: 문자열 인덱스는 0부터 시작하며, s[0]은 첫 글자를 가리킵니다.")

def explain_q2():
    print("Q2 해설: s[0:3] 은 0~2번째까지 잘라내므로 'Pyt'이 출력됩니다.")
    print("         슬라이싱은 시작 인덱스 포함, 끝 인덱스 미포함 규칙을 기억하세요.")

def explain_q3():
    print("Q3 해설: 데이터 형의 기본 특성")
    print("1) 문자열(str)은 불변(immutable)이다. ✅ 올바른 설명입니다.")
    print("2) 10 + 10.0 의 결과 타입은 int 이다. ❌ 틀림 → 정수 + 실수 = float 이므로 결과는 float입니다.")
    print("3) 인덱싱은 1부터 시작한다. ❌ 틀림 → 파이썬은 0부터 시작합니다.")
    print("4) '3' + 4 는 7 이 된다. ❌ 틀림 → 문자열 '3'과 숫자 4는 더할 수 없어 TypeError가 발생합니다.")

def explain_q4():
    print("Q4 해설: / 는 실수 나눗셈, // 는 몫(정수 나눗셈), ** 는 거듭제곱 연산입니다.")
    print("         a + b/c - d//2 + e**2 = 7 + 10/4 - 2 + 9 = 7 + 2.5 - 2 + 9 = 16.5")

def explain_q5():
    print("Q5 해설: 연산 결과의 타입")
    print("1) int ❌ 틀림 → 정수와 실수를 더하면 결과는 실수입니다.")
    print("2) float ✅ 정답 → 10 + 10.0 = 20.0 으로 float 입니다.")
    print("3) str ❌ 틀림 → 문자열 연산이 아니므로 str 이 될 수 없습니다.")
    print("4) bool ❌ 틀림 → True/False와 관련된 연산이 아니므로 bool 이 아닙니다.")

def explain_q6():
    print("Q6 해설: 문자열 포맷팅")
    print("- f-string: f\"{city} has {rating} rating.\" 처럼 변수값을 직접 삽입할 수 있어 간결합니다.")
    print("- format(): \"{} has {} rating.\".format(city, rating) 도 동일한 결과를 냅니다.")

def explain_q7():
    print("Q7 해설: str() 변환 후 ‘복원 가능’ 판단")
    print("1) float(str(3.14)) ✅ 가능 → '3.14'는 float()로 정확히 3.14로 복원됩니다.")
    print("2) bool(str(True))  ❌ 일반적 복원으로 보지 않습니다.")
    print("   - 이유: bool('무슨문자열이든') 은 비어있지 않으면 항상 True 입니다.")
    print("           예를 들어 bool('False') 도 True 가 되어 의미 보존이 되지 않습니다.")
    print("3) list(str([1, 2, 3])) ❌ '[1, 2, 3]' 은 단순 문자열일 뿐 list 로 파싱되지 않습니다.")
    print("4) dict(str({'a': 1})) ❌ \"{'a': 1}\" 역시 문자열이며 dict()로 변환할 수 없습니다.")

def explain_q8():
    print("Q8 해설: 기본형이 아닌 것")
    print("1) list ✅ 정답 → list는 컬렉션형(복합형)으로 기본형이 아닙니다.")
    print("2) int ❌ 틀림 → 숫자형 기본형입니다.")
    print("3) float ❌ 틀림 → 숫자형 기본형입니다.")
    print("4) bool ❌ 틀림 → 불리안 기본형입니다.")
    print("5) str ❌ 틀림 → 문자열 기본형입니다.")

def explain_q9():
    print("Q9 해설: 숫자형 변환 에러")
    print("1) int('123')   ✅ 정상 → '123' 은 정수 123으로 변환 가능합니다.")
    print("2) float('3.14')✅ 정상 → '3.14' 는 실수 3.14로 변환 가능합니다.")
    print("3) int('3.14')  ❌ 에러 → int()는 소수점 문자열을 직접 변환하지 못해 ValueError 발생.")
    print("4) float('10')  ✅ 정상 → '10' 은 10.0 으로 변환됩니다.")

def explain_q10():
    print("Q10 해설: replace(old, new, count)")
    print("- count를 지정하면 앞에서부터 해당 횟수만 치환합니다.")
    print("- 예제: 'banana banana banana' 에서 2회 치환 → 'apple apple banana'")
    print("- count를 생략하면 전체가 치환됩니다.")


# =========================
# 정답 + 해설 출력 유틸 (가독성 향상)
# =========================
from IPython.display import display, Markdown

def _answer_key() -> dict[int, str]:
    """문항별 정답 요약"""
    return {
        1: "s[0]",
        2: "s[0:3]  (또는 s[:3])",
        3: "1  (문자열은 불변)",
        4: "16.5",
        5: "2  (float)",
        6: 'f"{city} has {rating} rating."  (또는 "{} has {} rating.".format(city, rating))',
        7: "1  (float(str(3.14)) → float)",
        8: "1  (list는 기본형이 아님)",
        9: '3  (int("3.14")는 ValueError)',
        10: "2  (apple apple banana)",
    }

def _explain_func_map():
    """문항별 해설 함수 매핑 (기존 explain_qX 함수를 그대로 활용)"""
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
    """문항 제목 표시용"""
    return f"### Q{qnum} 해설"

def _render_block(title_md: str, answer_text: str | None):
    """Jupyter 노트북에서는 Markdown으로, 콘솔에서는 print로 렌더링"""
    try:
        # Jupyter/Colab 환경: Markdown 렌더
        body = []
        body.append(title_md)
        if answer_text is not None:
            body.append(f"> **정답:** `{answer_text}`  \n")
        display(Markdown("\n\n".join(body)))
    except Exception:
        # 콘솔 환경: 텍스트로 대체
        print(title_md.replace("### ", "").replace("## ", ""))
        if answer_text is not None:
            print(f"[정답] {answer_text}")
        print("-" * 50)

def print_explanation(qnum: int, show_answer: bool = True):
    """
    특정 문항의 '정답 + 해설'을 보기 좋게 출력.
    - show_answer=False 로 주면 해설만 출력.
    """
    answers = _answer_key()
    explains = _explain_func_map()

    if qnum not in explains:
        print(f"Q{qnum} 은(는) 존재하지 않습니다. 1~{max(explains)} 사이로 입력하세요.")
        return

    # 블록 헤더 + 정답
    ans_text = answers.get(qnum) if show_answer else None
    _render_block(_title_of(qnum), ans_text)

    # 실제 해설 실행
    explains[qnum]()

def show_all_explanations(show_answer: bool = True):
    """
    전체 문항의 '정답 + 해설'을 순서대로 출력.
    - show_answer=False 로 주면 해설만 일괄 출력.
    """
    explains = _explain_func_map()
    answers = _answer_key()

    # 전체 헤더
    try:
        display(Markdown("## 📘 Week3 전체 해설"))
    except Exception:
        print("📘 Week3 전체 해설")
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
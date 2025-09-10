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

# Q7. replace() 메서드
def show_q7():
    _panel(
        "Q7) 문자열 메서드",
        "문자열 text = 'I like python' 에서 'python'을 'java'로 바꾸어 출력하는 코드를 작성하세요.",
        code="text = 'I like python'\nprint(    )"
    )
def answer_q7(show_explanation: bool = True):
    ans = _ask_until_correct(lambda s: (_matches_any(s, "text.replace('python','java')"), "힌트: replace(기존,새로운)"))
    if show_explanation:
        explain_q7()
    return ans

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

# Q10. f-string 포맷팅
def show_q10():
    _panel(
        "Q10) 문자열 포맷팅",
        "도시 이름과 평점을 출력하려고 합니다. f-string을 이용하여 'Jeju의 평점은 4.8점입니다.' 를 출력하는 코드를 작성하세요.",
        code="city = 'Jeju'\nrating = 4.8\nprint(    )"
    )
def answer_q10(show_explanation: bool = True):
    ans = _ask_until_correct(lambda s: (_matches_any(s, "f\"{city}의 평점은 {rating}점입니다.\""), "힌트: f-string은 f\"...{변수}...\" 형태입니다."))
    if show_explanation:
        explain_q10()
    return ans

# ====== 프리뷰 전체 보기 (이 10개만) ======
def show_all():
    show_q1(); show_q2(); show_q3(); show_q4(); show_q5()
    show_q6(); show_q7(); show_q8(); show_q9(); show_q10()
    display(Markdown("> 프리뷰가 모두 표시되었습니다. 이제 각 문항의 `answer_qX()`를 실행해서 답만 입력하세요!"))


# =========================
# 해설 전용 함수들
# =========================

def explain_q1():
    print("Q1 해설: 문자열 인덱스는 0부터 시작하며, s[0]은 첫 글자를 가리킵니다.")

def explain_q2():
    print("Q2 해설: s[0:3] 은 0~2번째까지 잘라내므로 'Pyt'이 출력됩니다.")

def explain_q3():
    print("Q3 해설:")
    print("1) 문자열(str)은 불변(immutable)이다. ✅ 올바른 설명입니다.")
    print("2) 10 + 10.0 의 결과 타입은 int 이다. ❌ 틀림 → 정수 + 실수 = float 이므로 결과는 float입니다.")
    print("3) 인덱싱은 1부터 시작한다. ❌ 틀림 → 파이썬은 0부터 시작합니다.")
    print("4) '3' + 4 는 7 이 된다. ❌ 틀림 → 문자열 '3'과 숫자 4는 더할 수 없으므로 TypeError가 발생합니다.")

def explain_q4():
    print("Q4 해설: / 는 실수 나눗셈, // 는 몫, ** 는 제곱 연산이므로 최종 값은 16.5가 됩니다.")

def explain_q5():
    print("Q5 해설: 연산 결과의 타입")
    print("1) int ❌ 틀림 → 정수와 실수를 더하면 결과는 실수입니다.")
    print("2) float ✅ 정답 → 10 + 10.0 = 20.0 으로 float 입니다.")
    print("3) str ❌ 틀림 → 문자열 연산이 아니므로 str 이 될 수 없습니다.")
    print("4) bool ❌ 틀림 → True/False와 관련된 연산이 아니므로 bool 이 아닙니다.\n")

def explain_q6():
    print("Q6 해설: f-string은 가장 직관적이고 간결하며, format()은 중괄호에 변수를 삽입하는 방식입니다.")

def explain_q7():
    print("Q7 해설: replace()는 문자열의 일부를 새 문자열로 치환한 새로운 문자열을 반환합니다.")

def explain_q8():
    print("Q8 해설: 기본형이 아닌 것")
    print("1) list ✅ 정답 → list는 컬렉션형으로 기본형이 아닙니다.")
    print("2) int ❌ 틀림 → 숫자형 기본형입니다.")
    print("3) float ❌ 틀림 → 숫자형 기본형입니다.")
    print("4) bool ❌ 틀림 → 불리안 기본형입니다.")
    print("5) str ❌ 틀림 → 문자열 기본형입니다.\n")

def explain_q9():
    print("Q9 해설: 숫자형 변환 에러")
    print("1) int(\"123\") ✅ 정상 → '123' 은 정수로 변환 가능합니다.")
    print("2) float(\"3.14\") ✅ 정상 → '3.14' 는 실수로 변환 가능합니다.")
    print("3) int(\"3.14\") ❌ 에러 → int()는 소수점 문자열을 직접 변환하지 못해 ValueError 발생.")
    print("4) float(\"10\") ✅ 정상 → '10' 은 10.0 으로 변환됩니다.\n")

def explain_q10():
    print("Q10 해설: f-string을 사용하면 변수 값을 문자열 안에 바로 삽입할 수 있습니다.")


# =========================
# 전체 해설 출력
# =========================
def show_all_explanations():
    explain_q1()
    explain_q2()
    explain_q3()
    explain_q4()
    explain_q5()
    explain_q6()
    explain_q7()
    explain_q8()
    explain_q9()
    explain_q10()
    print("\n✅ 모든 해설이 출력되었습니다.")
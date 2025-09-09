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
def answer_q1():
    return _ask_until_correct(lambda s: (_matches_any(s, "s[0]"), "힌트: 인덱싱은 0부터 시작합니다."))

# Q2. 슬라이싱
def show_q2():
    _panel(
        "Q2) 슬라이싱",
        "문자열 s = 'Python' 에서 'Pyt'을 출력하는 코드를 작성하세요.",
        code="s = 'Python'\nprint(    )"
    )
def answer_q2():
    return _ask_until_correct(lambda s: (_matches_any(s, "s[0:3]", "s[:3]"), "힌트: 끝 인덱스는 포함되지 않습니다."))

# Q3. 음수 인덱싱
def show_q3():
    _panel(
        "Q3) 인덱싱(음수)",
        "문자열 s = 'Python' 에서 마지막 글자를 출력하는 코드를 작성하세요.",
        code="s = 'Python'\nprint(    )"
    )
def answer_q3():
    return _ask_until_correct(lambda s: (_matches_any(s, "s[-1]"), "힌트: 마지막 요소는 -1로 접근합니다."))

# Q4. 문자열 연산
def show_q4():
    _panel(
        "Q4) 문자열 연산",
        "문자열 word1 = 'Hi', word2 = 'Python' 이 있을 때, 'HiPython' 을 출력하는 코드를 작성하세요.",
        code="word1 = 'Hi'\nword2 = 'Python'\nprint(    )"
    )
def answer_q4():
    return _ask_until_correct(lambda s: (_matches_any(s, "word1+word2"), "힌트: + 연산자는 문자열을 이어붙입니다."))

# Q5. 문자열 반복
def show_q5():
    _panel(
        "Q5) 문자열 반복",
        "문자열 word = 'Hi' 를 3번 반복하여 출력하는 코드를 작성하세요.",
        code="word = 'Hi'\nprint(    )"
    )
def answer_q5():
    return _ask_until_correct(lambda s: (_matches_any(s, "word*3"), "힌트: * 연산자는 반복을 의미합니다."))

# Q6. upper() 메서드
def show_q6():
    _panel(
        "Q6) 문자열 메서드",
        "문자열 text = 'python' 을 모두 대문자로 변환해 출력하는 코드를 작성하세요.",
        code="text = 'python'\nprint(    )"
    )
def answer_q6():
    return _ask_until_correct(lambda s: (_matches_any(s, "text.upper()"), "힌트: upper() 메서드를 사용합니다."))

# Q7. replace() 메서드
def show_q7():
    _panel(
        "Q7) 문자열 메서드",
        "문자열 text = 'I like python' 에서 'python'을 'java'로 바꾸어 출력하는 코드를 작성하세요.",
        code="text = 'I like python'\nprint(    )"
    )
def answer_q7():
    return _ask_until_correct(lambda s: (_matches_any(s, "text.replace('python','java')"), "힌트: replace(기존,새로운)"))

# Q8. split() 메서드
def show_q8():
    _panel(
        "Q8) 문자열 메서드",
        "문자열 text = 'python programming' 을 공백 기준으로 분리해 출력하는 코드를 작성하세요.",
        code="text = 'python programming'\nprint(    )"
    )
def answer_q8():
    return _ask_until_correct(lambda s: (_matches_any(s, "text.split()"), "힌트: split()은 기본적으로 공백 기준입니다."))

# Q9. format() 포매팅
def show_q9():
    _panel(
        "Q9) 문자열 포매팅",
        "도시 이름과 방문자 수를 출력하려고 합니다. format()을 이용하여 'Jeju에는 100명이 방문했습니다.' 를 출력하는 코드를 작성하세요.",
        code="city = 'Jeju'\nvisitors = 100\nprint(    )"
    )
def answer_q9():
    return _ask_until_correct(lambda s: (_matches_any(s, "\"{}에는 {}명이 방문했습니다.\".format(city, visitors)"), "힌트: 중괄호 {}에 변수가 들어갑니다."))

# Q10. f-string 포매팅
def show_q10():
    _panel(
        "Q10) 문자열 포매팅",
        "도시 이름과 평점을 출력하려고 합니다. f-string을 이용하여 'Jeju의 평점은 4.8점입니다.' 를 출력하는 코드를 작성하세요.",
        code="city = 'Jeju'\nrating = 4.8\nprint(    )"
    )
def answer_q10():
    return _ask_until_correct(lambda s: (_matches_any(s, "f\"{city}의 평점은 {rating}점입니다.\""), "힌트: f-string은 f\"...{변수}...\" 형태입니다."))
# ====== 프리뷰 전체 보기 (이 10개만) ======
def show_all():
    show_q1(); show_q2(); show_q3(); show_q4(); show_q5()
    show_q6(); show_q7(); show_q8(); show_q9(); show_q10()
    display(Markdown("> 프리뷰가 모두 표시되었습니다. 이제 각 문항의 `answer_qX()`를 실행해서 답만 입력하세요!"))
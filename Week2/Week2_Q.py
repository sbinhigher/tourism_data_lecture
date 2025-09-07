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
# 난이도 하 – 복습 문제 Q1 ~ Q10
# =========================

# Q1. 출력 함수
def show_q1():
    _panel(
        "Q1) 출력 함수",
        "아래 코드의 빈칸에 들어갈 **출력 함수 이름**을 쓰세요.",
        code='_____("Hello Jeju")',
        hint="파이썬에서 화면에 출력할 때 쓰는 내장 함수"
    )
def answer_q1():
    return _ask_until_correct(lambda s: (s.strip() == "print", "정확히 print 라고 입력하세요."))

# Q2. 변수 지정 & 출력
def show_q2():
    _panel(
        "Q2) 변수 지정 & 출력",
        "다음 코드의 **출력 결과**를 정확히 쓰세요.",
        code='city = "Jeju"\nprint(city)'
    )
def answer_q2():
    return _ask_until_correct(lambda s: (s.strip() == "Jeju", "대소문자와 철자를 확인하세요."))

# Q3. 숫자와 문자열 구분 (객관식)
def show_q3():
    _panel(
        "Q3) 객관식: 숫자와 문자열 구분",
        "다음 중 **문자열(string)** 인 것은?",
        hint='따옴표(")로 둘러싸인 값은 문자열입니다.'
    )
    display(Markdown(
        "보기\n\n"
        "1) 10\n\n"
        "2) 3.14\n\n"
        "3) \"10\"\n\n"
        "4) 0"
    ))
def answer_q3():
    def checker(ans):
        a = ans.strip()
        return (_matches_any(a, "3", '"10"', "'10'"), "번호 3 또는 \"10\" 을 입력하세요.")
    return _ask_until_correct(checker)

# Q4. 문자열 연산 (객관식)
def show_q4():
    _panel(
        "Q4) 객관식: 문자열 연산",
        "다음 코드의 **출력 결과**로 알맞은 것은?",
        code='print("10" + "20")'
    )
    display(Markdown(
        "보기\n\n"
        "1) 30\n\n"
        "2) 1020\n\n"
        "3) 오류"
    ))
def answer_q4():
    return _ask_until_correct(lambda s: (_matches_any(s, "2", "1020"), "번호 2 또는 1020 을 입력하세요."))

# Q5. 정수 + 실수 (객관식)
def show_q5():
    _panel(
        "Q5) 객관식: 정수 + 실수",
        "다음 코드의 **출력 결과**로 알맞은 것은?",
        code="print(10 + 10.0)",
        hint="정수 + 실수 → 결과는 실수"
    )
    display(Markdown(
        "보기\n\n"
        "1) 20\n\n"
        "2) 20.0\n\n"
        "3) 오류"
    ))
def answer_q5():
    return _ask_until_correct(lambda s: (_matches_any(s, "2", "20.0"), "번호 2 또는 20.0 을 입력하세요."))

# Q6. 대입(=)과 비교(==) (객관식)
# Q6. 변수명 가능/불가능 (복수정답)
def show_q6():
    _panel(
        "Q6) 객관식(복수선택): 변수명으로 사용할 수 있는 것을 모두 고르시오.",
        "아래 보기 중 **파이썬 변수명으로 사용 가능한 것**을 모두 고르세요. (정답 2개)\n"
        "입력 예시: 1,4  또는  4, 1",
        hint="규칙: 숫자로 시작 X, 하이픈(-) X, 공백 X, 예약어(예: class) X. 영문/숫자/밑줄(_), 그리고 첫 글자는 영문/밑줄."
    )
    display(Markdown(
        "보기\n\n"
        "1) visitor_count\n\n"
        "2) class\n\n"
        "3) 2nd_place\n\n"
        "4) _score2\n\n"
        "5) user-name"
    ))

def answer_q6():
    # 정답: {1, 4}
    correct = {"1", "4"}
    valid_texts = {"visitor_count", "_score2"}

    def parse_choices(s: str):
        # "1,4" / "4, 1" / "1  ,   4" 등 허용
        parts = [p.strip() for p in s.replace(" ", "").split(",") if p.strip()]
        return set(parts)

    def checker(ans):
        a = ans.strip()
        # 번호로 답한 경우
        if any(ch.isdigit() for ch in a):
            chosen = parse_choices(a)
            if chosen == correct:
                return True, ""
            return False, "정답은 2개입니다. 예: 1,4"
        # 텍스트로 답한 경우(둘 다 포함해야 정답)
        lowered = set(" ".join(a.lower().split()).split())
        if valid_texts.issubset(lowered):
            return True, ""
        return False, "번호(예: 1,4) 또는 변수명(visitor_count _score2)을 정확히 입력하세요."

    return _ask_until_correct(checker)

# Q7. 소수 연산 주의 (참/거짓)
def show_q7():
    _panel(
        "Q7) 참/거짓: 소수 연산 주의",
        "다음의 참/거짓을 판단하세요.",
        code="0.1 + 0.2 == 0.3"
    )
def answer_q7():
    def checker(s):
        a = s.strip().lower()
        return (a in {"false", "거짓", "f"}, "정답은 거짓(False) 입니다.")
    return _ask_until_correct(checker)

# Q8. 문자열 반복
def show_q8():
    _panel(
        "Q8) 문자열 반복",
        "다음 코드의 **출력 결과**를 쓰세요.",
        code="print('10' * 3)"
    )
def answer_q8():
    return _ask_until_correct(lambda s: (s.strip() == "101010", "정확히 101010 을 입력하세요."))

# Q9. 노트북 환경의 출력 (참/거짓)
def show_q9():
    _panel(
        "Q9) 참/거짓: 노트북 출력",
        "Colab/Jupyter에서 **마지막 줄에 변수명만 적고 실행**하면, print 없이도 그 변수의 값이 표시된다. (참/거짓)"
    )
def answer_q9():
    def checker(s):
        a = s.strip().lower()
        return (a in {"true", "참", "t"}, "정답은 참(True) 입니다.")
    return _ask_until_correct(checker)

# Q10. 데이터 타입 함수 활용 (print_type)
# Q10. print의 구분자 파라미터
def show_q10():
    _panel(
        "Q10) 객관식: print 함수의 구분자 파라미터",
        "다음 중 **print**에서 여러 값을 출력할 때 **값 사이에 들어갈 구분자**를 지정하는 파라미터 이름은?"
    )
    display(Markdown(
        "보기\n\n"
        "1) sep\n\n"
        "2) end\n\n"
        "3) seq\n\n"
        "4) delimiter\n\n"
        "5) split"
    ))

def answer_q10():
    # 정답: 1) sep
    return _ask_until_correct(
        lambda s: (_matches_any(s, "1", "sep"), "번호 1 또는 'sep' 를 입력하세요.")
    )

# ====== 프리뷰 전체 보기 (이 10개만) ======
def show_all():
    show_q1(); show_q2(); show_q3(); show_q4(); show_q5()
    show_q6(); show_q7(); show_q8(); show_q9(); show_q10()
    display(Markdown("> 프리뷰가 모두 표시되었습니다. 이제 각 문항의 `answer_qX()`를 실행해서 답만 입력하세요!"))
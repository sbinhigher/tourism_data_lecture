
# -*- coding: utf-8 -*-
# Week5_Q.py : 제어문/반복문 과제 (if, 한줄 if, for, while, enumerate, zip, 들여쓰기, 무한루프)
from IPython.display import display, HTML, Markdown
import sys

# ====== 글로벌 아이콘 (사용자 커스터마이즈 가능) ======
CORRECT_ICON = "✅"
WRONG_ICON   = "❌"

def set_icons(correct="✅", wrong="❌"):
    global CORRECT_ICON, WRONG_ICON
    CORRECT_ICON, WRONG_ICON = correct, wrong

# ====== 프리뷰 패널 공통 렌더러 ======
PANEL_CSS = """
<style>
.wq-panel {border:1px solid #e5e7eb;border-radius:8px;margin:12px 0;padding:12px;background:#fafafa;}
.wq-title {font-weight:700;margin:0 0 6px 0;}
.wq-body  {margin:6px 0;}
.wq-code  {background:#0b1021;color:#eaeefb;padding:10px;border-radius:6px;white-space:pre;overflow:auto;font-family:ui-monospace,SFMono-Regular,Menlo,Monaco,Consolas,"Liberation Mono","Courier New",monospace;}
.wq-note  {color:#374151;font-size:0.9em;}
</style>
"""

def _panel(title: str, body: str, code: str = None):
    html = [PANEL_CSS, '<div class="wq-panel">', f'<div class="wq-title">{title}</div>']
    html.append(f'<div class="wq-body">{body}</div>')
    if code is not None:
        from html import escape
        html.append(f'<div class="wq-code">{escape(code)}</div>')
    html.append('</div>')
    display(HTML("".join(html)))

# ====== 인터랙션 유틸 ======
def _ask_until_correct(checker, prompt="정답을 입력하세요: "):
    while True:
        try:
            s = input(prompt).strip()
        except EOFError:
            # 노트북 환경이 아니어도 동작하게 — 표준 입력이 없으면 종료
            print("입력이 지원되지 않는 환경입니다.")
            return False
        ok, msg = checker(s)
        icon = CORRECT_ICON if ok else WRONG_ICON
        print(icon, msg)
        if ok:
            return True

def _matches_any(s, *alts):
    s_norm = s.strip().lower().replace(" ", "")
    for a in alts:
        a_norm = str(a).strip().lower().replace(" ", "")
        if s_norm == a_norm:
            return True
    return False

# ====== 문제 1~10 (이론 1, 객/주관 혼합) ======
# 1) 이론 객관식 — 들여쓰기
def show_q1():
    _panel(
        "Q1) 객관식(이론) — 파이썬의 코드 블록 구분 방식",
        "다음 중 파이썬에서 **코드 블록을 구분**하는 방식으로 옳은 것은?",
        code="1) 중괄호 {}\n2) 세미콜론 ;\n3) 들여쓰기(Indentation)\n4) 괄호 ()"
    )

def explain_q1():
    display(Markdown("- 정답: **3**\n- 파이썬은 들여쓰기로 코드 블록을 구분합니다."))

def answer_q1(show_explanation: bool=True):
    ok = _ask_until_correct(lambda s: (_matches_any(s, "3"), "정답은 3) 들여쓰기 입니다."))
    if show_explanation: explain_q1()
    return ok

# 2) if 구조 OX (객관식)
def show_q2():
    _panel(
        "Q2) 객관식 — if/elif/else 구조",
        "다음 중 if문 구조에 대한 설명으로 **틀린 것**은?",
        code="1) elif는 여러 개 사용할 수 있다.\n2) else는 선택적으로 사용할 수 있다.\n3) if는 조건이 참일 때만 실행된다.\n4) 모든 if문에는 반드시 else가 있어야 한다."
    )

def explain_q2():
    display(Markdown("- 정답: **4**\n- `else`는 필수가 아니라 선택입니다."))

def answer_q2(show_explanation: bool=True):
    ok = _ask_until_correct(lambda s: (_matches_any(s, "4"), "정답은 4) 입니다."))
    if show_explanation: explain_q2()
    return ok

# 3) 한 줄 if (주관식)
def show_q3():
    _panel(
        "Q3) 주관식 — 한 줄 if문(조건 표현식)",
        "다음 조건문을 **한 줄로** 표현하세요.",
        code="if age >= 20:\n    result = \"성인\"\nelse:\n    result = \"미성년자\""
    )

def explain_q3():
    display(Markdown("- 예시 정답: `result = \"성인\" if age >= 20 else \"미성년자\"`"))

def answer_q3(show_explanation: bool=True):
    def checker(s):
        ok = ("if" in s) and ("else" in s) and ("성인" in s) and ("미성년자" in s)
        return ok, "예시: result = \"성인\" if age >= 20 else \"미성년자\""
    ok = _ask_until_correct(checker)
    if show_explanation: explain_q3()
    return ok

# 4) for-range 결과 (객관식)
def show_q4():
    _panel(
        "Q4) 객관식 — for + range 결과",
        "다음 코드의 출력 결과는 무엇입니까?",
        code="for i in range(2, 7, 2):\n    print(i, end=' ')"
    )

def explain_q4():
    display(Markdown("- 정답: **2 4 6**"))

def answer_q4(show_explanation: bool=True):
    ok = _ask_until_correct(lambda s: (_matches_any(s, "2 4 6", "2,4,6", "246"), "정답은 2 4 6 입니다."))
    if show_explanation: explain_q4()
    return ok

# 5) enumerate 빈칸 (주관식)
def show_q5():
    _panel(
        "Q5) 주관식 — enumerate로 인덱스와 값 동시 출력",
        "빈칸을 채워 코드를 완성하세요.",
        code="fruits = [\"apple\", \"banana\", \"cherry\"]\nfor ____, ____ in enumerate(fruits, start=1):\n    print(____, ____)"
    )

def explain_q5():
    display(Markdown("- 예시 정답: `idx, name`"))

def answer_q5(show_explanation: bool=True):
    def checker(s):
        normalized = s.replace(" ", "")
        ok = normalized in {"idx,name", "i,name", "index,name", "k,v", "a,b"}
        return ok, "예: idx, name"
    ok = _ask_until_correct(checker, prompt="두 변수명을 콤마로 구분해 입력: ")
    if show_explanation: explain_q5()
    return ok

# 6) zip 개념 (객관식)
def show_q6():
    _panel(
        "Q6) 객관식 — zip 함수 설명",
        "다음 중 zip() 함수의 설명으로 옳은 것은?",
        code="1) 여러 시퀀스를 병렬로 순회한다.\n2) 길이가 다르면 반드시 오류가 난다.\n3) 항상 가장 긴 시퀀스 기준으로 순회한다.\n4) 문자열에는 사용할 수 없다."
    )

def explain_q6():
    display(Markdown("- 정답: **1**\n- zip은 여러 시퀀스를 병렬로 순회하며 기본적으로 **가장 짧은 길이**에 맞춰 잘립니다."))

def answer_q6(show_explanation: bool=True):
    ok = _ask_until_correct(lambda s: (_matches_any(s, "1"), "정답은 1) 입니다."))
    if show_explanation: explain_q6()
    return ok

# 7) while 결과 (객관식)
def show_q7():
    _panel(
        "Q7) 객관식 — while 반복 결과",
        "다음 코드의 출력 결과는 무엇입니까?",
        code="n = 1\nwhile n < 4:\n    print(n)\n    n += 1"
    )

def explain_q7():
    display(Markdown("- 정답: **1 2 3** (줄바꿈으로 출력됨)"))

def answer_q7(show_explanation: bool=True):
    ok = _ask_until_correct(lambda s: (_matches_any(s, "1 2 3", "1,2,3", "123"), "정답은 1 2 3 입니다."))
    if show_explanation: explain_q7()
    return ok

# 8) 무한 루프 방지 (주관식)
def show_q8():
    _panel(
        "Q8) 주관식 — 무한 루프를 방지하려면?",
        "다음 while문이 무한 루프가 되지 않도록 필요한 조치를 서술하세요.",
        code="count = 1\nwhile count <= 3:\n    print(count)\n    # 여기에 무엇이 필요할까요?"
    )

def explain_q8():
    display(Markdown("- 예시: 반복 변수 갱신 (예: `count += 1`)"))

def answer_q8(show_explanation: bool=True):
    def checker(s):
        ok = ("+=" in s and "count" in s) or ("증가" in s) or ("갱신" in s)
        return ok, "예: count += 1"
    ok = _ask_until_correct(checker)
    if show_explanation: explain_q8()
    return ok

# 9) 들여쓰기 판별 (객관식)
def show_q9():
    _panel(
        "Q9) 객관식 — 들여쓰기 차이에 따른 결과",
        "다음 두 코드 중, \"수고하셨습니다.\"가 **조건과 무관하게 항상 실행**되는 것은?",
        code="A)\nif score >= 60:\n    print(\"합격입니다.\")\nprint(\"수고하셨습니다.\")\n\nB)\nif score >= 60:\n    print(\"합격입니다.\")\n    print(\"수고하셨습니다.\")"
    )

def explain_q9():
    display(Markdown("- 정답: **A** — 두 번째 print가 if 블록 **밖**에 있습니다."))

def answer_q9(show_explanation: bool=True):
    ok = _ask_until_correct(lambda s: (_matches_any(s, "A", "a"), "정답은 A 입니다."))
    if show_explanation: explain_q9()
    return ok

# 10) 누적 변수 초기화 위치 (주관식)
def show_q10():
    _panel(
        "Q10) 주관식 — for문에서 누적 변수를 어디서 초기화해야 하나요?",
        "아래 코드는 의도와 다르게 동작합니다. **왜 그런지**와 **어떻게 고칠지**를 서술하세요.",
        code="nums = [1, 2, 3]\nfor n in nums:\n    total = 0\n    total += n\nprint(total)"
    )

def explain_q10():
    display(Markdown("- `total`을 반복문 **밖에서 한 번만** 초기화해야 합니다. 현재는 매 반복마다 0으로 리셋되어 마지막 값만 남습니다."))

def answer_q10(show_explanation: bool=True):
    def checker(s):
        ok = ("반복문 밖" in s) or ("밖에서" in s) or ("outside" in s) or ("한 번만" in s)
        return ok, "핵심: 누적 변수는 반복 **전**에 한 번만 초기화"
    ok = _ask_until_correct(checker)
    if show_explanation: explain_q10()
    return ok

# ====== 일괄 미리보기 / 답안 요약 ======
def show_all():
    show_q1(); show_q2(); show_q3(); show_q4(); show_q5()
    show_q6(); show_q7(); show_q8(); show_q9(); show_q10()
    display(Markdown("> 모든 문제 프리뷰가 표시되었습니다."))

def answers_brief():
    return {
        1: "3",
        2: "4",
        3: 'result = "성인" if age >= 20 else "미성년자"',
        4: "2 4 6",
        5: "idx, name",
        6: "1",
        7: "1 2 3",
        8: "count += 1 (반복 변수 갱신)",
        9: "A",
        10:"누적 변수는 반복문 밖에서 초기화"
    }

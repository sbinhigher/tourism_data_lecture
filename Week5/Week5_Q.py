# -*- coding: utf-8 -*-
# Week5_Q.py : 제어문/반복문 + 라이브러리 기초 (Q8~Q10: 라이브러리 이론)
# - Week4 스타일 UI 유지, 숫자/기호/한글 입력 정규화
# - 오답 시 정답 미노출, 재시도 가능

from IPython.display import display, HTML, Markdown
import re

CORRECT_ICON = "✅"
WRONG_ICON   = "❌"

def set_icons(correct="✅", wrong="❌"):
    global CORRECT_ICON, WRONG_ICON
    CORRECT_ICON, WRONG_ICON = correct, wrong

RENDER_STYLE = "week4"  # "week4" | "panel"
def set_style(style: str = "week4"):
    global RENDER_STYLE
    if style not in {"week4", "panel"}:
        style = "week4"
    RENDER_STYLE = style

PANEL_CSS = """
<style>
.wq-panel {border:1px solid #e5e7eb;border-radius:8px;margin:12px 0;padding:12px;background:#fafafa;}
.wq-title {font-weight:700;margin:0 0 6px 0;}
.wq-body  {margin:6px 0;}
.wq-code  {background:#0b1021;color:#eaeefb;padding:10px;border-radius:6px;white-space:pre;overflow:auto;font-family:ui-monospace,Consolas,monospace;}
</style>
"""
def _panel(title: str, body: str, code: str = None):
    html = [PANEL_CSS, '<div class="wq-panel">', f'<div class="wq-title">{title}</div>']
    html.append(f'<div class="wq-body">{body}</div>')
    if code is not None:
        from html import escape
        html.append(f'<div class="wq-code">{escape(code)}</div>')
    html.append("</div>")
    display(HTML("".join(html)))

STYLE_WEEK4 = """
<style>
.qbox{border:1px solid #e5e7eb;border-radius:10px;padding:14px 16px;margin:14px 0;background:#fff;}
.qtitle{font-weight:700;font-size:1.05rem;margin-bottom:6px;}
.qstem{margin:6px 0 10px 0;}
.qchoices{margin:8px 0 0 22px;}
.qchoices li{margin:4px 0;}
.qlabel{display:inline-block;margin-top:6px;color:#6b7280;font-size:0.9rem}
.qcode{background:#0b1021;color:#eaeefb;padding:10px;border-radius:6px;white-space:pre-wrap;overflow:auto;font-family:ui-monospace,Consolas,monospace;}
</style>
"""
def _render_week4(qid: int, title: str, body: str, code: str = None):
    choices = []
    if code:
        for line in code.splitlines():
            m = re.match(r"\s*(\d+)\)\s*(.+)$", line.strip())
            if m:
                choices.append((m.group(1), m.group(2)))
    html = [STYLE_WEEK4, '<div class="qbox">', f'<div class="qtitle">Q{qid}</div>', f'<div class="qstem">{body}</div>']
    if choices:
        html.append('<div class="qlabel">보기</div>')
        html.append('<ol class="qchoices">')
        for n, txt in choices:
            html.append(f"<li>{txt}</li>")
        html.append("</ol>")
    elif code:
        from html import escape
        html.append(f'<div class="qcode">{escape(code)}</div>')
    html.append("</div>")
    display(HTML("".join(html)))

def _normalize_choice(s: str) -> str:
    if s is None:
        return ""
    s = s.strip()
    circled = {"①":"1","②":"2","③":"3","④":"4","⑤":"5"}
    for k, v in circled.items():
        s = s.replace(k, v)
    s = s.replace("번", "").replace(")", "").replace(".", "")
    m = re.match(r"^\s*(\d+)\s*$", s)
    if m:
        return m.group(1)
    return s.strip().lower().replace(" ", "")

def _ask_until_correct(checker, prompt="정답을 입력하세요: "):
    while True:
        try:
            s = input(prompt).strip()
        except EOFError:
            print("입력이 지원되지 않는 환경입니다.")
            return False
        ok = bool(checker(s))
        print(CORRECT_ICON + " 정답입니다." if ok else WRONG_ICON + " 오답입니다. 다시 시도해보세요.")
        if ok:
            return True

def _matches_any_text(s, *alts):
    s_norm = (s or "").strip().lower().replace(" ", "")
    for a in alts:
        a_norm = str(a).strip().lower().replace(" ", "")
        if s_norm == a_norm:
            return True
    return False

Q = {
    1: dict(
        kind="mcq_theory",
        title="Q1) 객관식(이론) — 파이썬의 코드 블록 구분 방식",
        body="다음 중 파이썬에서 코드 블록을 구분하는 방식으로 옳은 것은?",
        code="1) 중괄호 {}\n2) 세미콜론 ;\n3) 들여쓰기(Indentation)\n4) 괄호 ()",
        checker=lambda s: (_normalize_choice(s) == "3") or _matches_any_text(s, "들여쓰기", "indentation", "indent"),
        explain="정답: 3\n파이썬은 들여쓰기로 코드 블록을 구분합니다."
    ),
    2: dict(
        kind="mcq",
        title="Q2) 객관식 — if/elif/else 구조",
        body="다음 중 if문 구조에 대한 설명으로 틀린 것은?",
        code="1) elif는 여러 개 사용할 수 있다.\n2) else는 선택적으로 사용할 수 있다.\n3) if는 조건이 참일 때만 실행된다.\n4) 모든 if문에는 반드시 else가 있어야 한다.",
        checker=lambda s: _normalize_choice(s) == "4",
        explain="정답: 4\nelse는 필수가 아니라 선택입니다."
    ),
    3: dict(
        kind="short",
        title="Q3) 주관식 — 한 줄 if문(조건 표현식)",
        body="다음 조건문을 한 줄로 표현하세요.",
        code="if age >= 20:\n    result = \"성인\"\nelse:\n    result = \"미성년자\"",
        checker=lambda s: ("if" in s) and ("else" in s) and ("성인" in s) and ("미성년자" in s),
        explain="예시 정답: result = \"성인\" if age >= 20 else \"미성년자\""
    ),
    4: dict(
        kind="mcq",
        title="Q4) 객관식 — for + range 결과",
        body="다음 코드의 출력 결과는 무엇입니까?",
        code="for i in range(2, 7, 2):\n    print(i, end=' ')",
        checker=lambda s: _matches_any_text(s, "2 4 6", "2,4,6", "2-4-6", "246"),
        explain="정답: 2 4 6"
    ),
    5: dict(
        kind="short",
        title="Q5) 주관식 — enumerate로 인덱스와 값 동시 출력",
        body="빈칸을 채워 코드를 완성하세요.",
        code="fruits = [\"apple\", \"banana\", \"cherry\"]\nfor ____, ____ in enumerate(fruits, start=1):\n    print(____, ____)",
        checker=lambda s: s.replace(" ", "") in {"idx,name", "i,name", "index,name", "k,v", "a,b"},
        prompt="두 변수명을 콤마로 구분해 입력: ",
        explain="예시 정답: idx, name"
    ),
    6: dict(
        kind="mcq",
        title="Q6) 객관식 — while에서 무한 루프 탈출",
        body="다음 while문에서 무한 루프를 깨기 위해 빈칸(_____)에 들어갈 구문을 고르시오.<div class=\"qcode\">i = 0\nwhile True:\n    i += 1\n    if i > 5:\n        _____\n    print(i)</div>",
        code="1) break\n2) continue\n3) pass\n4) raise SystemExit",
        checker=lambda s: _normalize_choice(s) == "1",
        explain="정답: 1) break\nbreak는 가장 안쪽 반복문을 즉시 종료합니다. continue는 이번 반복만 건너뜁니다. pass는 아무 동작도 하지 않습니다. raise SystemExit는 프로그램 종료 예외입니다."
    ),
    7: dict(
        kind="mcq",
        title="Q7) 객관식 — while 반복 결과",
        body="다음 코드의 출력 결과는 무엇입니까?",
        code="n = 1\nwhile n < 4:\n    print(n)\n    n += 1",
        checker=lambda s: _matches_any_text(s, "1 2 3", "1,2,3", "123"),
        explain="정답: 1 2 3 (줄바꿈)"
    ),
    8: dict(
        kind="mcq",
        title="Q8) 객관식(이론) — import와 불러오기",
        body="다음 중 설명으로 틀린 것은?",
        code=(
            "1) 일반적으로 설치가 완료된 라이브러리는 import 문을 통해 코드 내에서 불러와 사용한다.\n"
            "2) Python에서는 특정 모듈 전체 또는 일부만 선택적으로 불러올 수 있다.\n"
            "3) 라이브러리 명이 긴 경우에는 약어(Alias)를 지정하여 간결하게 사용할 수 있다.\n"
            "4) from 문은 모듈 전체만 불러올 수 있으며 일부 구성요소만 선택적으로 불러오는 것은 불가능하다."
        ),
        checker=lambda s: _normalize_choice(s) == "4",
        explain="정답: 4\nfrom 문은 일부 구성요소만 선택적으로 불러올 수 있습니다. 예: from numpy import array, mean 또는 from numpy import random as rnd"
    ),
    9: dict(
        kind="mcq",
        title="Q9) 객관식 — pandas describe로 확인할 수 없는 통계",
        body="다음 중 pandas.DataFrame.describe()의 기본 출력(수치형 기준)에 포함되지 않는 것은?",
        code="1) 분산(variance)\n2) 평균(mean)\n3) 표준편차(std)\n4) 사분위수(25%와 75%)",
        checker=lambda s: _normalize_choice(s) == "1",
        explain="정답: 1\ndescribe 기본 수치형 출력: count, mean, std, min, 25%, 50%(median), 75%, max. 분산(var)은 포함되지 않습니다."
    ),
    10: dict(
        kind="mcq",
        title="Q10) 객관식 — NumPy 함수와 기능의 짝이 잘못된 것은?",
        body="다음 중 함수와 설명의 짝이 잘못된 것은?",
        code="1) 평균(mean): np.mean(a)\n2) 분산(variance, 표본): np.var(a, ddof=0)\n3) 사분위수범위(IQR): np.percentile(a,75) - np.percentile(a,25)\n4) 범위(range): np.max(a) - np.min(a)",
        checker=lambda s: _normalize_choice(s) == "2",
        explain="정답: 2\n표본 분산은 ddof=1, 모집단 분산은 ddof=0을 사용합니다."
    ),
}

def show(qid: int):
    q = Q[qid]
    title, body, code = q["title"], q["body"], q.get("code")
    if RENDER_STYLE == "week4":
        _render_week4(qid, title, body, code)
    else:
        _panel(title, body, code)

def explain(qid: int):
    q = Q[qid]
    display(Markdown(q["explain"]))

def answer(qid: int, show_explanation: bool=True):
    q = Q[qid]
    prompt = q.get("prompt", "정답을 입력하세요: ")
    ok = _ask_until_correct(q["checker"], prompt=prompt)
    if show_explanation:
        explain(qid)
    return ok

def show_all():
    for i in range(1, len(Q)+1):
        show(i)
    display(Markdown("> 모든 문제 프리뷰가 표시되었습니다."))

def answers_brief():
    return {
        1: "3 (들여쓰기)",
        2: "4",
        3: 'result = "성인" if age >= 20 else "미성년자"',
        4: "2 4 6",
        5: "idx, name",
        6: "1 (break)",
        7: "1 2 3",
        8: "4",
        9: "1",
        10:"2"
    }

def _mk_show(qid):    return lambda : show(qid)
def _mk_answer(qid):  return lambda show_explanation=True: answer(qid, show_explanation)
def _mk_explain(qid): return lambda : explain(qid)

for _i in range(1, 10+1):
    globals()[f"show_q{_i}"]    = _mk_show(_i)
    globals()[f"answer_q{_i}"]  = _mk_answer(_i)
    globals()[f"explain_q{_i}"] = _mk_explain(_i)

# 끝

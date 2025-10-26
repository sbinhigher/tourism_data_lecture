# -*- coding: utf-8 -*-
# Week5_Q.py : 제어문/반복문 과제 (if, 한줄 if, for, while, enumerate, zip, 들여쓰기, 무한루프)
# 기능별 배치: 상수/스타일 → 공용 유틸 → 문제 레지스트리 → 공용 API → 호환 래퍼

from IPython.display import display, HTML, Markdown
import re

CORRECT_ICON = "✅"
WRONG_ICON   = "❌"

def set_icons(correct="✅", wrong="❌"):
    global CORRECT_ICON, WRONG_ICON
    CORRECT_ICON, WRONG_ICON = correct, wrong

RENDER_STYLE = "week4"
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
    html = [STYLE_WEEK4, '<div class="qbox">',
            f'<div class="qtitle">Q{qid}</div>',
            f'<div class="qstem">{body}</div>']
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
        body="다음 중 파이썬에서 **코드 블록을 구분**하는 방식으로 옳은 것은?",
        code="1) 중괄호 {}\n2) 세미콜론 ;\n3) 들여쓰기(Indentation)\n4) 괄호 ()",
        checker=lambda s: (_normalize_choice(s) == "3") or _matches_any_text(s, "들여쓰기", "indentation", "indent"),
        explain="- 정답: **3**\n- 파이썬은 들여쓰기로 코드 블록을 구분합니다."
    ),
    2: dict(
        kind="mcq",
        title="Q2) 객관식 — if/elif/else 구조",
        body="다음 중 if문 구조에 대한 설명으로 **틀린 것**은?",
        code="1) elif는 여러 개 사용할 수 있다.\n2) else는 선택적으로 사용할 수 있다.\n3) if는 조건이 참일 때만 실행된다.\n4) 모든 if문에는 반드시 else가 있어야 한다.",
        checker=lambda s: _normalize_choice(s) == "4",
        explain="- 정답: **4**\n- `else`는 필수가 아니라 선택입니다."
    ),
    3: dict(
        kind="short",
        title="Q3) 주관식 — 한 줄 if문(조건 표현식)",
        body="다음 조건문을 **한 줄로** 표현하세요.",
        code="if age >= 20:\n    result = \"성인\"\nelse:\n    result = \"미성년자\"",
        checker=lambda s: ("if" in s) and ("else" in s) and ("성인" in s) and ("미성년자" in s),
        explain="- 예시 정답: `result = \"성인\" if age >= 20 else \"미성년자\"`"
    ),
    4: dict(
        kind="mcq",
        title="Q4) 객관식 — for + range 결과",
        body="다음 코드의 출력 결과는 무엇입니까?",
        code="for i in range(2, 7, 2):\n    print(i, end=' ')",
        checker=lambda s: _matches_any_text(s, "2 4 6", "2,4,6", "2-4-6", "246"),
        explain="- 정답: **2 4 6**"
    ),
    5: dict(
        kind="short",
        title="Q5) 주관식 — enumerate로 인덱스와 값 동시 출력",
        body="빈칸을 채워 코드를 완성하세요.",
        code="fruits = [\"apple\", \"banana\", \"cherry\"]\nfor ____, ____ in enumerate(fruits, start=1):\n    print(____, ____)",
        checker=lambda s: s.replace(" ", "") in {"idx,name", "i,name", "index,name", "k,v", "a,b"},
        prompt="두 변수명을 콤마로 구분해 입력: ",
        explain="- 예시 정답: `idx, name`"
    ),
    6: dict(
        kind="mcq",
        title="Q6) 객관식 — while에서 무한 루프 탈출",
        body="다음 `while`문에서 **무한 루프를 깨기 위해** 빈칸(`_____`)에 들어갈 구문을 고르시오.<div class=\"qcode\">i = 0\nwhile True:\n    i += 1\n    if i > 5:\n        _____\n    print(i)</div>",
        code="1) break\n2) continue\n3) pass\n4) raise SystemExit",
        checker=lambda s: _normalize_choice(s) == "1",
        explain="- 정답: **1) break**\n- `break`는 가장 안쪽 반복문을 **즉시 종료**합니다.\n- `continue`는 이번 반복만 건너뛰며, `pass`는 아무 동작도 하지 않습니다.\n- `raise SystemExit`는 프로그램 종료 예외를 발생시키며, 보통 반복문 제어용으로 사용하지 않습니다."
    ),
    7: dict(
        kind="mcq",
        title="Q7) 객관식 — while 반복 결과",
        body="다음 코드의 출력 결과는 무엇입니까?",
        code="n = 1\nwhile n < 4:\n    print(n, end = ' ')\n    n += 1",
        checker=lambda s: _matches_any_text(s, "1 2 3", "1 2 3 "),
        explain="- 정답: **1 2 3**"
    ),
    8: dict(
        kind="mcq",
        title="Q8) 객관식(이론) — 라이브러리의 특성",
        body="다음 중 라이브러리의 특성에 대한 설명으로 잘못된 것은?",
        code="1) 공통 기능을 모듈화해 재사용성을 높인다.\n2) 검증된 구현을 제공해 생산성과 신뢰성을 높인다.\n3) 도메인별 고수준 API를 제공해 개발 복잡도를 낮춘다.\n4) 모든 라이브러리는 파이썬 인터프리터에 기본 포함되어 별도 설치가 필요 없다.",
        checker=lambda s: _normalize_choice(s) == "4",
        explain="정답: 4\n표준 라이브러리가 아닌 외부 라이브러리는 보통 pip/conda로 설치가 필요하다."
    ),
    9: dict(
        kind="mcq",
        title="Q9) 객관식 — pandas describe로 확인할 수 없는 통계",
        body="다음 중 pandas.DataFrame.describe()의 기본 출력(수치형 기준)에 포함되지 않는 것은?",
        code="1) 분산(variance)\n2) 평균(mean)\n3) 표준편차(std)\n4) 사분위수(25%와 75%)",
        checker=lambda s: _normalize_choice(s) == "1",
        explain="정답: 1\n기본 출력은 count, mean, std, min, 25%, 50%(median), 75%, max이며, 분산(var)은 포함되지 않는다."
    ),
    10: dict(
        kind="mcq",
        title="Q10) 객관식 — NumPy 함수와 기능의 짝짓기",
        body="다음 중 함수와 설명의 짝이 잘못된 것은?",
        code="1) np.arange(n): 0부터 n-1까지 1 간격의 배열 생성\n2) np.linspace(a, b, k): 구간 [a, b]를 k등분한 실수 배열 생성\n3) np.unique(x, return_counts=True): 고유값과 각 값의 개수 반환\n4) np.reshape(x, newshape): 배열을 무작위 순서로 섞는다",
        checker=lambda s: _normalize_choice(s) == "4",
        explain="정답: 4\nnp.reshape는 모양만 바꾸며, 섞으려면 np.random.shuffle 또는 np.random.permutation을 사용한다."
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
        8: "count += 1 (반복 변수 갱신)",
        9: "A",
        10:"누적 변수는 반복문 밖에서 초기화"
    }

def _mk_show(qid):    return lambda : show(qid)
def _mk_answer(qid):  return lambda show_explanation=True: answer(qid, show_explanation)
def _mk_explain(qid): return lambda : explain(qid)

for _i in range(1, 10+1):
    globals()[f"show_q{_i}"]    = _mk_show(_i)
    globals()[f"answer_q{_i}"]  = _mk_answer(_i)
    globals()[f"explain_q{_i}"] = _mk_explain(_i)

# 끝
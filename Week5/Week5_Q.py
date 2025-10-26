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
        res = checker(s)
        ok = bool(res)
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
        title="Q6) 객관식 — zip 함수 설명",
        body="다음 중 zip() 함수의 설명으로 옳은 것은?",
        code="1) 여러 시퀀스를 병렬로 순회한다.\n2) 길이가 다르면 반드시 오류가 난다.\n3) 항상 가장 긴 시퀀스 기준으로 순회한다.\n4) 문자열에는 사용할 수 없다.",
        checker=lambda s: _normalize_choice(s) == "1",
        explain="- 정답: **1**\n- zip은 여러 시퀀스를 병렬로 순회하며 기본적으로 **가장 짧은 길이**에 맞춰 잘립니다."
    ),
    7: dict(
        kind="mcq",
        title="Q7) 객관식 — while 반복 결과",
        body="다음 코드의 출력 결과는 무엇입니까?",
        code="n = 1\nwhile n < 4:\n    print(n)\n    n += 1",
        checker=lambda s: _matches_any_text(s, "1 2 3", "1,2,3", "123"),
        explain="- 정답: **1 2 3** (줄바꿈으로 출력됨)"
    ),
    8: dict(
        kind="short",
        title="Q8) 주관식 — 무한 루프를 방지하려면?",
        body="다음 while문이 무한 루프가 되지 않도록 필요한 조치를 서술하세요.",
        code="count = 1\nwhile count <= 3:\n    print(count)\n    # 여기에 무엇이 필요할까요?",
        checker=lambda s: (("+=" in s and "count" in s) or ("증가" in s) or ("갱신" in s)),
        explain="- 예시: 반복 변수 갱신 (예: `count += 1`)"
    ),
    9: dict(
        kind="mcq",
        title="Q9) 객관식 — 들여쓰기 차이에 따른 결과",
        body='다음 두 코드 중, `"수고하셨습니다."`가 **조건과 무관하게 항상 실행**되는 것은?',
        code="A)\nif score >= 60:\n    print(\"합격입니다.\")\nprint(\"수고하셨습니다.\")\n\nB)\nif score >= 60:\n    print(\"합격입니다.\")\n    print(\"수고하셨습니다.\")",
        checker=lambda s: _matches_any_text(s, "a"),
        explain="- 정답: **A** — 두 번째 print가 if 블록 **밖**에 있습니다."
    ),
    10: dict(
        kind="short",
        title="Q10) 주관식 — for문에서 누적 변수를 어디서 초기화해야 하나요?",
        body="아래 코드는 의도와 다르게 동작합니다. **왜 그런지**와 **어떻게 고칠지**를 서술하세요.",
        code="nums = [1, 2, 3]\nfor n in nums:\n    total = 0\n    total += n\nprint(total)",
        checker=lambda s: (("반복문 밖" in s) or ("밖에서" in s) or ("outside" in s) or ("한 번만" in s)),
        explain="- `total`을 반복문 **밖에서 한 번만** 초기화해야 합니다. 현재는 매 반복마다 0으로 리셋되어 마지막 값만 남습니다."
    ),
}

def show(qid: int):
    q = Q[qid]
    _panel(q["title"], q["body"], q.get("code"))

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
        6: "1",
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
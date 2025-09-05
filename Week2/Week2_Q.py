# -*- coding: utf-8 -*-
# Jupyter/콘솔 겸용 모듈: 프리뷰 패널 + 답안 입력 분리, 아이콘 커스터마이즈, 16문항
from IPython.display import display, HTML, Markdown
import math
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

def _panel(title: str, body_md: str, code: str|None=None, hint: str|None=None):
    html = [PANEL_CSS, '<div class="quiz-panel">']
    html += [f'<div class="quiz-title">{title}</div>',
             f'<div class="quiz-body">{body_md}</div>']
    if code:
        html.append(f'<div class="quiz-code">{code}</div>')
    if hint:
        html.append(f'<div class="quiz-hint">힌트: {hint}</div>')
    html.append('</div>')
    display(HTML("".join(html)))

# ====== 도메인 데이터 (제주) ======
destination = "Jeju"
spots = ["Hallasan", "Seongsan Ilchulbong", "Hyeopjae Beach"]
activities_list  = ["hiking", "swimming", "hiking", "snorkeling", "hiking"]
activities_set   = set(activities_list)
activities_tuple = tuple(["hiking", "swimming", "snorkeling"])
spot_info = {
    "Hallasan": {"height_m": 1947, "rating": 4.8, "activity": "hiking"},
    "Seongsan Ilchulbong": {"height_m": 182, "rating": 4.9, "activity": "hiking"},
    "Hyeopjae Beach": {"visitors_monthly": 100_000, "rating": 4.6, "activity": "swimming"}
}

# ====== 공용 입력 루프 ======
def _ask_until_correct(checker, prompt="> "):
    while True:
        ans = input(prompt)
        ok, msg = checker(ans)
        if ok:
            print(f"{CORRECT_ICON} 정답입니다!\n")
            return ans
        else:
            print(f"{WRONG_ICON} {msg} 다시 시도하세요.\n")

# =========================
# Q1 ~ Q16 : 프리뷰 + 답안
# =========================
# Q1
def show_q1():
    _panel("Q1) 결과물 출력하기",
           "아래 코드의 빈칸에 들어갈 **출력 함수** 이름을 쓰세요.",
           code='빈칸("Hello Jeju")', hint="파이썬에서 화면에 출력할 때 쓰는 내장 함수")
def answer_q1():
    return _ask_until_correct(lambda s: (s.strip()=="print", "함수 이름만 소문자로 입력하세요."))

# Q2
def show_q2():
    _panel(
        "Q2) 객관식: 포맷팅 문법이 잘못 적용된 경우는?",
        "다음 중 문법적으로 잘못되었거나 실행 시 오류가 나는 포맷팅을 고르세요.",
        hint="포맷 문자열의 '필드'와 format() 인자의 매칭 규칙을 떠올려 보세요."
    )
    display(Markdown(
        "**보기**\n\n"
        "1) f\"{name} is {age} years old.\"\n\n"
        "2) \"{} is {} years old.\".format(name, age)\n\n"
        "3) \"{name} is {age} years old.\".format(name, age)"
    ))
def answer_q2():
    # 정답: 3번 (named fields를 사용했는데 positional 인자를 넘겨서 오류)
    return _ask_until_correct(
        lambda s: (s.strip() == "3", "보기 번호(1/2/3) 중에서, 오류가 나는 케이스를 고르세요.")
    )

# Q3
def show_q3():
    word = "Seongsan"
    _panel(
        "Q3) 인덱싱",
        f'`word = "{word}"` 일 때, `word[0]`의 값(문자 그대로)을 쓰세요.',
        code='word = "Seongsan"\nprint(word[0])',
        hint="문자열 인덱스는 0부터 시작합니다."
    )
def answer_q3():
    word = "Seongsan"
    return _ask_until_correct(lambda s: (s.strip()==word[0], "문자 하나만 정확히 입력하세요."))

# Q4
def show_q4():
    word = "Seongsan"
    _panel(
        "Q4) 슬라이싱",
        f'`word = "{word}"` 일 때, `word[:4]`의 결과를 쓰세요.',
        code='word = "Seongsan"\nprint(word[:4])',
        hint="슬라이스는 시작 포함, 끝 인덱스는 포함되지 않습니다."
    )
def answer_q4():
    word = "Seongsan"
    return _ask_until_correct(lambda s: (s.strip()==word[:4], "대소문자/철자 확인!"))

# Q5
def show_q5():
    _panel("Q5) 객관식: 자료형 특성",
           "**순서가 없고**, **중복을 허용하지 않으며**, **가변**인 자료형은?")
    display(Markdown("**보기**\n\n1) list\n\n2) set\n\n3) tuple"))
def answer_q5():
    return _ask_until_correct(lambda s: (s.strip()=="2", "자료형의 핵심 특성을 떠올려 보세요."))

# Q6
def show_q6():
    _panel(
        "Q6) Set의 특성",
        "다음 코드의 결과값을 **정수**로 입력하시오.",
        code=f"print(len(set({activities_list})))",
        hint="len() 함수는 시퀀스나 컬렉션의 길이(원소 개수)를 반환합니다."
    )

def answer_q6():
    def checker(s):
        s = s.strip()
        if not s.isdigit():
            return (False, "정수로 입력하세요.")
        return (
            int(s) == len(set(activities_list)),
            f"set은 중복을 제거합니다. 결과 원소 개수는 {len(set(activities_list))}개입니다."
        )
    return _ask_until_correct(checker)

# Q7
def show_q7():
    _panel(
        "Q7) 딕셔너리 접근",
        '`spot_info["Hallasan"]["height_m"]`의 값은? **정수**로 쓰세요.',
        code=(
            'spot_info = {\n'
            '    "Hallasan": {"height_m": 1947, "rating": 4.8, "activity": "hiking"},\n'
            '    "Seongsan Ilchulbong": {"height_m": 182, "rating": 4.9, "activity": "hiking"},\n'
            '    "Hyeopjae Beach": {"visitors_monthly": 100_000, "rating": 4.6, "activity": "swimming"}\n'
            '}\n'
            'print(spot_info["Hallasan"]["height_m"])'
        ),
        hint='중첩 딕셔너리에서 키를 순서대로 접근합니다: ["Hallasan"] → ["height_m"]'
    )
def answer_q7():
    return _ask_until_correct(lambda s: (s.strip().isdigit() and int(s.strip())==spot_info["Hallasan"]["height_m"],
                                        "딕셔너리 중첩 접근을 떠올리세요."))

# Q8
def show_q8():
    _panel(
        "Q8) 객관식: 딕셔너리 요소",
        "다음 중 **딕셔너리를 구성하는 요소가 아닌 것**은?",
    )
    display(Markdown("**보기**\n\n1) keys\n\n2) values\n\n3) indexes\n\n4) items"))

def answer_q8():
    return _ask_until_correct(
        lambda s: (s.strip() == "3", "딕셔너리에는 keys, values, items만 있고 indexes는 없습니다.")
    )

# Q9
def show_q9():
    _panel("Q9) f-string 결과 쓰기",
           "다음 f-string의 **출력 결과 전체**를 정확히 쓰세요.",
           code='spot="Hallasan"; h=1947\nf"{spot} is {h} meters tall."')
def answer_q9():
    expected = "Hallasan is 1947 meters tall."
    return _ask_until_correct(lambda s: (s.strip()==expected, "스페이스/철자/대소문자까지 정확히 입력!"))

# Q10
def show_q10():
    _panel(
        "Q10) 객관식: 부동소수점 비교",
        "`0.1 + 0.2 == 0.3` 의 결과로 알맞은 것은?"
    )
    display(Markdown("**보기**\n\n1) True \n\n2) False\n\n3) 비교 불가"))
def answer_q10():
    return _ask_until_correct(lambda s: (s.strip()=="2", "부동소수점 표현 방식을 떠올려 보세요."))

# Q11
def show_q11():
    _panel(
        "Q11) 객관식: 결과가 다른 하나 고르기",
        "서로 다른 결과(나머지 셋과 값이 다른 것)를 고르세요.",
        code=(
            '1) 10 + 10.0 == 20.0\n'
            '2) len({"Hallasan": 1947, "Seongsan": 182}.keys()) == 2\n'
            '3) ("hiking","swimming")[0] == ["hiking","swimming"][0]\n'
            '4) 0.1 + 0.2 == 0.3'
        )
    )
    # 보기 번호만 입력받게 하므로 별도 Markdown 선택지는 생략합니다.

def answer_q11():
    # 정답: 4  (1,2,3은 True / 4는 False)
    return _ask_until_correct(
        lambda s: (s.strip() == "4", "보기 번호(1/2/3/4) 중에서 서로 다른 결과를 고르세요.")
    )
# Q12
def show_q12():
    _panel(
        "Q12) 주관식(코드 작성, 한 줄)",
        (
            "`spot_info` 딕셔너리에서 **세 번째 키**를 꺼내는 코드를 한 줄 작성하세요.\n\n"
            "출력(정답):\n"
            "Hyeopjae Beach"
        ),
        code=(
            'spot_info = {\n'
            '    "Hallasan": {"height_m": 1947, "rating": 4.8},\n'
            '    "Seongsan Ilchulbong": {"height_m": 182, "rating": 4.9},\n'
            '    "Hyeopjae Beach": {"visitors_monthly": 100000, "rating": 4.6}\n'
            '}\n'
            '# 여기에 코드를 작성하세요.'
        ),
        hint="dict.keys()를 리스트로 변환해 인덱싱하세요."
    )

def answer_q12():
    expected = "Hyeopjae Beach"
    while True:
        src = input("코드를 한 줄 입력하세요:\n> ").strip()
        if not src:
            print(f"{WRONG_ICON} 입력이 비어 있습니다. 다시 작성하세요.\n")
            continue
        if "\n" in src:
            print(f"{WRONG_ICON} 여러 줄은 허용되지 않습니다. 한 줄만 작성하세요.\n")
            continue
        if expected in src and "spot_info" not in src:
            print(f"{WRONG_ICON} 하드코딩은 허용되지 않습니다. 반드시 spot_info를 활용하세요.\n")
            continue

        ns = {"spot_info": spot_info}
        buf = io.StringIO()
        result = None
        try:
            # 표현식 평가 먼저 시도
            result = eval(src, {}, ns)
        except SyntaxError:
            try:
                with contextlib.redirect_stdout(buf):
                    exec(src, {}, ns)
            except Exception as e:
                print(f"{WRONG_ICON} 실행 에러: {e}\n다시 시도해 보세요.\n")
                continue
        except Exception as e:
            print(f"{WRONG_ICON} 실행 에러: {e}\n다시 시도해 보세요.\n")
            continue

        out_exec = buf.getvalue().strip()
        if out_exec == expected or result == expected:
            print(f"{CORRECT_ICON} 정답입니다!\n")
            return src
        else:
            print(f"{WRONG_ICON} 출력이 다릅니다.\n"
                  f"- 기대 출력: {expected!r}\n"
                  f"- 실제 출력: {out_exec or result!r}\n"
                  "힌트: list(spot_info.keys())[2] 를 떠올려 보세요.\n")
# === 신규 추가 문항 (Q13~Q16) ===

# Q13: 음수 인덱싱
def show_q13():
    word = "Hallasan"
    _panel(
        "Q13) 텍스트 타입의 인덱싱",
        f'`word = "{word}"` 일 때, `word[-1]`의 값은? (마지막 글자)',
        code='word = "Hallasan"\nprint(word[-1])'
    )
def answer_q13():
    word = "Hallasan"
    return _ask_until_correct(lambda s: (s.strip()==word[-1], "마지막 글자 하나를 입력."))

# Q14: 슬라이싱 step
def show_q14():
    _panel(
        "Q14) 주관식(코드 작성, 한 줄) : 슬라이싱으로 'san' 출력",
        (
            "문자열 s 에서 **슬라이싱만 사용하여** 'san' 을 꺼내는 코드를 작성하세요.\n"
            "※ print를 쓰지 않아도 됩니다 (표현식만 입력해도 OK)."
        ),
        code=(
            's = "SeongsanIlchulbong"\n'
            '# 여기에 슬라이싱을 작성하세요. 예: s[start:end]'
        ),
        hint="슬라이싱 기본형: s[start:end] (start 포함, end 제외). 'san' 부분의 인덱스를 찾아보세요."
    )

def answer_q14():
    s = "SeongsanIlchulbong"
    expected = "san"
    while True:
        src = input("슬라이싱 한 줄을 입력하세요 (print 생략 가능):\n> ").strip()
        if not src:
            print(f"{WRONG_ICON} 입력이 비어 있습니다. 다시 작성하세요.\n")
            continue
        if "\n" in src:
            print(f"{WRONG_ICON} 여러 줄은 허용되지 않습니다. 한 줄만 작성하세요.\n")
            continue
        # 슬라이싱 검사
        if "s" not in src or "[" not in src or ":" not in src or "]" not in src:
            print(f"{WRONG_ICON} 반드시 s[start:end] 형태의 슬라이싱을 사용하세요.\n")
            continue

        ns = {"s": s}
        buf = io.StringIO()
        result = None
        try:
            result = eval(src, {}, ns)  # 표현식
        except SyntaxError:
            try:
                with contextlib.redirect_stdout(buf):
                    exec(src, {}, ns)  # print 사용
            except Exception as e:
                print(f"{WRONG_ICON} 실행 에러: {e}\n다시 시도해 보세요.\n")
                continue
        except Exception as e:
            print(f"{WRONG_ICON} 실행 에러: {e}\n다시 시도해 보세요.\n")
            continue

        out_exec = buf.getvalue().strip()
        if out_exec == expected or result == expected:
            print(f"{CORRECT_ICON} 정답입니다!\n")
            return src
        else:
            shown = out_exec if out_exec else result
            print(f"{WRONG_ICON} 출력/평가 결과가 다릅니다. 기대값은 'san' 입니다. "
                  f"현재 출력: {shown!r}\n힌트: 'san'은 인덱스 4~7 사이에 있습니다.\n")
# Q15: set 연산 (합집합/교집합)
def show_q15():
    _panel(
        "Q15) 주관식(코드 작성, 한 줄) : 리스트 중복 제거",
        (
            "다음 리스트에서 **중복을 제거**하는 코드를 작성하세요.\n\n"
            "출력(정답 예시):\n"
            "['hiking', 'swimming', 'snorkeling']   (순서는 달라도 정답 처리)"
        ),
        code=(
            "activities = ['hiking','swimming','hiking','snorkeling','hiking']\n"
            "# 여기에 한 줄 코드를 작성하세요."
        ),
        hint="리스트는 중복을 허용하고, 세트는 중복을 제거합니다. list(set(...)) 형태를 떠올리세요."
    )

def answer_q15():
    expected_set = {"hiking", "swimming", "snorkeling"}
    activities = ['hiking','swimming','hiking','snorkeling','hiking']
    while True:
        src = input("중복을 제거하는 한 줄 코드를 작성하세요:\n> ").strip()
        if not src:
            print(f"{WRONG_ICON} 입력이 비어 있습니다. 다시 작성하세요.\n")
            continue

        ns = {"activities": activities}
        buf = io.StringIO()
        result = None
        try:
            result = eval(src, {}, ns)
        except SyntaxError:
            try:
                with contextlib.redirect_stdout(buf):
                    exec(src, {}, ns)
            except Exception as e:
                print(f"{WRONG_ICON} 실행 에러: {e}\n")
                continue
        except Exception as e:
            print(f"{WRONG_ICON} 실행 에러: {e}\n")
            continue

        out_exec = buf.getvalue().strip()

        # 실행 결과가 리스트 형태인지 확인
        if isinstance(result, list):
            if set(result) == expected_set:
                print(f"{CORRECT_ICON} 정답입니다! (순서는 달라도 OK)\n")
                return src
        elif out_exec:
            try:
                evaluated = eval(out_exec)
                if isinstance(evaluated, list) and set(evaluated) == expected_set:
                    print(f"{CORRECT_ICON} 정답입니다!\n")
                    return src
            except Exception:
                pass

        print(f"{WRONG_ICON} 출력/평가 결과가 다릅니다.\n"
              f"기대 원소: {expected_set}\n"
              f"현재 결과: {result or out_exec}\n"
              "힌트: list(set(activities)) 형태를 떠올리세요.\n")
# Q16: dict.get 기본값
def show_q16():
    _panel(
        "Q16) 객관식: 튜플(tuple)의 특성",
        "다음 중 튜플의 특성을 올바르게 설명한 것은?"
    )
    display(Markdown(
        "**보기**\n\n"
        "1) 튜플은 리스트와 달리 원소를 변경할 수 없다.\n\n"
        "2) 튜플은 집합(set)과 같이 중복을 제거한다.\n\n"
        "3) 튜플은 항상 딕셔너리의 키(key)로 사용할 수 없다.\n\n"
        "4) 튜플은 문자열과 달리 인덱싱이나 슬라이싱을 지원하지 않는다."
    ))

def answer_q16():
    return _ask_until_correct(
        lambda s: (s.strip() == "1", 
                   "정답은 1번입니다. 튜플은 불변(immutable)하며, 리스트처럼 순서를 유지하고 중복을 허용하며 인덱싱/슬라이싱도 지원합니다.")
    )

# ====== 프리뷰 전체 보기 ======
def show_all():
    show_q1(); show_q2(); show_q3(); show_q4(); show_q5(); show_q6(); show_q7(); show_q8()
    show_q9(); show_q10(); show_q11(); show_q12(); show_q13(); show_q14(); show_q15(); show_q16()
    display(Markdown("> 프리뷰가 모두 표시되었습니다. 이제 각 문항의 `answer_qX()`를 실행해서 답만 입력하세요!"))
# 사칙연산(+,-,*,/)과 거듭제곱(^)을 지원하는
# Infix(중위표기식) → Postfix(후위표기식) 변환 및 계산기 프로그램

# ----------------------------
# 연산자 우선순위 정의
# ----------------------------
OPS = {"+": 1, "-": 1, "*": 2, "/": 2, "^": 3}
# 거듭제곱(^)은 오른쪽 결합 → RIGHT_ASSOC 집합에 추가
RIGHT_ASSOC = {"^"}

# ----------------------------
# Tokenizer: 문자열 수식을 토큰 리스트로 변환
# ----------------------------
def tokenize(s: str):
    tokens, num = [], []

    # 숫자 버퍼를 tokens에 옮기고 초기화하는 함수
    def flush_num():
        if num:
            tokens.append("".join(num))
            num.clear()

    prev = None  # 직전 토큰 추적 (단항 음수 판별용)
    i = 0
    while i < len(s):
        ch = s[i]

        if ch.isspace():         # 공백은 무시
            i += 1
            continue

        if ch.isdigit() or ch == ".":   # 숫자(정수/소수)
            num.append(ch)
            i += 1

        elif ch in OPS or ch in "()":   # 연산자 또는 괄호
            flush_num()

            # 단항 '-' 처리 → 0 - (다음 항) 으로 변환
            if ch == "-" and (prev is None or prev in OPS or prev == "("):
                tokens.append("0")
                tokens.append("-")
            else:
                tokens.append(ch)

            prev = tokens[-1]
            i += 1
            continue

        # prev 업데이트 (숫자를 입력 중일 때는 나중에 flush_num 후 갱신됨)
        prev = None if not tokens and not num else (tokens[-1] if not num else None)

    # 숫자 버퍼가 남아있으면 tokens에 추가
    flush_num()
    return tokens

# ----------------------------
# Infix → Postfix (Shunting Yard 알고리즘)
# ----------------------------
def infix_to_postfix(tokens):
    out, st = [], []
    for t in tokens:
        if t not in OPS and t not in ("(", ")"):   # 피연산자(숫자)
            out.append(t)

        elif t in OPS:   # 연산자
            while st and st[-1] in OPS:
                top = st[-1]
                # 우선순위가 높거나 / 같은데 좌결합이면 pop
                if (OPS[top] > OPS[t]) or (OPS[top] == OPS[t] and t not in RIGHT_ASSOC):
                    out.append(st.pop())
                else:
                    break
            st.append(t)

        elif t == "(":   # 여는 괄호
            st.append(t)

        elif t == ")":   # 닫는 괄호 → '(' 나올 때까지 pop
            while st[-1] != "(":
                out.append(st.pop())
            st.pop()  # '(' 제거

    # 스택에 남은 연산자 모두 출력
    while st:
        out.append(st.pop())
    return out

# ----------------------------
# Postfix 계산기
# ----------------------------
def eval_postfix(postfix):
    st = []
    for t in postfix:
        if t not in OPS:   # 숫자면 스택에 push
            v = float(t)
            # 정수라면 int로 변환 (보기 좋게)
            st.append(int(v) if v.is_integer() else v)
        else:              # 연산자면 스택에서 두 피연산자 pop 후 계산
            b, a = st.pop(), st.pop()
            st.append(
                a + b if t == "+" else
                a - b if t == "-" else
                a * b if t == "*" else
                a / b if t == "/" else
                a ** b
            )
    return st[0]

# ----------------------------
# Infix 계산 함수 (한 줄 완성)
# ----------------------------
def calc(expr: str):
    return eval_postfix(infix_to_postfix(tokenize(expr)))

# ----------------------------
# 메인 실행부: REPL (계속 입력받아 계산)
# ----------------------------
if __name__ == "__main__":
    while True:
        s = input("> ").strip()
        if not s:   # 빈 입력 무시
            continue
        pf = infix_to_postfix(tokenize(s))   # 후위표기 변환
        print("Postfix:", " ".join(pf))      # 후위표기 출력
        print("Result :", calc(s))           # 계산 결과 출력

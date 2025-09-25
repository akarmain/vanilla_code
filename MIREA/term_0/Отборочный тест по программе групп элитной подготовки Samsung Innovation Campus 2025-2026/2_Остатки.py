def is_correct(s: str) -> str:
    stack = []
    pairs = {')': '(', ']': '[', '}': '{'}

    for ch in s:
        if ch in "([{":
            stack.append(ch)
        elif ch in ")]}":
            if not stack or stack[-1] != pairs[ch]:
                return "no"
            stack.pop()

    return "yes" if not stack else "no"


# чтение ввода
s = input().strip()
print(is_correct(s))

s = input().strip()
if len(s) % 2 == 1:
    print("no")

pairs = {')': '(', ']': '[', '}': '{'}
openers = set(pairs.values())
stack = []

for ch in s:
    if ch in openers:
        stack.append(ch)
    else:
        if not stack or pairs.get(ch) != stack[-1]:
            print("no")
            break
        stack.pop()
else:
    print("yes" if not stack else "no")

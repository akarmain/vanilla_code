data = input().strip().split()
n = int(data[0])

pairs = []
for _ in range(n):
    pid, score = map(int, input().strip().split())
    pairs.append((pid, score))

pairs.sort(key=lambda x: (-x[1], x[0]))

for pid, score in pairs:
    print(pid, score)

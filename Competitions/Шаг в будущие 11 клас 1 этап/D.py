n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
k = int(input())
ops = [int(input()) for _ in range(k)]
row_sums = [sum(row) for row in a]
col_sums = [sum(a[i][j] for i in range(n)) for j in range(m)]
sides = [0, 1, 2, 3]  # sides[physical_side] = original_side
for op in ops:
    if op == 1:
        sides = [sides[3], sides[0], sides[1], sides[2]]
        n, m = m, n
        row_sums, col_sums = col_sums[::-1], row_sums[:]
    elif op == 2:
        sides = [sides[1], sides[2], sides[3], sides[0]]
        n, m = m, n
        row_sums, col_sums = col_sums[:], row_sums[::-1]
    elif op == 3:
        sides = [sides[2], sides[1], sides[0], sides[3]]
        row_sums = row_sums[::-1]
    elif op == 4:
        sides = [sides[0], sides[3], sides[2], sides[1]]
        col_sums = col_sums[::-1]
p1_side = sides[3]
p2_side = sides[1]
if p1_side == 0:
    p1_score = row_sums[0]
elif p1_side == 1:
    p1_score = col_sums[-1]
elif p1_side == 2:
    p1_score = row_sums[-1]
else:
    p1_score = col_sums[0]
if p2_side == 0:
    p2_score = row_sums[0]
elif p2_side == 1:
    p2_score = col_sums[-1]
elif p2_side == 2:
    p2_score = row_sums[-1]
else:
    p2_score = col_sums[0]
print(f"{p1_score} {p2_score}")

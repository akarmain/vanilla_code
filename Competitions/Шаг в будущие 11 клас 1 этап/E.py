X = int(input())
A, B = map(int, input().split())
N = int(input())
ps = []
for _ in range(N):
    s, w = map(int, input().split())
    ps.append((s, s + w))
ps.sort()
am = A
rpt = {}
for r in range(am):
    rpt[r] = set()
for idx, (start, end) in enumerate(ps):
    s = start
    e = end
    start_i = s
    end_i = e
    start_i_plus = start_i + 1
    end_i_minus = end_i - 1
    if start_i_plus > end_i_minus:
        continue
    for r in range(am):
        q_min = (start_i_plus - r + A - 1) // A
        q_max = (end_i_minus - r) // A
        if q_min <= q_max:
            rpt[r].add(idx)
min_potholes = None
best_r = None
min_sum = None
for r in range(am):
    p_set = rpt[r]
    num_potholes = len(p_set)
    sum_pothole = sum(ps[i][0] for i in p_set)
    if min_potholes is None or num_potholes < min_potholes or (num_potholes == min_potholes and sum_pothole < min_sum):
        min_potholes = num_potholes
        best_r = r
        min_sum = sum_pothole
selected_potholes = rpt[best_r]
output_potholes = sorted([ps[i][0] for i in selected_potholes])
print(len(output_potholes))
for pos in output_potholes:
    print(pos)

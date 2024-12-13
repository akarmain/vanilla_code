def can_choose_elements_refined():

    dd1 = list(map(int, input().split()))
    dd2 = list(map(int, input().split()))
    dd3 = list(map(int, input().split()))

    test_cases = [dd1, dd2, dd3]

    results = []
    for n, m, k, a, b in test_cases:
        a_set = set(a)
        b_set = set(b)
        common_elements = a_set & b_set
        unique_a = a_set - common_elements
        unique_b = b_set - common_elements
        required_from_a = sum(1 for i in range(1, k + 1) if i in unique_a)
        required_from_b = sum(1 for i in range(1, k + 1) if i in unique_b)
        common_required = sum(1 for i in range(1, k + 1) if i in common_elements)

        if required_from_a + required_from_b + common_required >= k and \
                min(required_from_a, k // 2) + min(required_from_b, k // 2) + common_required >= k:
            results.append("YES")
        else:
            results.append("NO")

    return results



results_refined = can_choose_elements_refined()


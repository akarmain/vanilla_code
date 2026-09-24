def main(s):
    p = 0
    minp = 0
    maxp = 0
    for char in s:
        if char == 'R':
            p += 1
            minp = min(minp, p)
            maxp = max(maxp, p)
        elif char == 'L':
            p -= 1
            minp = min(minp, p)
            maxp = max(maxp, p)
        elif char == '?':
            p_left = p - 1
            minp_left = min(minp, p_left)
            maxp_left = maxp
            spread_left = maxp_left - minp_left
            p_right = p + 1
            minp_right = minp
            maxp_right = max(maxp, p_right)
            spread_right = maxp_right - minp_right
            if spread_left > spread_right:
                p = p_left
                minp = minp_left
                maxp = maxp_left
            else:
                p = p_right
                minp = minp_right
                maxp = maxp_right
    return maxp - minp


if __name__ == '__main__':
    print(main(input()))

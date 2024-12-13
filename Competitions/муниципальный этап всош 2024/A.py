def main(a, b, t):
    ans = 0
    for t in range(t + 1):
        if t % 2 == 0:
            if t % a == 0:
                ans += 1
        else:
            if t % b == 0:
                ans += 1
    return ans


if __name__ == '__main__':
    print(main(4, 3, 10))

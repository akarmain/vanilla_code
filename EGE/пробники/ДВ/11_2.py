import math


def main():
    ans = []
    all_bit = 13631488
    for m in range(2, 100000):
        bv = math.ceil(math.log2(m))
        odna = math.ceil((1224 * bv) / 8)
        if odna * 16_535 < all_bit:
            ans.append(m)
    return max(ans)


if __name__ == "__main__":
    print("ANS:", main())

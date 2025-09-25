def algos(n):
    s = "1" + ("3" * n)
    while "12" in s or "233" in s or "333" in s:
        s = s.replace("12", "233", 1)
        s = s.replace("233", "23", 1)
        s = s.replace("3333", "32", 1)
    return len(s)


def main():
    for n in range(6, 200):
        if algos(n) % 6 == 0:
            return n


if __name__ == "__main__":
    print(algos(20))
    print("ANS:", main())

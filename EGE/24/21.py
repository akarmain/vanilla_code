def main():
    ans = -float('inf')
    c = 1
    data = open("../../imputs/EGE_21.txt").readline()
    for i in range(len(data) - 2):
        if data[i] != data[i + 1]:
            c += 1

            ans = max(c, ans)
        else:
            c = 1
    return ans


if __name__ == "__main__":
    print("ANS:", main())

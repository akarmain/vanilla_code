def main():
    n = int(input())
    s1 = input()
    s2 = input()
    f = True
    for iter in range(n - 1):
        if iter % 2 == 0 and s1[iter + 1] == '<' and s2[iter] == '<':
            f = False
        if iter % 2 != 0 and s1[iter] == '<' and s2[iter + 1] == '<':
            f = False
    return f


if __name__ == "__main__":
    for i in range(int(input())):
        print("YES" if main() else "NO")

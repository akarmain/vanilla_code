def main():
    s = input()
    st = "1234567890"
    ans = 4 + st.index(s[0])
    for i in range(3):
        ans += abs(st.index(s[i]) - st.index(s[i + 1]))
    print(ans)


if __name__ == '__main__':
    for i in range(int(input())):
        main()

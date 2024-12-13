def main():
    su = int(input()) - 3
    word = ['a', 'a', 'a']
    for i in range(2, -1, -1):
        add = min(su, 25)
        word[i] = chr(ord('a') + add)
        su -= add
        if su <= 0:
            break

    return ''.join(word)


if __name__ == '__main__':
    for _ in range(int(input())):
        print(main())

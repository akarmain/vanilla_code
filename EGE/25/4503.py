import re


def main():
    for d in range(141, 10**8, 141):
        if re.fullmatch(r"1234\d*7", str(d)):
            print(d, d//141)


if __name__ == "__main__":
    print("ANS:", main())

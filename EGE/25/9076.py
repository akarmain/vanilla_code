"""
URL:

"""
import re


def main():
    for d in range(2023, 10 ** 9, 2023):
        c = re.compile(r"20\d*23")
        if c.fullmatch(str(d)):
            s = sum(list(map(int, str(d))))
            if s % 7 == 0 and s < 20:
                print(d)


if __name__ == "__main__":
    print("ANS:", main())

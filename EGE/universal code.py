import random

"""
URL: universal code
"""


def main():
    for i in range(27):
        print(i, random.randint(0, 1_000_000))


if __name__ == "__main__":
    main()

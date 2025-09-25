import re


def main():
    data = open("../../imputs/EGE_13866.txt").readline()[:1000]
    pattern = re.compile(r'(?:(?![13579]{3}).)+')
    fragments = pattern.findall(data)
    return max(map(len, fragments), default=0)

if __name__ == "__main__":
    print("ANS:", main())

import re
def main():
    for d in range(253, 10**8, 253):
        if re.fullmatch(r"12\d\d15\d*6", str(d)):
            print(d, d//253)


if __name__ == "__main__":
    print("ANS:", main())

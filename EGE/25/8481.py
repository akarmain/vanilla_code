import re

def main():
    c1 = re.compile(r"81\d2\d*80")
    c2 = re.compile(r"\d*9\d*")
    for d in range(237, 10**8, 237):
        if c1.fullmatch(str(d)) and (not c2.fullmatch(str(d))):
            print(d, d//237)

if __name__ == "__main__":
    print("ANS:", main())

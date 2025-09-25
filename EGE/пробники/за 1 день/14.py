import string

def to_5(n):
    ans = ''
    while n:
        ans = str(n % 5) + ans
        n //= 5
    return ans



def main():
    ...


if __name__ == "__main__":
    print("ANS:", main())

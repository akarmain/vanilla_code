from itertools import product

def main():
    n = 0
    for d in product("АГМНСТУ", repeat=6):
        d = "".join(d)
        n+=1
        if d[0] != "У" and d.count("М") == 2 and d.count("Г") <= 1:
            print(n, d)


if __name__ == "__main__":
    print("ANS:", main())

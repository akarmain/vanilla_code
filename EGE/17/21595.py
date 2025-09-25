def main():
    data = []
    for l in open("../../imputs/EGE_21595.txt"):
        data.append(int(l))

    print(data)


if __name__ == "__main__":
    print("ANS:", main())

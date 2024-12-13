def main(a, b, c):
    numbers = sorted([a, b, c])
    arithmetic = numbers[1] * 2 == numbers[0] + numbers[2]
    geometric = numbers[1] ** 2 == numbers[0] * numbers[2]
    if geometric and numbers[1] / numbers[0] <= 1:
        geometric = False
    if arithmetic and geometric:
        return "B " + " ".join(map(str, numbers))
    elif arithmetic:
        return "A " + " ".join(map(str, numbers))
    elif geometric:
        return "G " + " ".join(map(str, numbers))
    else:
        return "No"

if __name__ == '__main__':
    print(main(int(input()), int(input()),int(input())))

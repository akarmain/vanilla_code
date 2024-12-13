def main(f, a, b, moments):
    charge = f
    last_moment = 0
    for moment in moments:
        cost_on = a * (moment - last_moment)
        charge -= min(cost_on, b)
        if charge <= 0:
            return "NO"
        last_moment = moment
    return "YES"


if __name__ == '__main__':
    for _ in range(int(input())):
        n, f, a, b = map(int, input().split())
        moments = list(map(int, input().split()))
        print(main(f, a, b, moments))

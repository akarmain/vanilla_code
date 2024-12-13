def main():
    n, m = map(int, input().split())
    users = {}
    for _ in range(n):
        id, vaule = map(int, input().split())
        users[id] = vaule
    for _ in range(m):
        a, b, x = map(int, input().split())
        if users[a] >= x:
            users[a] -= x
            users[b] += x
    for k, v in users.items():
        print(k, v)


"""
4 5
1 500
2 200
3 1000
4 300
1 2 200
2 3 150
3 4 100
4 1 300
2 3 50


Ответ:
1 600
2 200
31100
4 100"""
if __name__ == '__main__':
    main()

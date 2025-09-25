"""
URL: https://education.yandex.ru/ege/task/ae005540-2fe7-4bac-9836-f47864553f09

"""
from fnmatch import fnmatch

def main():
    max_value = 10**10  # 100,000,000,000
    for x in range(2024, max_value + 1, 2024):
        if fnmatch(str(x), '10*2024?'):
            print(x, x // 2024)

if __name__ == "__main__":
    main()


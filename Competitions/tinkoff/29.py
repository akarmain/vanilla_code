import re


def check_password(password):
    # Проверка длины пароля
    if not 10 <= len(password) <= 25:
        return False
    if not re.search(r"[_\.\-@#&]", password):
        return False
    if not re.search(r"\d", password):
        return False
    if not re.search(r"[A-Z]", password):
        return False
    if not re.search(r"[a-z]", password):
        return False

    return True


def check_login(login):
    if not 5 <= len(login) <= 20:
        return False
    if not re.match(r"^[a-zA-Z0-9_]+$", login):
        return False

    return True


def main():
    login = input()
    password = input()
    return check_password(password) and check_login(login)


if __name__ == '__main__':
    for _ in range(int(input())):
        print("yes" if main() else "no")

"""
1
asdasd
1234567890123456A1a&
"""
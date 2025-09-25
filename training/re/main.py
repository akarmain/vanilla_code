import re


def domain():
    data = """Emails to extract:
    alice.smith@example.com
    bob@example.co.uk
    carol99@sub.mail-server.net
    not-an-email@wrong
    dev@jun.akarmain.ru
    justtext
    """

    pattern = re.compile(r"([\w.-]+)@([\w.-]+)(\.[a-z]+)")
    for m in re.finditer(pattern, data):
        print(m.group(0), m.group(1), m.group(2), m.group(3)[1:])


if __name__ == "__main__":
    domain()

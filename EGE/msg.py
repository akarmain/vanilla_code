"""
URL:

"""


def main():
    f = open('24.txt', 'r')
    s = f.readlines()[0]
    i = 0
    j = 0
    ans = 0
    t = "UVWXYZ"
    d = {x:0 for x in t}
    while True:
        if all(d[x] <= 100 for x in t):
            ans = max(ans, i-j+1)
            i += 1
            if i == len(s):
                break
            if s[i] in t:
                d[s[i]] += 1
        else:
            if s[j] in t:
                d[s[j]] -= 1
            j += 1

    print(ans)


import requests


def send_telegram_message(message):
    """
    Отправляет сообщение через Telegram Bot API.

    :param bot_token: Строка, содержащая токен вашего Telegram бота.
    :param chat_id: Идентификатор чата получателя (числовое значение или строка).
    :param message: Текст сообщения для отправки.
    :return: Словарь с результатом выполнения запроса или информацией об ошибке.
    """
    url = f"https://api.telegram.org/bot5782848850:AAEAVe6Z7khw_PiDXX6PpjV_s5LIGQ12hnw/sendMessage"
    params = {
        'chat_id': "1619901051",
        'text': message
    }

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as error:
        return {"error": str(error)}


# Пример использования функции
if __name__ == '__main__':
    message_text = """

    """
    result = send_telegram_message(message_text)
    # print(result)

# if __name__ == '__main__':
#     main()


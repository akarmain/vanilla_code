import os
import string


def main():
    data = {}
    gp = "/Users/akarmain/PycharmProjects/vanilla_code/imputs/elements/"
    lf = os.listdir(gp)
    for file in lf:
        with open(gp + file, 'r') as f:  # Контекстный менеджер
            for line in f:
                line = line.lower().strip()
                line = line.translate(str.maketrans('', '', string.punctuation))
                for word in line.split():
                    data[word] = data.get(word, 0) + 1

    # Сортируем по убыванию частоты
    sorted_data = sorted(data.items(), key=lambda x: x[1], reverse=True)
    # Берём первые три
    return sorted_data[:3]



if __name__ == "__main__":
    print("ANS:", main())

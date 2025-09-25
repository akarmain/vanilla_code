import os
import string
import pandas as pd



def main():
    data = pd.Series()
    gp = "/Users/akarmain/PycharmProjects/vanilla_code/imputs/elements/"
    lf = os.listdir(gp)
    for file in lf:
        with open(gp + file, 'r') as f:  # Контекстный менеджер
            for line in f:
                line = line.lower().strip()
                line = line.translate(str.maketrans('', '', string.punctuation))
                for word in line.split():
                    data[word] = data.get(word, 0) + 1
    return data.sort_values(ascending=False)[:3]
    # # Сортируем по убыванию частоты
    # sorted_data = sorted(data.items(), key=lambda x: x[templates1.ipynb], reverse=True)
    # # Берём первые три
    # return sorted_data[:3]



if __name__ == "__main__":
    print("ANS:", *main().index)

import json
import os
import random

from dotenv import load_dotenv
from pathlib import Path

from string import ascii_lowercase, digits


def get_creds(file='.env'):
    dotenv_path = Path(file)
    load_dotenv()

    return os.environ.get('LOGIN'), os.environ.get('PASSWORD'), os.environ.get('NUMOFLETTERS')


def random_string(n=10):
    num_list = []
    while len(num_list) < n:
        num_list.append(random.choice(list(ascii_lowercase+digits)))
    return ''.join(num_list)


def json_to_file(jstring):
    """
    Пише json у вигляді стрічки у файл
    :param jstring:
    :return: нічого
    """
    with open("letters.json", "w") as outfile:
        json.dump(jstring, outfile)


def read_from_json(filename="letters.json"):
    """
    Відкриває файл зазначений файл
    :param filename:
    :return: повертає словник даних
    """
    # return dict
    with open(filename) as json_file:
        json_data = json_file.read()

    return json.loads(json_data)


def calc_symbol_in_strint(income_string: str, symbol="letter"):
    """
    :param income_string: строка яка буде піддаватися прорахунку
    :param symbol: "letter" якщо рахуем символи, "number" якщо рахуем десяткові числа
    :return: повертає кількість символів чи чисел з строки
    """
    lst = list(income_string)
    count = 0
    if symbol == "letter":
        for item in lst:
            if item.isalpha():
                count += 1
    elif symbol == "number":
        for item in lst:
            if item.isdigit():
                count += 1
    else:
        print("ПОМИЛКА!!! Невизначений символ")
    return count


if __name__ == '__main__':
    s = random_string(10)
    print(s)

    d = {
        'one': 1,
        'two': 2,
        'three': 3
    }

    # json_to_file(d)

    # j_data = read_from_json("../letters.json")
    #
    # print(j_data)
    #
    # for (key, value) in j_data.items():
    #     print(key, value)

    print(calc_symbol_in_strint(s, "letter"))
    print(calc_symbol_in_strint(s, "number"))
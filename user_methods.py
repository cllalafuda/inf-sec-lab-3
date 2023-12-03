import random
from math import ceil

from constants import USER_HELP

from validators import (
    yes_no_validator,
    brute_speed_validator,
    probability_validator,
    password_duration_validator
)
from misc import input_field
from constants import alphabet_mapping


ALPHABET = "".join(alphabet_mapping.values())
P = 10 ** -6
V = 10
T = 7200
S_LOW = ceil(V * T / P)


def commands_help():
    print(USER_HELP)


def get_password_length():
    alpha_len = len(ALPHABET)
    for length in range(0, 100):
        if alpha_len ** length >= S_LOW:
            return length


def change_alphabet():
    print("Замена параметров алфавита пароля. Выберите нужные группы символов\n")
    include_ascii_upper = input_field("Латинские прописные (y/n)", yes_no_validator)
    include_ascii_lower = input_field("Латинские строчные (y/n)", yes_no_validator)
    include_cyrillic_upper = input_field("Кириллические прописные (y/n)", yes_no_validator)
    include_cyrillic_lower = input_field("Кириллические строчные (y/n)", yes_no_validator)
    include_symbols = input_field("Символы (y/n)", yes_no_validator)
    include_digits = input_field("Цифры (y/n)", yes_no_validator)
    global ALPHABET
    new_alphabet = ""
    if include_ascii_upper == "y":
        new_alphabet += alphabet_mapping["au"]
    if include_ascii_lower == "y":
        new_alphabet += alphabet_mapping["al"]
    if include_cyrillic_upper == "y":
        new_alphabet += alphabet_mapping["cu"]
    if include_cyrillic_lower == "y":
        new_alphabet += alphabet_mapping["cl"]
    if include_symbols == "y":
        new_alphabet += alphabet_mapping["s"]
    if include_digits == "y":
        new_alphabet += alphabet_mapping["d"]
    if not new_alphabet:
        print("Необходимо выбрать хотя бы одну группу символов")
        return
    ALPHABET = new_alphabet
    print(f"Словарь изменен")


def change_settings():
    print("Замена переменных вероятности, скорости перебора и длительности действия. Введите данные\n")
    probability = float(input_field("Вероятность (в формате 0.x)", probability_validator))
    brute_speed = float(input_field("Скорость перебора (паролей в минуту)", brute_speed_validator))
    validity_time = float(input_field("Длительность действия пароля (в минутах)", password_duration_validator))
    global P, V, T
    P = probability
    V = brute_speed
    T = validity_time
    print(f"Данные изменены. {P=} {V=} {T=}")


def generate_password():
    password_length = get_password_length()
    password = "".join(random.choice(ALPHABET) for _ in range(password_length))
    print(f"Пароль сгенерирован: {password}")

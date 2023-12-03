from string import punctuation, ascii_uppercase, ascii_lowercase, digits

cyrillic_lowercase = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
cyrillic_uppercase = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
symbols = punctuation
USER_HELP = """ca      изменение словаря пароля
cs      изменение параметров генерации пароля
g       сгенерировать пароль
h       вывести список доступных команд
"""
COMMANDS = ["h", "cs", "g", "ca"]

alphabet_mapping = {
    "al": ascii_lowercase,
    "au": ascii_uppercase,
    "cl": cyrillic_lowercase,
    "cu": cyrillic_uppercase,
    "s": symbols,
    "d": digits,
}

from user_methods import (
    commands_help,
    change_alphabet,
    change_settings,
    generate_password
)
from misc import get_command


COMMANDS_MAPPING = {
    "ca": change_alphabet,
    "cs": change_settings,
    "g": generate_password,
    "h": commands_help
}


def main():
    while True:
        command = get_command()
        COMMANDS_MAPPING[command]()


if __name__ == '__main__':
    main()

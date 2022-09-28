# модуль ввода команд

from load import load_data
from add import add_data
from view import view_data
from save import save_data
from exit import exit_program
from help_commands import view_help
import names


def input_command():
    print()
    command = input("Ведите команду: ")
    if command =="/load":
        load_data()
    elif command =="/save":
        save_data()
    elif command =="/view":
        view_data()
    elif command =="/add":
        add_data()
    elif command =="/exit":
        exit_program()
    elif command =="/help":
        view_help()
    else:
        print("Такой команды пока нет или вы ошиблись в написании.")
        
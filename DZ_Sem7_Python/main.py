# Задание в группах: Создать телефонный справочник с возможностью импорта и экспорта данных формате .txt.

# главный модуль запуска программы

import os
from help_commands import view_help
from input import input_command
import names


os.system("cls") # очистка консоли
print("Добро пожаловать в систему 'Телефонный справочник!")
view_help()

while names.flag:
    input_command()

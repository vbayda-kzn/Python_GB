# модуль выхода из программы

from save import save_data
import names


def exit_program():
    answer = input("Хотите сохранить Справочник перед выходом из системы? (y/n): ")
    while answer !="y" and answer !="n":
        answer(input("Система не распознала ваш ответ. попробуйте еще раз: "))
    if answer == "y":
        save_data()
        print("Программа заканчивает свою работу. До новых встреч!")
        names.flag = False
    else: 
        print("Программа заканчивает свою работу. До новых встреч!")
        names.flag = False
   
        

# модуль загрузки справочника из файла

from view import view_data
import names


def load_data():
    with open ("tel.txt", 'r', encoding="utf-8") as f:
        data_str = f.read()
        data_lst = data_str.split('\n')
        names.data = [i.split(" ") for i in data_lst]
        names.data.pop()
    answer = input("Справочник загружен. Вывести его на экран? (y/n): ")
    while answer !="y" and answer !="n":
        answer = (input("Система не распознала ваш ответ. Попробуйте еще раз: "))
    if answer == "y":
        view_data()
    else:
        print("Как скажете. ")
    
    
     
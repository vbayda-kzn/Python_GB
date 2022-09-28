# модуль добавления в справочник новых записей

import names


def add_data():
    row = []
    answer = ""
    fio = input("Введите Фамилию, Имя и Отчество через пробел: ").split(" ")
    while len(fio) != 3:
        fio = input("Недостаточно данных или слишком много слов. Введите еще раз ").split(" ")
    
    fam = fio[0]
    name = fio[1]
    father_name = fio[2]
    tel = (input("Введите телефон: "))
    answer = input("Хотите ввести дополнительный телефон? (y/n) : ")
    while answer !="y" and answer !="n":
        answer = (input("Система не распознала ваш ответ. Попробуйте еще раз: "))
    if answer =="y":
        tel2 = input("Введите дополнительный телефон: ")
        row.extend([fam, name, father_name, tel, tel2])
    else:
        row.extend([fam, name, father_name, tel])
    names.data.append(row)
    print("В справочник внесена запись:")
    print()
    print("Фамилия       Имя           Отчество      Телефон осн.  Телефон доп. ")
    print("------------- ------------- ------------- ------------- -------------")
    for elem in row:
        print('%-14s' % (elem), end = "")
    print()
   
   
    
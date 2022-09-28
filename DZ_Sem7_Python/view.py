# модуль вывода на экран записей справочника

import names

def view_data():
    if names.data !=[]:
        print()
        print("Фамилия       Имя           Отчество      Телефон осн.  Телефон доп. ")
        print("------------- ------------- ------------- ------------- -------------")
        for row in names.data:
            for elem in row:
                #print(elem + "\t  ", end = "")
                print('%-14s' % (elem), end = "")
            print()
    else:
        print("Справочник пуст или не был загружен - показывать нечего.")
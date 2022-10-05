# Задача: Создать информационную систему позволяющую работать с сотрудниками
# некой компании \ студентами вуза \ учениками школы
# (прямая отсылка к первому семинару “введение в базы данных”)

# Расписание (номер класса, номер урока, начало/конец урока, номер кабинета, учитель(null), предмет)
# Контактные данные ...
# Учителя (ФИО, др, номер, адрес, классное руководство(null), основной предмет, вход/выход в школу???)


# Сделал как мог, не смог придумать проверку на пустой результат выдачи по поисковому запросу 
# (если ничего не выдало в поиске - возвращать "Ничего не найдено" вместо заголовка таблицы) и 
# еще бы было бы хорошо реализовать поиск без привязки к регистру, но если со стороны Питона там все понятно,
# то как реализовать это в рамках sql запроса со стороны ячейки БД так и  не понял.


from prettytable import PrettyTable
from prettytable import from_db_cursor
import sqlite3
from sqlite3 import Error

title = ""
zapros = ""
flag = True

def input_command():
    print()
    command = input("Ведите команду: ")
    if command =="/s":
        students()
    elif command =="/t":
        teachers()
    elif command =="/r":
        rasp()
    elif command =="/f":
        find()
    elif command =="/q":
        exit_program()
    elif command =="/h":
        help_commands()
    else:
        print("Такой команды пока нет или вы ошиблись в написании.")

def students():
    title = "Сведения об учащихся: "
    zapros = "SELECT * FROM Students"
    sql_connection(zapros, title)

def teachers():
    title = "Сведения о преподавателях: "
    zapros = "SELECT Id_teacher, Surname, Name, Patronymic, B_date, Phone_home,  Phone_work, Class_name, Predmet FROM Teachers"
    sql_connection(zapros, title)

def rasp():
    req_class = '"' + input("Расписание для классов 1А, 1Б, 1В, 2А, 2Б, 2В. Введите интересующий Вас класс: ") + '"'
    print(req_class)
    zapros = 'SELECT Number_lesson, Start_lesson, End_lesson, Rasp.Predmet, Surname, Cab FROM Rasp INNER JOIN Cabs ON Cabs.Id_cab = Rasp.Cab_id INNER JOIN Teachers ON Teachers.Id_teacher = Rasp.Id_teacher WHERE Rasp.Class_name = ' + req_class 
    title = "расписание для " + req_class + " класса:"
    print(zapros)
    sql_connection(zapros, title)

def find():# запрос на поиск в списках учеников и учителей
    title = "Результаты поиска: "
    req_string = '%' + input("Ведите фамилию или ее часть: ") + '%'
    print("Поиск в базе студентов..........")
    zapros = "SELECT * FROM Students WHERE Surname LIKE '" + req_string + "'" 
    sql_connection(zapros, title)
    print("Поиск в базе учителей..........")
    zapros = "SELECT * FROM Teachers WHERE Surname LIKE '" + req_string + "'" 
    sql_connection(zapros, title)

def help_commands():
    print("Список доступных команд: ")
    print("\t /s - вывод сведений об учениках")
    print("\t /t - вывод сведений об учителях")
    print("\t /r - вывод расписания для заданного класса школы")
    print("\t /f - поиск по фамилии в списках учеников и учителей")
    print("\t /q - выход из системы" )
    print("\t /h - вывод списка доступных команд" )

def exit_program():
    global flag
    print("Досвидания. До новых встреч!" )
    flag = False

def sql_connection(request, title_text):
    try:
        con = sqlite3.connect('sem8.db')
        cursorObj = con.cursor()
        cursorObj.execute(request)
        table = from_db_cursor(cursorObj)
        print(title_text)
        print(table)
    except Error:
        print(Error)
    finally:
        con.close()

print()
print()
print() 
print('Добро пожаловать в Информационную систему начальной школы № 158!')
print()
help_commands()

while flag:
    input_command()







# Создайте программу для игры в ""Крестики-нолики"".

import random


arr = [["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"]] 
desk_lst1 = []
desk_lst2 = []

mv = random.randint(1, 2) # кто ходит первым (номер игрока)
move_player = 0 # ход игрока (номер сектора доски)

flag = True

print()
print()
print("Приготовились? Мы начинаем игру 'Крестики-нолики'!")
choice = int(input("Нажмите '1' если хотите играть с человеком, '2' - если с компьютером: "))
while  choice != 1 and choice != 2:
    choice = int(input("Другие режимы игры еще в разработке, доступны режимы только '1' или '2': "))
print()
if choice == 2:
    print("Отлично! За Игрока2 ноликами играет компьютер! Крестиками играет Игрок1.")
else: 
    print("Отлично! Игрока1 ходит крестиками, Игрок2 - ноликами!")
print (f"По итогам жеребьевки первым ходит Игрок{mv}.")



def view_desk():
    global arr
    global desk_lst1
    global desk_lst2
    for item in desk_lst1:
        arr[((item + 2) // 3) - 1][item -3*((item + 2) // 3 - 1) - 1] = "X"         
    for item in desk_lst2:
        arr[((item + 2) // 3) - 1][item -3*((item + 2) // 3 - 1) - 1] = "O"    

    for row in arr:
        print(row)

def add_lst(): 
    global mv
    global desk_lst1
    global desk_lst2
    global move_player
    global desk_lst
    if mv == 1:
        desk_lst1.append(move_player)
        desk_lst = desk_lst1
    else: 
        desk_lst2.append(move_player)
        desk_lst = desk_lst2
    
def move():
    global choice
    global move_player
    global desk_lst1
    global desk_lst2

    if choice == 1 or mv == 1: # когда играет человек
        move_player = int(input(f"Игрок{mv}, введите номер сектора доски, где хотите оставить свой знак: "))
        while move_player <=0 or move_player > 9:
            move_player = int(input(f"Нет, такого сектора на доске нет! Давайте еще раз: "))
        if move_player in desk_lst1 or move_player in desk_lst2: # проверка на занятость секторов знаками   
            print("Вы профукали свой ход! Такой сектор уже занят.")
        else: 
            add_lst() # запись значений доски в список
            view_desk() # отображение результата хода на доске
         
    else: # когда играет компьютер
        move_player = random.randint(1, 9)
        while move_player in desk_lst1 or move_player in desk_lst2: # проверка на занятость секторов знаками
            move_player = random.randint(1, 9)
        print(f"Ходит Игрок2 (компьютер)...................сектор {move_player}!")
        add_lst()
        view_desk() # отображение результата хода на доске
    
  
def proverka_pobedy():
    global flag
    desk_lst.sort()
    
    win_comb_lst = [1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7]
    for item in win_comb_lst:
        if all(x in desk_lst for x in item):
            if choice == 2 and mv == 2:
                print(f"Увы, Победил Игорок{mv}, т.е. компьютер. Попробуйте в следующий раз.")
                flag = False 
            else:
                print(f"Ура!!! Победил Игрок{mv}!!!")
                flag = False
    if len(desk_lst1)+len(desk_lst2) == 9:
        print((f"Никто не победил - Ничья!!!"))
        flag = False

view_desk() # отображение результата хода на доске

while flag:
   
    move() # делаем ход
    proverka_pobedy() # проверяем, вдруг кто-то победил
    mv = (mv % 2) + 1 # меняем игроков
# Создайте программу для игры с конфетами человек против человека.

# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход. 
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# 

import random


konf = 2021
score1 = 0
score2 = 0
mv = random.randint(1, 2)

flag = True

print()
print()
print("Приготовились? Мы начинаем игру 'Конфеты'!")
choice = int(input("Нажмите '1' если хотите играть с человеком, '2' - если с компьютером: "))
while  choice != 1 and choice != 2:
    choice = int(input("Другие режимы игры еще в разработке, доступны режимы только '1' или '2': "))
print()
if choice == 2:
    print("Отлично! За Игрока2 играет компьютер!")
print (f"По итогам жеребьевки первым ходит Игрок{mv}.")
def view_score():
    print (f"В Банке - {konf} конфет. У Игрока1 - {score1} конфет, у Игрока2 - {score2} конфет")
    
def move():
    global score1
    global score2
    global konf
    if choice == 1 or mv == 1:
        move_player = int(input(f"Игрок{mv}, введите количество конфет, которые хотите взять: "))
        while konf < move_player:
            move_player = int(input(f"Столько конфет уже нет, возьмите меньше: "))
        while  move_player > 28:
            move_player = int(input(f"Нет, конфет можно взять не больше 28! Давайте еще раз: "))
    else:
        # move_player = random.randint(1, 28)
        move_player = konf % 28 + 1
        print(f"Игрок{mv} берет {move_player} конфет")

    if mv == 1:
        score1 = score1 + move_player
    else: 
        score2 = score2 + move_player
    konf = konf - move_player
  
def proverka_pobedy():
    global konf
    global flag
    if konf <= 0:
        if choice == 2 and mv == 2:
             print(f"Увы, Победил Игорок{mv}, т.е. компьютер. Он забирает все конфеты.")
        else:
            print(f"Ура!!! Победил Игорок{mv}!!!! Он забирает все конфеты соперника!!!")
        flag = False 

while flag:
    view_score() # выводим очки игроков и оставшиеся конфеты
    move() # делаем ход
    proverka_pobedy() # проверяем, вдруг кто-то победил
    mv = (mv % 2) + 1 # меняем игроков
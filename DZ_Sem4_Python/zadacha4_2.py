# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
N = int(input())
i = 2
mn_list = []
flag = True
while flag:
    if N % i == 0:
        mn_list.append(i)
        N = N / i
        if N == 1: 
            if len(mn_list) == 1: 
                print("Число простое и множителей кроме себя самого и 1 у него нет.")
            else: 
                print(mn_list)
            flag = False
    else: 
        i += 1

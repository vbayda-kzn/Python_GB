# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]
import math
# my_list = [2, 3, 4, 5, 6]
my_list = [2, 3, 5, 6]
new_list = []
for i in range(math.ceil(len(my_list)/2)):
    new_list.append(my_list[i]*my_list[-i-1])
print(new_list)
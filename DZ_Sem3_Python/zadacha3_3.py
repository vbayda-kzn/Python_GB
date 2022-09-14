# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между 
# максимальным и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19


my_list = [1.1, 1.2, 3.1, 5, 10.01]

minnn = my_list[0] - int(my_list[0]) 
maxxx = my_list[0] - int(my_list[0]) 

for item in my_list:
    if "." in str(item):
        if item - int(item) > maxxx:
            maxxx = item - int(item)
        if  item - int(item) < minnn:
            minnn = item - int(item)
print (round(maxxx - minnn, 3))
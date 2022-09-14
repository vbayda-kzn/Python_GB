# Задайте последовательность чисел. 
# Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

little_list = [1, 5, 7, 3, 7, 9, 5, 1, 4]
new_list = []
for i in little_list:
    if i not in new_list: 
        new_list.append(i)
print(new_list)
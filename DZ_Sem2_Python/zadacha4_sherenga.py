
# Петя впервые пришел на урок физкультуры в новой школе. Перед началом урока ученики выстраиваются по росту, 
# в порядке невозрастания. Напишите программу, которая определит на какое место в шеренге Пете нужно встать, чтобы 
# не нарушить традицию, если заранее известен рост каждого ученика и эти данные уже расположены по невозрастанию 
# (то есть каждое следующее число не больше предыдущего). Если в классе есть несколько учеников с таким же ростом, 
# как у Пети, то программа должна расположить его после них.

# Входные данные
# Первая строка входного файла INPUT.TXT содержит натуральное число N (N ≤ 100) – количество учеников (не считая Петю). 
# Во второй строке записаны N натуральных чисел Ai (Ai ≤ 200) – рост учеников в сантиметрах в порядке невозрастания. 
# Третья строка содержит единственное натуральное число X (X ≤ 200) – рост Пети.

# Выходные данные
# В выходной файл OUTPUT.TXT выведите единственное целое число – номер Пети в шеренге учеников. 



input_file = open("input_sherenga.txt", "r")
n = int(input_file.readline())
sherenga = input_file.readline()
rost_petr = int(input_file.readline())
input_file.close

sherenga_lst = sherenga.split()
sherenga_lst = [int(item) for item in sherenga_lst]

for i in range(len(sherenga_lst)):
    if sherenga_lst[i] < rost_petr:
        sherenga_lst.insert(i, rost_petr)
        break
    elif i == len(sherenga_lst): sherenga_lst.append(rost_petr)


print(f"{sherenga_lst}")
sherenga_lst = [str(item) for item in sherenga_lst]
result = " ".join(sherenga_lst)

output_file = open("output_sherenga.txt", "w")
output_file.write(result)
output_file.close()

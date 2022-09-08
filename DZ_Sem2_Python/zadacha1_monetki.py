# На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. 
# Определите минимальное число монеток, которые нужно перевернуть,
# чтобы все монетки были повернуты вверх одной и той же стороной.

# Входные данные
# В первой строке входного файла INPUT.TXT записано натуральное число N (1 ≤ N ≤ 100) 
# – число монеток. В каждой из последующих N строк содержится одно целое число – 1 если
# монетка лежит решкой вверх и 0 если вверх гербом.

# Выходные данные
# В выходной файл OUTPUT.TXT выведите минимальное количество монет, которые нужно перевернуть.

input_file = open("input_monetki.txt", "r")
orel = 0
reshka = 0
while True:
    m = input_file.readline()
    if not m:
        break
    else:
        if int(m) == 1:  reshka += 1
        elif int(m) == 0: orel += 1
input_file.close
if reshka > orel: chislo = orel
else: chislo = reshka
print(f"перевернуть надо {chislo} монет")

output_file = open("output_monetki.txt", "w")
output_file.write(str(chislo))
output_file.close()

# Требуется посчитать сумму целых чисел, расположенных между числами 1 и N включительно.

# Входные данные
# В единственной строке входного файла INPUT.TXT записано единственное целое число N, не превышающее по абсолютной величине 104.

# Выходные данные
# В единственную строку выходного файла OUTPUT.TXT нужно вывести одно целое число — сумму чисел, расположенных между 1 и N включительно.

sum = 0
input_file = open("input_summa.txt", "r")
n = input_file.readline()
input_file.close

for i in range(1, int(n) + 1):
    sum += i

print(f"сумма чисел от 1 до {n} включительно равна {sum}")

output_file = open("output_sum.txt", "w")
output_file.write(str(sum))
output_file.close()

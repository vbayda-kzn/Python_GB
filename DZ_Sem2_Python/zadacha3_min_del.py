# Требуется найти наименьший натуральный делитель целого числа N, отличный от 1.

# Входные данные
# Входной файл INPUT.TXT содержит целое число N (1 < N ≤ 106).

# Выходные данные
# В выходной файл OUTPUT.TXT выведите ответ на задачу.

input_file = open("input_min_del.txt", "r")
n = int(input_file.readline())
input_file.close

for i in range(2, n + 1):
    if n % i == 0:
        min_del = i
        break

print(f"минимальный натуральный делитель для числа {n}, (кроме 1) является число {min_del}")

output_file = open("output_min_del.txt", "w")
output_file.write(str(min_del))
output_file.close()

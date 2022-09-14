# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

n = int(input())
bin_list = []
flag = True

while n != 0:
    ost = n % 2
    n = n // 2
    bin_list.insert(0, str(ost))

print ("".join(bin_list))

# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) 
# многочлена и записать в файл многочлен степени k.

# Пример:
# k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

from random import randint


n = int(input())
c = randint(0, 100)

if c == 0:
    string_c = " = 0"
else: 
    string_c = " + " + str(c) + " = 0"

main_string =  string_c 
for i in range(1, n + 1):
    a = randint(0, 100)
    if a == 0:
        string_a = ""
    elif i == 1:
        string_a =  " + " + str(a) + "*x" 
    else:
        string_a =  " + " + str(a) + "*x**" + str(i)
    main_string =  string_a + main_string 


print(main_string[3:])
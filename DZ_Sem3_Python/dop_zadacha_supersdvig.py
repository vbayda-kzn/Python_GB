# Дана последовательность из N целых чисел и число K. Необходимо сдвинуть всю последовательность (сдвиг - циклический) на |K| элементов вправо, 
# если K – положительное и влево, если отрицательное.

my_list = [5, 3, 7, 4, 6]
n = int(input())
print (my_list)
for i in range(0, abs(n)):
    if n > 0:
        my_list.insert(0, my_list.pop())
    elif n < 0:
        my_list.append(my_list.pop(0))
    else:
        print("никто никуда не двигается")

print (my_list)



# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.




with open("symbols.txt", 'r', encoding="utf-8") as f: # "output.txt"
    string = f.read() + " "
rle_str = ""
count = 1
for i in range(1, len(string)):
    if string[i] != string[i-1]:
        rle_str = rle_str + (str(count) + string[i-1])
        count = 1
    else:
        count += 1

with open("output_symbols.txt", 'w', encoding="utf-8") as f: # "output.txt"
    f.write(rle_str)


print (string)
print (rle_str)
# Пам парам....
glassn = ['а', 'е', 'ё', 'и', 'о', 'у', 'ы','э', 'ю', 'я']
string = "Па-ра-рам пам-па-бам-пам"
list = string.split()
rythm = set()
print(list)


def pam_param(list):
    for e in list:
        rythm.add((len([i for i in e if i in glassn])))
    return len(rythm) == 1

print(pam_param(list))
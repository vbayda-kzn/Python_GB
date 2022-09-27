# Все равны как на подбор
values = [0, 2, 4, 6, 8, 10, 12]

def same_by(characteristic, object):
    count = 0
    for e in object:
        if characteristic(e) == 0:
            count += 1
    return len(object) == count

if same_by(lambda x: x % 2, values):
    print("True")
else:
    print("False")


# другое решение через списочное выражение (с семинара):
""" 
def same_by(characteristic, object):
    list_1 = [characteristic(el) for el in object]
    return len(object) == list_1.count(0)


values = [0, 2, 10, 6]
if same_by(lambda x: x % 2, values):
    print('same')
else:
    print('different')
 """

# другое сокращенное решение через списочное выражение (с семинара):
""" 
def same_by(characteristic, object):
    return len(object) == [characteristic(el) for el in object].count(0)

values = [0, 2, 10, 6]
if same_by(lambda x: x % 2, values):
    print('same')
else:
    print('different') """
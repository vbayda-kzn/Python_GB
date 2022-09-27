# Мимикрия

values = [2, 3, 5, 7, 11, 17, 19, 23, 29]
transformation = lambda x: x

transformation_values = list(map(transformation, values))
if values == transformation_values:
    print('ok')
else:
    print('fail')


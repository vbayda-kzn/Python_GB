# супертаблица


def print_operation_table(operation, num_rows = 9, num_columns = 9):
    for i in range(1, num_rows + 1):
        for j in range(1, num_columns + 1):
            print(f'{operation(i, j)}' + ' \t', end = '')
        print()

print_operation_table(lambda x, y: x * y, 5, 6)
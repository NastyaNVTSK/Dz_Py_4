def print_operation_table(operation, num_rows=6, num_columns=6):
    for i in range(1, num_rows + 1):
        for j in range(1, num_columns + 1):
            print(operation(i, j), end='\t')
        print()

def multiply(i, j):
    return i * j

print_operation_table(multiply, num_rows=6, num_columns=6)
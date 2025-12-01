def matrica(file_path):
    matrix = []
    with open(file_path, "r") as input_file:
        for line in input_file:
            row = [int(x) for x in line.split()]
            matrix.append(row)
    return matrix


def vivod(matrix, output_name):
    with open(output_name, "w") as out_file:
        for row in matrix:
            out_file.write(" ".join(map(str, row)) + "\n")


def sum_super_diag(matrix):
    total_sum = 0
    n = len(matrix) - 1
    for i in range(n):
        total_sum += matrix[i][i + 1]  # Сумма элементов над главной диагональю
    output_file = open('result.txt', 'w')
    output_file.write(str(total_sum))
    output_file.close()
    return total_sum

# matrix_data = matrica('vvod.txt')
# result = sum_super_diag(matrix_data)


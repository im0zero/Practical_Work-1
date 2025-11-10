#9.1
ss = [[1, 2, 3, 4], [1, 100, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4]]

k = 2

sp = []

for i in range(len(ss)):
    for j in range(len(ss)):
        if ss[i][j] % k == 0:
            sp.append(ss[i][j])

print(len(sp), max(sp))


#9.2
n = 3
matrix = [
    [1, 5, 3],
    [4, 9, 6],
    [7, 2, 8]
]

max_i = max_j = 0
for i in range(n):
    for j in range(n):
        if matrix[i][j] > matrix[max_i][max_j]:  # убрали abs
            max_i, max_j = i, j

new_matrix = []
for i in range(n):
    if i != max_i:
        row = []
        for j in range(n):
            if j != max_j:
                row.append(matrix[i][j])
        new_matrix.append(row)

print("Новая матрица:")
for row in new_matrix:
    print(row)

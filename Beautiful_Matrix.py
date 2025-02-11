def beautiful_matrix(matrix):
    for i in range(5):
        for j in range(5):
            if matrix[i][j] == 1:
                return abs(i - 2) + abs(j - 2)
matrix = []
for _ in range(5):
    matrix.append(list(map(int, input().split())))

print(beautiful_matrix(matrix))

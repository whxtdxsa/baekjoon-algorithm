import sys
def diffusion(r, c, matrix):
    acc_matrix = [[0 for _ in range(c)] for _ in range(r)]
    di = (1, 0, 0, -1)
    dj = (0, 1, -1, 0)

    for i in range(r):
        for j in range(c):
            dust = matrix[i][j]
            if dust >= 5:
                diffused_dust = dust // 5
                for k in range(4):
                    n_i = di[k] + i
                    n_j = dj[k] + j
                    if n_i < 0 or n_i >= r or n_j < 0 or n_j >= c: continue
                    if matrix[n_i][n_j] == -1: continue
                    acc_matrix[n_i][n_j] += diffused_dust
                    matrix[i][j] -= diffused_dust


    for i in range(r):
        for j in range(c):
            matrix[i][j] += acc_matrix[i][j]

    return matrix

def air_purification(circulator, r, c, matrix):
    c_r1, c_r2 = (circulator[0], circulator[1])
    # upper loop
    for i in range(c_r1 - 1, 0, -1):
        matrix[i][0] = matrix[i - 1][0]
    
    for j in range(c - 1):
        matrix[0][j] = matrix[0][j + 1]
    
    for i in range(0, c_r1):
        matrix[i][c - 1] = matrix[i + 1][c - 1]

    for j in range(c - 1, 1, -1):
        matrix[c_r1][j] = matrix[c_r1][j - 1]
    
    matrix[c_r1][1] = 0

    # lower loop
    for i in range(c_r2 + 1, r - 1):
        matrix[i][0] = matrix[i + 1][0]
    
    for j in range(c - 1):
        matrix[r - 1][j] = matrix[r - 1][j + 1]

    for i in range(r - 1, c_r2 - 1, -1):
        matrix[i][c - 1] = matrix[i - 1][c - 1]

    for j in range(c - 1, 1, -1):
        matrix[c_r2][j] = matrix[c_r2][j - 1]

    matrix[c_r2][1] = 0
    return matrix
def main():
    r, c, t = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(r)]
    circulator = []
    for i in range(r):
        if matrix[i][0] == -1: circulator.append(i)
    
    for _ in range(t):
        matrix = diffusion(r, c, matrix)
        matrix = air_purification(circulator, r, c, matrix)

    print(sum(sum(e) for e in matrix) + 2)

main()


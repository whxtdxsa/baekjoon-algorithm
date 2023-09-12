from collections import deque
import sys
read = sys.stdin.readline

def findStartPoint(n, m, matrix):
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 2: return i, j

def initByMinus(n, m, matrix):
    for i in range(n):
        for j in range(m):
            if matrix[i][j] != 0: matrix[i][j] = -1

def initByDistance(n, m, matrix):
    visited = [[False] * m for _ in range(n)]
    start_x, start_y = findStartPoint(n, m, matrix)
    
    visited[start_x][start_y] = True
    que = deque([(start_x, start_y, 0)])

    dx = [-1, 0, 0, 1]
    dy = [0, 1, -1, 0]

    initByMinus(n, m, matrix)
    printMatrix(matrix)
    while que:
        x, y, step = que.popleft()
        matrix[x][y] = step
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and matrix[nx][ny] != 0:
                visited[nx][ny] = True
                que.append((nx, ny, step + 1))

def printMatrix(matrix):
    for row in matrix: print(*row)

def main():
    n, m = map(int, read().split())
    matrix = [list(map(int, read().split())) for _ in range(n)]
    initByDistance(n, m, matrix)
    printMatrix(matrix)

main()
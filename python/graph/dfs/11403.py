import sys
read = sys.stdin.readline

def getLinks(n, matrix):
    links = [[] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if matrix[i][j] == 1: links[i].append(j)
    return links

def checkLinks(n, links):
    matrix = [[0] * n for _ in range(n)]
    def go(i, start):
        for j in links[i]:
            if matrix[start][j] == 1: continue
            matrix[start][j] = 1
            if j != start: go(j, start)
    for i in range(n): go(i, i)
    return matrix

def printMatrix(matrix):
    for row in matrix: print(*row)

def main():
    n = int(read())
    matrix = [list(map(int, read().split())) for _ in range(n)]
    links = getLinks(n, matrix)
    matrix_revised = checkLinks(n, links)
    printMatrix(matrix_revised)

main()

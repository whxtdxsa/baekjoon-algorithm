import sys
from collections import deque

def coloring(i, j, maps, n):
    res = 1
    dx = [0, 1, 0, -1]
    dy = [-1, 0, 1, 0]
    queue = deque([(i, j)])
    maps[i][j] = '0'

    while queue:
        x, y = queue.popleft()

        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if  0 <= nx < n and 0 <= ny < n and maps[nx][ny] == '1':
                res += 1
                maps[nx][ny] = '0'
                queue.append((nx, ny))
    return res

def numbering(maps, n):
    res = []
    for i in range(n):
        for j in range(n):
            if maps[i][j] == '1': res.append(coloring(i , j, maps, n))
    res.sort()
    return res

def getMaps(n):
    maps = [0] * n
    for _ in range(n): maps[_] = list(input())
    return maps

def main():
    n = int(input())
    maps = getMaps(n)
    res = numbering(maps, n)
    print(len(res))
    print(*res, sep = "\n")

main()

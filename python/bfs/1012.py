import sys
from collections import deque

def coloring(i, j, maps, m, n):
    dx = [0, 1, 0, -1]
    dy = [-1, 0, 1, 0]
    queue = deque([(i, j)])
    maps[i][j] = False

    while queue:
        x, y = queue.popleft()

        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if  0 <= nx < n and 0 <= ny < m and maps[nx][ny] == True:
                maps[nx][ny] = False
                queue.append((nx, ny))

def numbering(maps, m, n):
    res = 0
    for i in range(n):
        for j in range(m):
            if maps[i][j] == True:
                res += 1
                coloring(i, j, maps, m, n)
    return res

def getGround(m, n, k):
    maps = [[False] * m for _ in range(n)]
    for _ in range(k):
        x, y = map(int, sys.stdin.readline().split())
        maps[y][x] = True
    return maps

def main():
    t = int(input())
    for _ in range(t):
        m, n, k = map(int, input().split())
        maps = getGround(m, n, k)
        res = numbering(maps, m, n)
        print(res)

main()
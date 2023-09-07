import sys
from collections import deque

def initBox(m, n, h):
    box = [[0] * n for _ in range(h)]
    for i in range(h):
        for j in range(n): 
            box[i][j] = list(map(int, sys.stdin.readline().split()))
    return box
    
def tomatosInfo(box):
    que = deque()
    cnt = 0

    h = len(box)
    n = len(box[0])
    m = len(box[0][0])
    for i in range(h): 
        for j in range(n):
            for k in range(m):
                if box[i][j][k] == 1: que.append((i, j, k, 0))
                elif box[i][j][k] == 0: cnt += 1

    return que, cnt

def changingTomatos(box, que, cnt):
    if cnt == 0: return 0
    h = len(box)
    n = len(box[0])
    m = len(box[0][0])

    dz = [0, 0, -1, 0, 0, 1]
    dx = [1, 0, 0, -1, 0, 0]
    dy = [0, -1, 0, 0, 1, 0]
    while que:
        z, x, y, acc = que.popleft()
        for i in range(6):
            nz = z + dz[i]
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nz < h and 0 <= nx < n and 0 <= ny < m and box[nz][nx][ny] == 0:
                cnt -= 1
                if cnt == 0: return acc + 1
                box[nz][nx][ny] = 1
                que.append((nz, nx, ny, acc + 1))
    return -1
    
def main():
    m, n, h = map(int, input().split())
    box = initBox(m, n, h)
    que, cnt = tomatosInfo(box)
    res = changingTomatos(box, que, cnt)
    print(res)

main()
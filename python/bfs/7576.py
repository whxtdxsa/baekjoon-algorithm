from collections import deque

def initBox(m, n):
    box = [[0] for _ in range(n)]
    for _ in range(n): 
        box[_] = list(map(int, input().split()))
    return box
    
def tomatosInfo(box):
    que = deque()
    cnt = 0

    n = len(box)
    m = len(box[0])
    for i in range(n): 
        for j in range(m):
            if box[i][j] == 1: que.append((i, j, 0))
            elif box[i][j] == 0: cnt += 1

    return que, cnt

def changingTomatos(box, que, cnt):
    if cnt == 0: return 0
    n = len(box)
    m = len(box[0])

    dx = [1, 0, -1, 0]
    dy = [0, -1, 0, 1]
    while que:
        x, y, acc = que.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and box[nx][ny] == 0:
                cnt -= 1
                if cnt == 0: return acc + 1
                box[nx][ny] = 1
                que.append((nx, ny, acc + 1))
    return -1
    
def main():
    m, n = map(int, input().split())
    box = initBox(m, n)
    que, cnt = tomatosInfo(box)
    res = changingTomatos(box, que, cnt)
    print(res)

main()
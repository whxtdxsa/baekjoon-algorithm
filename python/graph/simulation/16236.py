import sys
from collections import deque

# 상어의 정보 초기화 (x, y, size)
def initShark(N, Matrix):
    for i in range(N):
        for j in range(N):
            if Matrix[i][j] == 9:
                Matrix[i][j] = 0
                return i, j, 2 

def bfs(shark_x, shark_y, shark_size, N, Matrix):
    visited = [[False] * N for _ in range(N)]
    visited[shark_x][shark_y] = True
    q = deque([(shark_x, shark_y, 0)])

    dx = [-1, 0, 0, 1]
    dy = [0, -1, 1, 0]

    res = []
    while q:
        x, y, t = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            
            # 상어 이동 조건
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and Matrix[nx][ny] <= shark_size:
                # 상어 먹이 조건
                if 0 < Matrix[nx][ny] < shark_size: 
                    res.append((nx, ny, t + 1))
                else:
                    q.append((nx, ny, t + 1))
                visited[nx][ny] = True
    if res:
        res.sort(key=lambda x: (x[2], x[0], x[1]))
        x, y, t = res[0]
        Matrix[x][y] = 0
        return (x, y, t)
    else: return None

def DinnerTime(N, Matrix):
    shark_x, shark_y, shark_size = initShark(N, Matrix)
    dinnerTime = 0
    eat_times = 0
    while True:
        res = bfs(shark_x, shark_y, shark_size, N, Matrix)
        if res == None: break
        else: 
            shark_x, shark_y = res[0], res[1]
            dinnerTime += res[2]
            eat_times += 1
            if eat_times == shark_size:
                shark_size += 1
                eat_times = 0

    return dinnerTime

def main():
    N = int(input())
    Matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
    res = DinnerTime(N, Matrix)
    print(res)

main()
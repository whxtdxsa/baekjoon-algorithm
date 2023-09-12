import sys
from collections import deque

def Maze(N, M, Matrix):
    if N == M == 1: return 1
    visited = [[False] * M for _ in range(N)]
    broken_visited = [[False] * M for _ in range(N)]
    visited[0][0] = True
    q = deque([(0, 0, 0, False)]) # (x, y, step, broken)

    dx = [1, 0, 0, -1]
    dy = [0, 1, -1, 0]

    while q:
        x, y, step, broken = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            # 종료 조건
            if nx == N - 1 and ny == M - 1: return step + 2

            # 이동 조건
            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny] and not broken:
                # 벽이 없을 때
                if Matrix[nx][ny] == 0:
                    visited[nx][ny] = True
                    q.append((nx, ny, step + 1, broken))
                # 벽이 있을 때
                elif Matrix[nx][ny] == 1:
                    broken_visited[nx][ny] = True
                    q.append((nx, ny, step + 1, True))

            if 0 <= nx < N and 0 <= ny < M and not broken_visited[nx][ny] and broken:
                # 벽이 없을 때
                if Matrix[nx][ny] == 0:
                    broken_visited[nx][ny] = True
                    q.append((nx, ny, step + 1, broken))

    return -1

def main():
    # 입력 처리
    N, M = map(int, sys.stdin.readline().split())
    Matrix = [[0] * M for _ in range(N)]
    for i in range(N):
        i_str = sys.stdin.readline()
        for j in range(M):
            Matrix[i][j] = int(i_str[j])

    res = Maze(N, M, Matrix)
    print(res)

main()
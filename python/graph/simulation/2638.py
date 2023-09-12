from collections import deque
import sys
read = sys.stdin.readline

def Cheeze(n, m, matrix):
    visited_count = [[0] * m for _ in range(n)]

    visited = [[True] * m] + [[False] * m for _ in range(n - 2)] + [[True] * m]
    for i in range(n - 2): visited[i + 1][0] = visited[i + 1][m - 1] = True

    q = deque()
    for i in range(m):
        q.append((0, i))
        q.append((n - 1, i))
    for i in range(n - 2):
        q.append((i + 1, 0))
        q.append((i + 1, m - 1))

    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    
    def bfs():
        cheezes = deque()
        while q:
            x, y = q.popleft()
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]

                if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                    if matrix[nx][ny] == 0:
                        q.append((nx, ny))
                        visited[nx][ny] = True

                    else:
                        visited_count[nx][ny] += 1
                        if visited_count[nx][ny] >= 2:
                            matrix[nx][ny] = 0
                            cheezes.append((nx, ny))
                            visited[nx][ny] = True
        return cheezes

    time = 0
    while True:
        cheezes = bfs()
        if not cheezes: break
        time += 1
        while cheezes: q.append(cheezes.popleft())

    return time

def main():
    n, m = map(int, read().split())
    matrix = [list(map(int, read().split())) for _ in range(n)]
    time = Cheeze(n, m, matrix)
    print(time)

main()
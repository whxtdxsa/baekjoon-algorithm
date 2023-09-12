from collections import deque

def initArr(n, m):
    arr = [[0] * (m + 2) for _ in range(n + 2)]
    for i in range(n):
        row = input()
        for j in range(m):
            arr[i + 1][j + 1] = int(row[j])
    return arr

def maze(arr, n, m):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    visited = [[False] * (m + 2) for _ in range(n + 2)]
    queue = deque([(1, 1, 1)])
    visited[1][1] = True

    while queue:
        x, y, steps = queue.popleft()

        if x == n and y == m: return steps

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if arr[nx][ny] == 1 and not visited[nx][ny]:
                visited[nx][ny] = True
                queue.append((nx, ny, steps + 1))

n, m = map(int, input().split())
arr = initArr(n, m)
res = maze(arr, n, m)
print(res)

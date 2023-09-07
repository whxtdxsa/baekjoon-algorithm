from collections import deque
import sys

def bfs(v, e, r):
    nodes = [[] for _ in range(n)]
    for _ in range(m):
        x, y = map(int, sys.stdin.readline().split())
        nodes[x - 1].append(y - 1)
        nodes[y - 1].append(x - 1)
    for i in nodes: i.sort(reverse = True)

    visited = [0] * v
    visited[r - 1] = 1
    queue = deque([r - 1])

    acc = 1
    while queue:
        u = queue.popleft()
        for i in nodes[u]:
            if visited[i] == 0:
                acc += 1
                visited[i] = acc
                queue.append(i)
    return visited

n, m, r = map(int, sys.stdin.readline().split())
res = bfs(n, m, r)
print(*res, sep="\n")
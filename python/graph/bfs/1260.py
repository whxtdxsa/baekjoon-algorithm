import sys
from collections import deque
sys.setrecursionlimit(10**6)

def getLinks(n, m):
    links = [[] for _ in range(n)]
    for _ in range(m):
        x, y = map(int,sys.stdin.readline().split())
        links[x - 1].append(y - 1)
        links[y - 1].append(x - 1)
    for _ in links: _.sort()
    return links

def dfs(links, v):
    visited = [False] * len(links)
    res = []
    def go(i):
        res.append(i + 1)
        visited[i] = True
        for _ in links[i]:
            if not visited[_]:
                go(_)
    go(v - 1)
    return res

def bfs(links, v):
    visited = [False] * len(links)
    visited[v - 1] = True
    res = [v]
    queue = deque([v - 1])
    while queue:
        i = queue.popleft()
        for _ in links[i]:
            if not visited[_]:
                res.append(_ + 1)
                visited[_] = True
                queue.append(_)
    return res

def printRes(res0, res1):
    print(*res0, end = "\n")
    print(*res1, end = "\n")

def main():
    n, m, v = map(int, input().split())
    links = getLinks(n, m)
    res0, res1 = dfs(links, v), bfs(links, v)
    printRes(res0, res1)

main()

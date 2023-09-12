import sys
sys.setrecursionlimit(10**6)
read = sys.stdin.readline

def getLoads(n, m):
    nodes = [[] for _ in range(n)]
    for _ in range(m):
        x, y = map(int, read().split(" "))
        nodes[x - 1].append(y - 1)
        nodes[y - 1].append(x - 1)
    for i in nodes: i.sort()
    return nodes

def visited(nodes, k):
    orders = [0] * n
    acc = 0
    def go(i):
        nonlocal acc
        if orders[i] == 0:
            acc += 1
            orders[i] = acc
            for j in nodes[i]: go(j)
    go(k - 1)
    return orders

n, m, r = map(int, read().split(" "))
nodes = getLoads(n, m)
res = visited(nodes, r)
print(*res, sep="\n")
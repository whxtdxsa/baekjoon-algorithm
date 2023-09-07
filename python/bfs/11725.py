import sys
from collections import deque

def initTree(n):
    tree = [[] for _ in range(n)]
    for _ in range(n - 1):
        h, t = map(int, sys.stdin.readline().split())
        tree[h - 1].append(t - 1)
        tree[t - 1].append(h - 1)
    return tree

def getHeads(tree):
    heads = [-1] * len(tree)
    que = deque([0])
    while que:
        h = que.popleft()
        for i in tree[h]:
            if heads[i] == -1:
                heads[i] = h + 1
                que.append(i)
    return heads[1:]

def main():
    tree = initTree(int(input()))
    res = getHeads(tree)
    print(*res, sep = "\n")

main()
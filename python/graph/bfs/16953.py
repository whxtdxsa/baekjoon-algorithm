from collections import deque

def AtoB(a, b):
    que = deque([(a, 0)])
    while que:
        x, step = que.popleft()
        n1, n2 = x * 2, x * 10 + 1
        if n1 == b or n2 == b: return step + 2
        if n1 < b: que.append((n1, step + 1))
        if n2 < b: que.append((n2, step + 1))
    return -1

def main():
    a, b = map(int, input().split())
    res = AtoB(a, b)
    print(res)

main()
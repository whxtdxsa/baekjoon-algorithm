from collections import deque

def seek(n, k):
    max = 100000
    visited = [False] *  (2 * max)
    visited[n] = True
    queue = deque([(n, 0)])

    while queue:
        x, time = queue.popleft()
        if x == k: return time
        dx = [x - 1, x + 1, 2 * x]
        for i in dx:
            if 0 <= i and i < 2 * max  and not visited[i]:
                visited[i] = True
                queue.append((i, time + 1))

def main():
    n, k = map(int, input().split())
    res = seek(n, k)
    print(res)

main()
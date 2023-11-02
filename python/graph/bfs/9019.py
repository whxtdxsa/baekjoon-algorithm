from collections import deque
import sys
read = sys.stdin.readline

def operators(n):
    def D(n): return (2 * n) % 10000
    def S(n): return (9999 + n) % 10000
    def L(n): return (n % 1000) * 10 + n // 1000
    def R(n): return (n % 10) * 1000 + n // 10
    return (D(n), "D"), (S(n), "S"), (L(n), "L"), (R(n), "R")

def DSLR(a, b):
    visited = [False] * 10000
    visited[a] = 0
    que = deque([(a, "")])

    while que:
        c_n, c_op = que.popleft()
        n_modified = operators(c_n)
        for n, op in n_modified:
            if n == b: return c_op + op
            if visited[n]: continue
            visited[n] = True
            que.append((n, c_op + op))

    return -1

def main():
    a, b = map(int, read().split())
    print(DSLR(a, b))
    
for _ in range(int(read())): main()
import heapq

def main():
    n = int(input())
    m = int(input())
    d_matrix = [[float('inf') for _ in range(n)] for _ in range(n)]

    for _ in range(m):
        s, e, w = map(int, input().split())
        d_matrix[s - 1][e - 1] = min(w, d_matrix[s - 1][e - 1])
    s, e = map(lambda x: int(x) - 1, input().split())

    visited = 0
    que = []
    heapq.heappush(que, (0, s, [s + 1]))
    
    while que:
        d, n1, load = heapq.heappop(que)
        if visited & 1 << n1: continue
        visited |= 1 << n1
        if n1 == e: 
            print(d)
            print(len(load))
            print(*load, sep = ' ')
            return
        for n2 in range(n):
            w = d_matrix[n1][n2]
            if w == float('inf'): continue
            heapq.heappush(que, (w + d, n2, load + [n2 + 1]))

main() 
    

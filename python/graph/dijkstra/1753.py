import sys
import heapq

def dijkstra(graph, start):
    d = [float('inf')] * (len(graph))
    d[start] = 0

    queue = []
    heapq.heappush(queue, (0, start))

    while queue:
        curr_d, curr_p = heapq.heappop(queue)
        
        if curr_d > d[curr_p]: continue

        for neighbor_p, neighbor_w in graph[curr_p]:
            if neighbor_w + curr_d < d[neighbor_p]:
                d[neighbor_p] = neighbor_w + curr_d
                heapq.heappush(queue, (neighbor_w + curr_d, neighbor_p))

    return d[1:]

def main():
    V, E = map(int, sys.stdin.readline().split())
    K = int(input())

    graph = [[] for _ in range(V + 1)]
    for _ in range(E):
        u, v, w = map(int, sys.stdin.readline().split())
        graph[u].append((v, w))
    
    d = dijkstra(graph, K)
    print(*map(lambda x: x if x != float('inf') else "INF", d), sep = "\n")

main()
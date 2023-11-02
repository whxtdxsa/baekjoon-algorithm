import sys
import heapq

def dijkstra(graph, start, end):
    d = [(float('inf'), []) for _ in range(len(graph))]
    d[start] = (0, [start])

    queue = []
    heapq.heappush(queue, (0, start))

    while queue:
        curr_d, curr_p = heapq.heappop(queue)

        if curr_d > d[curr_p][0]: 
            continue

        for neighbor_p, neighbor_w in graph[curr_p]:
            if neighbor_w + curr_d < d[neighbor_p][0]:
                new_d = neighbor_w + curr_d
                new_path = d[curr_p][1] + [neighbor_p]
                d[neighbor_p] = (new_d, new_path)
                heapq.heappush(queue, (new_d, neighbor_p))

    return d[end]

def main():
    n = int(input())
    m = int(input())

    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        start_p, end_p, w = map(int, sys.stdin.readline().split())
        graph[start_p].append((end_p, w))

    start, end = map(int, sys.stdin.readline().split())
    d, root = dijkstra(graph, start, end)
    print(d)
    print(len(root))
    print(*root, sep = " ")

main()
import sys
import heapq

def dijkstra(graph, start):
    # 무한대의 거리 값으로 초기화
    distances = [float('inf')] * (N + 1)
    distances[start] = 0

    # 우선순위 큐 사용
    queue = []
    heapq.heappush(queue, (0, start))

    while queue:
        current_distance, current_node = heapq.heappop(queue)

        # 현재 노드까지의 거리가 이미 더 짧은 경우 무시
        if distances[current_node] < current_distance:
            continue

        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight

            # 더 짧은 경로를 찾았을 때 업데이트
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(queue, (distance, neighbor))

    return distances

# 입력 받기
N = int(input())
M = int(input())

graph = [[] for _ in range(N + 1)]

for _ in range(M):
    start, end, cost = map(int, sys.stdin.readline().split())
    graph[start].append((end, cost))

start_point, end_point = map(int, sys.stdin.readline().split())

# 다익스트라 알고리즘 적용
distances = dijkstra(graph, start_point)

# 구간 도착점의 최소비용 출력
print(distances[end_point])
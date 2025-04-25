import heapq

def find_shorted_way(s, e, matrix, n):
    visited = 0
    que = []
    for i in range(n):
        d = matrix[s][i]
        if d != float('inf'):
            heapq.heappush(que, (d, i))
    
    while que:
        s_d, s_i = heapq.heappop(que)
        if s_i == e: return s_d

        if visited & 1 << s_i: continue
        visited |= 1 << s_i

        for e_i in range(n):
            d = matrix[s_i][e_i]
            if d != float('inf'):
                heapq.heappush(que, (d + s_d, e_i))
    
    return -1

def main():
    n, e = map(int, input().split())
    d_matrix = [[float('inf') for _ in range(n)] for _ in range(n)]

    for _ in range(e):
        a, b, c = map(int, input().split())
        d_matrix[a - 1][b - 1] = c
        d_matrix[b - 1][a - 1] = c
    for i in range(n):
        d_matrix[i][i] = 0
        
    v1, v2 = map(lambda x: int(x) - 1, input().split())
    

    s_to_v1 = find_shorted_way(0, v1, d_matrix, n)
    s_to_v2 = find_shorted_way(0, v2, d_matrix, n)
    
    v1_to_v2 = find_shorted_way(v1, v2, d_matrix, n)

    v1_to_e = find_shorted_way(v1, n - 1, d_matrix, n)
    v2_to_e = find_shorted_way(v2, n - 1, d_matrix, n)
    
    way1 = float('inf')
    way2 = float('inf')

    if s_to_v1 != -1 and v1_to_v2 != -1 and v2_to_e != -1: 
        way1 = s_to_v1 + v1_to_v2 + v2_to_e
    
    if s_to_v2 != -1 and v1_to_v2 != -1 and v1_to_e != -1: 
        way2 = s_to_v2 + v1_to_v2 + v1_to_e
    if way1 == float('inf') and way2 == float('inf'): 
        best_way = -1
    else:
        best_way = min(way1, way2)
    print(best_way)

main()

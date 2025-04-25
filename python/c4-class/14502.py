import sys
from collections import deque

def virus(n, m, matrix):
    nm = n * m
    def set_wall(c0, c1, c2):
        if c1 == nm - 2 and c2 == nm - 1:
            c0 += 1
            c1 = c0 + 1
            c2 = c0 + 2
        elif c2 == nm - 1:
            c1 += 1
            c2 = c1 + 1
        else:
            c2 += 1
        return c0, c1, c2
    
    def dim_transformer(c):
        y = c // m
        x = c % m
        return y, x
    
    final_cnt_walls = 3
    final_cnt_virus = float('inf') 
    
    init_que = set()
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 2:
                init_que.add((i, j))
            elif matrix[i][j] == 1:
                final_cnt_walls += 1
    dx = (1, 0, 0, -1)
    dy = (0, 1, -1, 0)
    c0, c1, c2 = (0, 1, 2)
    temp = []
    while c0 != nm - 2:
        cnt_virus = 0
        y0, x0 = dim_transformer(c0)
        y1, x1 = dim_transformer(c1)
        y2, x2 = dim_transformer(c2)
        if matrix[y0][x0] == 0 and matrix[y1][x1] == 0 and matrix[y2][x2] == 0:
            matrix[y0][x0] = 1
            matrix[y1][x1] = 1
            matrix[y2][x2] = 1
            
            que = deque()
            for e in init_que:
                que.append(e)
            visited = set()

            while que:
                y, x = que.popleft()
                if (y, x) in visited: continue
                visited.add((y, x))
                cnt_virus += 1
                for i in range(4):
                    n_y = y + dy[i]
                    n_x = x + dx[i]
                    if n_y < 0 or n_y >= n or n_x < 0 or n_x >= m: continue
                    if matrix[n_y][n_x] != 0: continue
                    que.append((n_y, n_x))
            matrix[y0][x0] = 0
            matrix[y1][x1] = 0
            matrix[y2][x2] = 0
            final_cnt_virus = min(final_cnt_virus, cnt_virus)
        c0, c1, c2 = set_wall(c0, c1, c2)
    return nm - (final_cnt_virus + final_cnt_walls)


def main():
    input = sys.stdin.readline
    n, m = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(n)]
    res = virus(n, m, matrix)
    print(res)
main()

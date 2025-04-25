def moving_pipe(room):
    visited = {}
    n = len(room)
    def dfs(phase, current_loc):
        c_i, c_j = current_loc
        if (phase, c_i, c_j) in visited: 
            return visited[(phase, c_i, c_j)]

        if c_i == n - 1 and c_j == n - 1: return 1
        acc = 0
        if phase == 1:
            if c_j + 1 < n and room[c_i][c_j + 1] == 0:
                acc += dfs(1, (c_i, c_j + 1))
                if c_i + 1 < n and room[c_i + 1][c_j] == 0 and room[c_i + 1][c_j + 1] == 0:
                    acc += dfs(3, (c_i + 1, c_j + 1))

        elif phase == 2:
            if c_i + 1 < n and room[c_i + 1][c_j] == 0:
                acc += dfs(2, (c_i + 1, c_j))
                if c_j + 1 < n and room[c_i][c_j + 1] == 0 and room[c_i + 1][c_j + 1] == 0:
                    acc += dfs(3, (c_i + 1, c_j + 1))

        else:
            t1 = False
            t2 = False
            if c_j + 1 < n and room[c_i][c_j + 1] == 0:
                acc += dfs(1, (c_i, c_j + 1))
                t1 = True
            if c_i + 1 < n and room[c_i + 1][c_j] == 0:
                acc += dfs(2, (c_i + 1, c_j))
                t2 = True
            if t1 and t2 and room[c_i + 1][c_j + 1] == 0:
                acc += dfs(3, (c_i + 1, c_j + 1))

        visited[(phase, c_i, c_j)] = acc
        return acc
    
    return dfs(1, (0, 1))

import sys
def main():
    input = sys.stdin.readline
    n = int(input())
    room = [list(map(int, input().split())) for _ in range(n)]
    res = moving_pipe(room)
    print(res)


main()


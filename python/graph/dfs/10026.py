import sys

def dfs(grid, x, y, N, color, visited):
    if x < 0 or x >= N or y < 0 or y >= N or visited[x][y] or grid[x][y] not in color:
        return False
    
    visited[x][y] = True
    # 상하좌우 탐색
    dfs(grid, x+1, y, N, color, visited)
    dfs(grid, x-1, y, N, color, visited)
    dfs(grid, x, y+1, N, color, visited)
    dfs(grid, x, y-1, N, color, visited)
    
    return True

def solve(grid, N, color_blind=False):
    visited = [[False] * N for _ in range(N)]
    count = 0

    if color_blind:
        for i in range(N):
            for j in range(N):
                if not visited[i][j]:
                    color = ['B']
                    if grid[i][j] in ['R', 'G']:
                        color = ['R', 'G']

                    if dfs(grid, i, j, N, color, visited):
                      count += 1                  

    else:
        for i in range(N):
            for j in range(N):
                if not visited[i][j]:
                    if dfs(grid, i, j, N, list(grid[i][j]), visited):
                        count += 1
    
    return count

def main():
    sys.setrecursionlimit(10000)
    input = sys.stdin.readline
    
    N = int(input().rstrip())
    grid = [input().rstrip() for _ in range(N)]

    human = solve(grid, N)
    cow = solve(grid, N, True)
    print(human, cow)

if __name__ == "__main__":
    main()
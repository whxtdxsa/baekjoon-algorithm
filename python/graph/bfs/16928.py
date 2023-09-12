from collections import deque
def initMaps(n, m):
    maps = [0] * 101
    for i in range(n + m):
        f, s = map(int, input().split())
        maps[f] = s
    return maps

def movePlayer(maps):
    que = deque([(1, 0)])
    while que:
        x, times = que.popleft()
        for i in range(6):
            nx = x + i + 1
            if nx == 100: return times + 1
            elif 0 < nx < 100 and maps[nx] != -1:
                if maps[nx] == 0: que.append((nx, times + 1))
                elif maps[nx] != 0: que.append((maps[nx], times + 1))
                maps[nx] = -1
                
def main():
    n, m = map(int, input().split())
    maps = initMaps(n, m)
    res = movePlayer(maps)
    print(res)

main()
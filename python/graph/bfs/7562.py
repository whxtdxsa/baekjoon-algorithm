from collections import deque

def initBoard(l): return [[0] * l for _ in range(l)]

def moveKight(curr_k, goal_k, board):
    size = len(board)
    board[curr_k[0]][curr_k[1]] = 1
    que = deque([(curr_k[0], curr_k[1], 0)])

    dx = [1, 2, 2, 1, -1, -2, -2, -1]
    dy = [2, 1, -1, -2, -2, -1, 1, 2]

    while que:
        x, y, acc = que.popleft()
        if x == goal_k[0] and y == goal_k[1]: return acc

        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < size and 0 <= ny < size and board[nx][ny] == 0:
                board[nx][ny] = 1
                que.append((nx, ny, acc + 1))

def main():
    board = initBoard(int(input()))
    curr_k = list(map(int, input().split()))
    goal_k = list(map(int, input().split()))
    res = moveKight(curr_k, goal_k, board)
    print(res)

t_case = int(input())
for _ in range(t_case): main()
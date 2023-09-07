import sys
read = sys.stdin.readline
write = sys.stdout.write

n, m, q = map(int, read().split(" "))

mat = [[0] * m for _ in range(n)]
que1 = [0] * n
que2 = [0] * m

for i in range(q): 
    op, li, v= map(int, read().split(" "))
    if (op == 1): que1[li - 1] += v
    else: que2[li - 1] += v

def addRow(q): 
    for i in range(n): mat[i] = list(map(lambda x: x + q[i], mat[i]))
def addColumn(q):
    for i in range(n): mat[i] = list(map(lambda x, y: x + y, mat[i], q))
addRow(que1)
addColumn(que2)

for row in mat:
    write(" ".join(map(str, row)) + "\n")
from collections import deque
import sys
read = sys.stdin.readline

def AC(op, num_deq):
    reverse = False
    for c in op:
        if c == 'R': 
            if reverse: reverse = False
            else: reverse = True
        else:
            if not num_deq: 
                print("error")
                return
            
            if not reverse: num_deq.popleft()
            else: num_deq.pop()
    
    if reverse: num_deq.reverse()
    print("[" + ','.join(map(str, num_deq)) + "]")
    return

def toDeq(n, num_string):
    if n == 0: return deque()
    return deque(map(int, num_string))

def main():
    op = read().rstrip()
    n = int(read())
    num_string = read().rstrip()[1:-1].split(',')
    num_deq = toDeq(n, num_string)
    AC(op, num_deq)

for _ in range(int(read())): main()


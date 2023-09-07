import sys
from collections import deque

def stack(s,ord):
    if ord[0] == "push": s.append(ord[1])
    elif ord[0] == "pop": 
        if s: print(s.popleft())
        else: print(-1)
    elif ord[0] == "size": print(len(s))
    elif ord[0] == "empty": print(int(not s))
    elif ord[0] == "front": 
        if s: print(s[0])
        else: print(-1)
    else:
        if s: print(s[-1])
        else: print(-1)

def main():
    s = deque()
    for _ in range(int(input())): stack(s, sys.stdin.readline().split())

main()
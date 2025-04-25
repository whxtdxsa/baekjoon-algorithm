import sys
from collections import deque
def main():
    input = sys.stdin.readline
    n, m = map(int, input().split())
    true_list = list(map(lambda x: int(x) - 1, input().split()[1:]))
    parties = [list(map(lambda x: int(x) - 1, input().split()[1:])) for _ in range(m)]

    nodes = [set() for _ in range(n)]
    for party in parties:
        for i in range(len(party) - 1):
            nodes[party[i]].add(party[i + 1]) 
            nodes[party[i + 1]].add(party[i])

    
    visited = 0
    que = deque()
    true_set = set()
    for trues in true_list:
        true_set.add(trues)
        que.append(trues)
        visited |= 1 << trues
    while que:
        p = que.popleft()
        
        for e in nodes[p]:
            if visited & 1 << e: continue     
            visited |= 1 << e
            true_set.add(e)
            que.append(e)
    total = 0
    for party in parties:
        t = 1
        for i in range(len(party)):
            if party[i] in true_set: t = 0

        total += t
    print(total)
            



main()


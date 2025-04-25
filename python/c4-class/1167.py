import sys
def main():
    readline = sys.stdin.readline
    n = int(readline())
    nodes = [[] for _ in range(n)]
    
    for _ in range(n):
        edge_info = list(map(int, readline().split()))
        for i in range(1, len(edge_info), 2):
            if edge_info[i] == -1: break
            nodes[edge_info[0] - 1].append((edge_info[i] - 1, edge_info[i + 1])) # (end, weight)
        
    res = find_max_distance(nodes)
    print(res)

def find_max_distance(tree):
    visited = [0] * len(tree)
    s = set()
    
    def loop(root):
        visited[root] = 1
        m1 = 0
        m2 = 0
        for e, w in tree[root]:
            if visited[e]: continue
            res = loop(e)
            if res + w > m1: 
                m2 = m1
                m1 = res + w
            elif res + w > m2:
                m2 = res + w

        s.add(m1 + m2)
        return m1

    loop(0)
    return max(s)

sys.setrecursionlimit(10**6)
main()

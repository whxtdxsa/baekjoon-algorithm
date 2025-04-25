class Node:
    def __init__(self, data):
        self.data = data
        self.child_list = set()
        
import sys
def main():
    readline = sys.stdin.readline
    n = int(readline())

    nodes = [Node(0) for i in range(n)]

    for _ in range(n - 1):
        parent, child, weight = map(int, readline().split()) 
        nodes[parent - 1].child_list.add(child - 1)
        nodes[child - 1].data = weight
    
    res = find_max_distance(nodes)
    print(res)

def find_max_distance(tree):
    s = set()

    def loop(root):
        dist_list = [loop(tree[i]) + tree[i].data for i in root.child_list]
        if len(dist_list) <= 1: 
            dist_list.append(0)
            dist_list.append(0)

        dist_list.sort()
        s.add(dist_list[-1] + dist_list[-2])
        return dist_list[-1]
    loop(tree[0])
    return max(s)
sys.setrecursionlimit(10**6)
main()



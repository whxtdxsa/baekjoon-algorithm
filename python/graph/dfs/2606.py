import sys
def getLinks(n_com, n_net):
    links = [[] for _ in range(n_com)]
    for _ in range(n_net):
        a, b = map(int, sys.stdin.readline().split())
        links[a - 1].append(b - 1)
        links[b - 1].append(a - 1)
    return links

def virus(links):
    visited = [False] * len(links)
    def go(i):
        visited[i] = True
        for _ in links[i]:
            if not visited[_]: go(_)
    go(0)
    return visited.count(True) - 1

def main():
    n_com, n_net = map(int, (input(), input()))
    links = getLinks(n_com, n_net)
    res = virus(links)
    print(res)

main()
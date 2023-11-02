import heapq
import sys
read = sys.stdin.readline

def deleting(num_list):
    if num_list: return heapq.heappop(num_list)[1]
    return 0

def pushing(num, num_list):
    heapq.heappush(num_list, (abs(num), num))

def main():
    n = int(read())
    num_list = []
    for _ in range(n):
        num = int(read())
        if num == 0: print(deleting(num_list))
        else: pushing(num, num_list)

main()
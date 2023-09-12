import sys
read = sys.stdin.readline

def findMaxLan(lan_list, n):
    minimum = 1
    maximum = max(lan_list) + 1
    while maximum - minimum > 1:
        mid = (maximum + minimum) // 2
        lan_sum = sum(list(map(lambda x: x // mid, lan_list)))

        if lan_sum < n: maximum = mid
        else: minimum = mid

    return minimum

def main():
    k, n = map(int, read().split())
    lan_list = [int(read()) for _ in range(k)]
    res = findMaxLan(lan_list, n)
    print(res)
    
main()
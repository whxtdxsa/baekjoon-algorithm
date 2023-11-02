import math
import sys
read = sys.stdin.readline

def findYear(m, n, x, y):
    lcm = m * n // math.gcd(m, n)
    nums = sorted([(m, x), (n, y)])
    for k in range(nums[1][1], lcm + 1, nums[1][0]):
        if (k - 1) % nums[0][0] + 1 == nums[0][1]: return k
    return -1

def main():
    m, n, x, y = map(int, read().split())
    res = findYear(m, n, x, y)
    print(res)

t = int(read())
for _ in range(t): main()
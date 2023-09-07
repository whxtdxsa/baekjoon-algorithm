import sys
def nAndM12(x, y, nums):
    def go(n, acc, prev):
        if n == 0:
            print(*acc, sep = " ")
            return
        for i in range(prev, x):
            if i == 0 or nums[i - 1] != nums[i]: go(n - 1, acc + [nums[i]], i)
    go(y, [], 0)

def main():
    x, y = map(int, input().split())
    nums = sorted(list(map(int, sys.stdin.readline().split())))
    nAndM12(x, y, nums)

main()
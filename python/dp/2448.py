import math
def star(n):
    dp= ["  *  ", " * * ", "*****"]
    for i in range(n):
        d = len(dp)
        dp = (
            list(map(lambda x: " " * d + x + " " * d, dp))
            + list(map(lambda x: x + " " + x, dp))
        )
    return dp

def main():
    n = int(math.log(int(input()) // 3, 2))
    res = star(n)
    print(*res, sep = "\n")

main()
import math
import sys
def get_power(a, b, p): # return a ** b
    if b == 0: return 1
    elif b == 1: return a
    else:
        sqrt_a = get_power(a, b // 2, p)
        powered_a = (sqrt_a * sqrt_a) % p
        if b % 2 == 0:
            return powered_a
        else:
            return (powered_a * a) % p
    
def get_relatively_prime(a, b):
    d = math.gcd(a, b)
    return a // d, b // d

def main():
    m = int(input())
    p = 1000000007
    total = 0
    for _ in range(m):
        n, s = map(int, input().split())
        a, b = get_relatively_prime(n, s)
        res = (b * get_power(a, p - 2, p)) % p
        total = (total + res) % p

    print(total)

sys.setrecursionlimit(10**5)
main()

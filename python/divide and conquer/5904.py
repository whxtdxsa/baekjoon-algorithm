def MooLen(n):
    def go(i, preLen, currLen):
        if currLen >= n: return (i - 1, preLen)
        else: return go(i + 1, currLen, currLen * 2 + i + 3)
    return go(1, 0, 3)

def findChar(n):
    i, prev = MooLen(n)
    if n <= prev + i + 3:
        if n == prev + 1: return "m"
        else: return "o"
    else: return findChar(n - prev - i - 3)

def main():
    n = int(input())
    print(findChar(n))

main()
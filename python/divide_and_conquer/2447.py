def star10(n):
    args = ["***", "* *", "***"]

    def go(i, args):
        if i == 3: return args
        else:
            bound = list(map(lambda x: x * 3, args))
            mid = list(map(lambda x: x + " " * len(x) + x, args))
            return go(i / 3, bound + mid + bound)

    return go(n, args)

def main():
    n = int(input())
    res = star10(n)
    print(*res, sep = "\n")

main()
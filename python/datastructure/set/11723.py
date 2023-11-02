import sys
read = sys.stdin.readline
def setOp(set0, operation, value=None):
    if operation == "add":
        set0.add(value)
    elif operation == "remove":
        set0.discard(value)
    elif operation == "check":
        print(int(value in set0))
    elif operation == "toggle":
        if value in set0:
            set0.discard(value)
        else:
            set0.add(value)
    elif operation == "all":
        set0.update(range(1, 21))
    elif operation == "empty":
        set0.clear()

def main():
    m = int(read())
    set0 = set()
    for _ in range(m):
        command, *args = read().split()
        if args:
            setOp(set0, command, int(args[0]))
        else:
            setOp(set0, command)

if __name__ == "__main__":
    main()
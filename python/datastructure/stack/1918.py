def ordering(c):
    if c == '+' or c == '-': return 0
    elif c == '*' or c == '/': return 1
    else: return 2

def toPostfix(str):
    cList, oList = [], []
    ops = ['+', '-', '*', '/', '(', ')']
    for c in str:
        if not c in ops: cList.append(c)
        else:
            if c == '(': oList.append(c)
            elif c == ')':
                while oList[-1] != '(': cList.append(oList.pop())
                oList.pop()
            else:
                while oList and oList[-1] != '(' and ordering(c) <= ordering(oList[-1]): cList.append(oList.pop())
                oList.append(c)

    while oList: cList.append(oList.pop())
    return cList

def main():
    str = input()
    cList = toPostfix(str)
    print(*cList, sep = '')
    
main()
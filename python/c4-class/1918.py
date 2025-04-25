def get_op_rank(op):
    if op == '+' or op == '-': 
        return 1
    elif op == '*' or op == '/':
        return 0
    else:
        return 2

def invert_expression(s):
    var_stack = []
    op_stack = []
    op_tuple = ('+', '-', '*', '/', '(', ')')
    for c in s:
        if c in op_tuple:
            if c == ')':
                while op_stack:
                    op = op_stack.pop()
                    if op == '(': break
                    var_stack.append(op)
            elif c == '(':
                op_stack.append(c)
            else:
                if op_stack and get_op_rank(c) >= get_op_rank(op_stack[-1]):
                    while op_stack:
                        if op_stack[-1] == '(': break
                        if get_op_rank(c) < get_op_rank(op_stack[-1]): break
                        var_stack.append(op_stack.pop())
                
                op_stack.append(c)
        else:
            var_stack.append(c)
    
    while op_stack:
        var_stack.append(op_stack.pop())
    return ''.join(var_stack) 
    
def main():
    s = input()
    res = invert_expression(s)
    print(res)

main()


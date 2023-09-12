import sys
read = sys.stdin.readline

def stackSeq(nums_seq):
    nums_stack = [0]
    operator_list = []
    curr_num = 0

    for i in nums_seq:
        if nums_stack[-1] > i: return ["NO"]

        if nums_stack[-1] < i:
            while curr_num != i:
                # Push
                curr_num += 1
                nums_stack.append(curr_num)
                operator_list.append("+")
        # Pop
        nums_stack.pop()
        operator_list.append("-")
    return operator_list

def main():
    # Get input
    n = int(read())
    nums_seq = [int(read()) for _ in range(n)]
    res = stackSeq(nums_seq)
    print(*res, sep = "\n")

main()
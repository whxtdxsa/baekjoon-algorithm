def exist_on_main_list(main_list, e, start_index, n):
    for i in range(start_index, n):
        if main_list[i] == e: return i
    return None



def get_lcs(n, main_list, m, flag_list):
    index_list = [None for _ in range(m)]
    kernel_list = [None for _ in range(m)]

    start_kernel = 0
    for i in range(m):
        e = flag_list[i]
        prev_kernel = None
        curr_kernel = start_kernel

        while True:
            if flag_list[curr_kernel] < e: # foound sup(e)
                if prev_kernel is None:
                    start_index = 0
                    target_index = exist_on_main_list(main_list, e, start_index, n)
                    if target_index is not None:
                        start_kernel = i
                        index_list[i] = target_index
                else:
                    start_index = index_list[prev_kernel] + 1
                    target_index = exist_on_main_list(main_list, e, start_index, n)
                    if target_index is not None:
                        kernel_list[prev_kernel] = i
                        index_list[i] = target_index
                break
            else:
                prev_kernel = curr_kernel
                curr_kernel = kernel_list[curr_kernel]
                if curr_kernel is None:
                    if index_list[prev_kernel] is None:
                        start_index = 0
                        target_index = exist_on_main_list(main_list, e, start_index, n)
                        if target_index is not None:
                            start_kernel = i
                            index_list[i] = target_index

                    else:
                        start_index = index_list[prev_kernel] + 1
                        target_index = exist_on_main_list(main_list, e, start_index, n)
                        if target_index is not None:
                            kernel_list[prev_kernel] = i
                            index_list[i] = target_index
                    break                    
    total = 1
    res = []
    if index_list[start_kernel] is None:
        print(0)
        return
    c = start_kernel
    for i in range(n):
        res.append(flag_list[c])
        c = kernel_list[c]
        if c is None: 

            print(len(res))
            print(*res, sep = ' ')
            return
import sys
def main():
    n = int(input())
    main_list = list(map(int, input().split()))
    m = int(input())
    flag_list = list(map(int, input().split()))
    get_lcs(n, main_list, m, flag_list)
main() 

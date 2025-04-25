def explosion(m_str, e_str):
    length_of_m_str = len(m_str)
    length_of_e_str = len(e_str)

    head = 0
    kernel = [None for _ in range(len(m_str))]
    
    if length_of_e_str == 1:
        for i in range(length_of_m_str):
            if m_str[i] == e_str:
                kernel[i] = i + 1
        return kernel

    while True:
        curr_id = head - 1
        is_same = 1
        for i in range(length_of_e_str):
            curr_id += 1
            if curr_id >= length_of_m_str:
                return kernel
            while kernel[curr_id] is not None:
                curr_id = kernel[curr_id]
            if m_str[curr_id] != e_str[i]:
                is_same = 0
                break

        if is_same:
            curr_id += 1

            kernel[head] = curr_id
            kernel[curr_id - 1] = head - 1
        
            if curr_id >= length_of_m_str:
                return kernel
            
            for i in range(length_of_e_str - 1):
                prev = curr_id
                curr_id -= 1
                while kernel[curr_id] is not None:
                    curr_id = kernel[curr_id]
                
                if curr_id == -1:
                    curr_id = prev
                    break

            head = curr_id
        else:
            head += 1
            if head + length_of_e_str -1 >= length_of_m_str: return kernel
            while kernel[head] is not None:
                head = kernel[head]

import sys
def main():
    m_str = input() # main string
    e_str = input() # explosion string
    length_of_m_str = len(m_str)
    kernel = explosion(m_str, e_str)

    curr_id = -1
    len_of_res = 0
    while True:
        curr_id += 1
        if curr_id == length_of_m_str: 
            if len_of_res == 0: sys.stdout.write('FRULA')
            sys.stdout.write('\n')
            return
        while kernel[curr_id] is not None:
            curr_id = kernel[curr_id]
            if curr_id == length_of_m_str: 
                if len_of_res == 0: sys.stdout.write('FRULA')
                sys.stdout.write('\n')
                return   
        len_of_res += 1
        sys.stdout.write(m_str[curr_id])
    print()

main()

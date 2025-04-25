import sys
def alphabet(r, c, matrix):
    max_len = 1
    di = (1, 0, 0, -1)
    dj = (0, 1, -1, 0)
    
    def loop(i, j, visited_mask, current_len):
        nonlocal max_len
        char_index = ord(matrix[i][j]) - ord('A')
        if (visited_mask >> char_index) & 1: 
            max_len = max(max_len, current_len)
            return

        new_mask = visited_mask | (1 << char_index)
        current_len += 1
        
        for k in range(4):
            n_i = di[k] + i
            n_j = dj[k] + j
            if n_i < 0 or n_i >= r or n_j < 0 or n_j >= c: continue
            loop(n_i, n_j, new_mask, current_len)

    loop(0, 0, 0, 0)
    return max_len

def main():
    input = sys.stdin.readline
    r, c = map(int, input().split())
    matrix = [list(input().rstrip()) for _ in range(r)]
    res = alphabet(r, c, matrix)
    print(res)

main()

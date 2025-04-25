import sys
def chicken_d(n, matrix):
    home_set = []
    chicken_set = []
    for i in range(n):
        for j in range(n):
            if matrix[i][j] == 1:
                home_set.append((i, j))
            elif matrix[i][j] == 2:
                chicken_set.append((i, j))
    
    home_cnt = len(home_set)
    chicken_cnt = len(chicken_set)
    chicken_matrix = [[0 for _ in range(chicken_cnt)] for _ in range(home_cnt)]
    
    for i in range(home_cnt):
        for j in range(chicken_cnt):
            chicken_matrix[i][j] = abs(home_set[i][0] - chicken_set[j][0]) + abs(home_set[i][1] - chicken_set[j][1])

    return chicken_matrix
    
def select_m(m, chicken_matrix):
    chicken_cnt = len(chicken_matrix[0])
    total_min = float('inf')
    def loop(i, seleted_mask, acc): # if e: i chicken must be select_
        nonlocal total_min
        new_mask = seleted_mask
        if chicken_cnt - i + acc == m: # include all redundent 
            for e in range(i, chicken_cnt):
                new_mask |= 1 << e
            
            total = chicken_d_of_city(new_mask, chicken_matrix)
            total_min = min(total_min, total)

            for e in range(i, chicken_cnt):
                new_mask |= 0 << e
                        
            return
        if acc == m:
            total = chicken_d_of_city(new_mask, chicken_matrix)
            total_min = min(total_min, total)
            return
        
        # if i is selected
        new_mask |= 1 << i
        loop(i + 1, new_mask, acc + 1)
        
        # if i is not selected
        loop(i + 1, seleted_mask, acc)
    loop(0, 0, 0) 
    return total_min

def chicken_d_of_city(chicken_mask, chicken_matrix):
    total = 0
    for city in chicken_matrix:
        minimum = float('inf')
        for i in range(len(city)):
            if chicken_mask & 1 << i:
                minimum = min(minimum, city[i])
        total += minimum
    return total
        

def main():
    input = sys.stdin.readline
    n, m = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(n)]
    chicken_matrix = chicken_d(n, matrix)
    res = select_m(m, chicken_matrix)
    print(res)

main()

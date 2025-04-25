def get_substring(n , a):
    accent_list = [1 for _ in range(n)]
    decent_list = [1 for _ in range(n)]

    for i in range(n - 1):
        prev_number = a[i]
        curr_number = a[i + 1]
            
        for j in range(i + 1):
            cand_number = a[j]
            if cand_number < curr_number:
                accent_list[i + 1] = max(accent_list[i + 1], accent_list[j] + 1)

                    
    for i in range(n - 1, 0, -1):
        prev_number = a[i]
        curr_number = a[i - 1]
        for j in range(n - 1, i - 1, -1):
            cand_number = a[j]
            if cand_number < curr_number:
                decent_list[i - 1] = max(decent_list[i - 1], decent_list[j] + 1)
 
    maximum = 0
    for i in range(n):
        maximum = max(maximum, accent_list[i] + decent_list[i])
    return maximum - 1

    

def main():
    n = int(input())
    a = list(map(int, input().split()))
    res = get_substring(n, a)
    print(res)

main()

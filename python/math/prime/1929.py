import math

n, m = map(int, input().split())
sqrt_m = math.floor(math.sqrt(m))

prime_matrix = [True] * (m + 1)
prime_matrix[0] = prime_matrix[1] = False

for i in range(sqrt_m + 1):
    if prime_matrix[i] == False: continue

    cnt = 2
    while i * cnt <= m:
         prime_matrix[i * cnt] = False
         cnt += 1

for i in range(n, m + 1):
    if prime_matrix[i]: print(i)
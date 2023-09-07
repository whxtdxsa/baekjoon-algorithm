def power(base, exp):
    if exp == 1: return base
    elif exp % 2 == 0:
        half_power = power(base, exp / 2)
        return half_power * half_power
    else:
        half_power = power(base, (exp - 1) / 2)
        return base * half_power * half_power
    
def modified_power(base, exp, w):
    if exp == 1: return base % w
    elif exp % 2 == 0:
        half_power = modified_power(base, exp / 2, w)
        return (half_power * half_power) % w
    else:
        half_power = modified_power(base, (exp - 1) / 2, w)
        return (base * half_power * half_power) % w
    
def main():
    base, exp, w = map(int, input().split())
    res = modified_power(base, exp, w)
    print(res)

main()


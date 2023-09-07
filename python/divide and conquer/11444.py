class Matrix:
    def __init__(self): self.data = [[1, 1], [1, 0]]

    def set(self, row, col, value): self.data[row][col] = value
    def get(self, row, col): return self.data[row][col]

    def multiply(self, other):
        result = Matrix()
        for i in range(2):
            for j in range(2):
                value = 0
                for k in range(2):
                    value += self.get(i, k) * other.get(k, j)
                result.set(i, j, value % 1000000007)
        return result
    
    def power(self, exp):
        if exp == 1: return self
        elif exp % 2 == 0:
            half_power = self.power(exp // 2)
            return half_power.multiply(half_power)
        else:
            half_power = self.power((exp - 1) // 2)
            return self.multiply(half_power.multiply(half_power))
        
def fib(n):
    if n == 1: return 1

    mat = Matrix()
    return mat.power(n - 1).get(0, 0)

res = fib(int(input()))
print(res)
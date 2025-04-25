import sys
class Matrix:
    def __init__(self, rows, cols, inputed = 1):
        self.rows = rows
        self.cols = cols
        if inputed == 1:
            self.data = [[0] * cols for _ in range(rows)]
        else:
            self.data = [[0] for _ in range(rows)]
            for i in range(rows): self.data[i] = list(map(int, sys.stdin.readline().split()))

    def set(self, row, col, value): self.data[row][col] = value

    def get(self, row, col): return self.data[row][col]

    def multiply(self, other, w = 1):
        result = Matrix(self.rows, other.cols)
        for i in range(self.rows):
            for j in range(other.cols):
                value = 0
                for k in range(self.cols):
                    value += self.get(i, k) * other.get(k, j)
                result.set(i, j, value % w)
        return result
    
    def power(self, exp, w = 1):
        if exp == 1: return self
        elif exp % 2 == 0:
            half_power = self.power(exp / 2, w)
            return half_power.multiply(half_power, w)
        else:
            half_power = self.power((exp - 1) / 2, w)
            return self.multiply(half_power.multiply(half_power, w), w)
        
    def print(self):
        for i in range(self.rows): print(*self.data[i], sep = " ")
    
def main():
    n, b = map(int, input().split())
    mat = Matrix(n, n, 0)
    if b != 1:
        res = mat.power(b, 1000)
    else:
        res = Matrix(n, n)
        for i in range(n):
            for j in range(n):
                res.set(i, j, mat.get(i, j) % 1000)
        

    res.print()

main()
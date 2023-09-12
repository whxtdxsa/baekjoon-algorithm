import sys
from collections import defaultdict

class Statistic:
    def __init__(self, total_count):
        self.total_count = total_count
        self.num_list = []
        self.num_dict = defaultdict(int)

    def getNums(self):
        for _ in range(self.total_count):
            N = int(sys.stdin.readline())
            self.num_list.append(N)
            self.num_dict[N] += 1
        self.num_list = sorted(self.num_list)
        self.num_dict = sorted(self.num_dict.items(), key = lambda x: (-x[1], x[0]))

    def Mean(self): return round(sum(self.num_list) / self.total_count)
    
    def Median(self): return self.num_list[self.total_count // 2]
    
    def Mode(self):
        if self.total_count == 1: return self.num_list[0]
        elif self.num_dict[0][1] == self.num_dict[1][1]: return self.num_dict[1][0]
        else: return self.num_dict[0][0]
    
    def Range(self): return self.num_list[-1] - self.num_list[0]
    

def main():
    N = int(sys.stdin.readline())
    s = Statistic(N)
    s.getNums()
    print(s.Mean(), s.Median(), s.Mode(), s.Range(), sep = "\n")

main()
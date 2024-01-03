class RC:
    def __init__(self, brokens):
        self.normal_buttons = [x for x in range(0, 10) if x not in brokens]
        
        self.original_target = 100
        self.reduced_target = 100

        self.first_digit = 0
        self.zero_button = False
        self.smaller_normal_buttons = []
        self.bigger_normal_buttons = []

    def initTarget(self, target):
        self.original_target = target
        target_string = str(target)
        non_exist_digit = len(target_string) - 1
        for idx, i in enumerate(target_string):
            if int(i) not in self.normal_buttons:
                non_exist_digit = idx
                if i == '0': non_exist_digit -= 1
                break

        self.reduced_target = int(target_string[non_exist_digit:])
        print(non_exist_digit, self.reduced_target)
        self.first_digit = self.reduced_target // 10**(len(str(self.reduced_target))-1)
        self.splitBrokens()

    def splitBrokens(self):
        for button in self.normal_buttons:
            if button == 0: self.zero_button = True
            elif button < self.first_digit: self.smaller_normal_buttons.append(button)
            elif button > self.first_digit: self.bigger_normal_buttons.append(button)
            else: 
                self.smaller_normal_buttons.append(button)
                self.bigger_normal_buttons.append(button)

    def getUpperBound(self):
        smallest_button = self.normal_buttons[0]
        upper_channel = 0

        if self.bigger_normal_buttons:
            upper_channel = self.bigger_normal_buttons[0] * 10 ** (len(str(self.reduced_target))-1)
            for i in range(len(str(self.reduced_target)) - 1):
                upper_channel += smallest_button * 10**i

        elif self.zero_button:
                upper_channel += self.smaller_normal_buttons[0] * 10 ** len(str(self.reduced_target))

        else:
            for i in range(len(str(self.reduced_target)) + 1):
                upper_channel += smallest_button * 10**i
                
        return upper_channel

    def getLowerBound(self):
        biggest_button = self.normal_buttons[-1]
        lower_channel = 0

        if self.smaller_normal_buttons:
            lower_channel = self.smaller_normal_buttons[-1] * 10 ** (len(str(self.reduced_target))-1)
            for i in range(len(str(self.reduced_target)) - 1):
                lower_channel += biggest_button * 10**i

        else:
            for i in range(len(str(self.reduced_target)) - 1):
                lower_channel += biggest_button * 10**i

        return lower_channel
    
    def getLeastSolution(self):
        candidate = list(map(lambda x: abs(self.reduced_target - x), (self.getLowerBound(), self.getUpperBound())))

        candidate.append(abs(self.original_target - 100))

        print(candidate)

        least_error = min(candidate) + len(str(self.original_target))
        return least_error
    
def main():
    N, M = int(input()), int(input())
    if M == 0: 
        print(len(str(N)))
        return

    input_brokens = map(int, input().split())
    controller = RC(input_brokens)
    controller.initTarget(N)
    controller.splitBrokens()
    print(controller.getUpperBound())
    print(controller.getLowerBound())
    
    print(controller.getLeastSolution())

main()

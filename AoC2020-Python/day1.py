from utils import AoCSol


class AoCDay1(AoCSol):
    
    def parse_input(self):
        with open(self.path) as f:
            return [int(line) for line in f]


    def solve1(self):
        for i in self.input:
            for j in self.input:
                if i + j == 2020:
                    return i*j
    
    def solve2(self):
        for i in self.input:
            for j in self.input:
                for k in self.input:
                    if i + j + k == 2020:
                        return i*j*k


inputpath = '/input/day1.txt'
print(AoCDay1(inputpath))
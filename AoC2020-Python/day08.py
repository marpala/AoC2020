from utils import AoCSol


class AoCDay8(AoCSol):
    
    def parse_input(self):
        with open(self.path) as f:
            return [(line[:3], int(line[4:].replace('\n', ''))) for line in f]
    
    def simulate(self):
        accumulator = 0
        history = set()
        index = 0
        while index < len(self.input):
            if index in history:
                return accumulator, True

            history.add(index)
            ins, val = self.input[index]
            if ins == 'acc':
                accumulator += val
            elif ins == 'jmp':
                index += val
                continue
            index += 1
        return accumulator, False

    def stuck(self):
        return self.simulate()[1]

    def solve1(self):
        return self.simulate()[0]
    
    def solve2(self):
        inpt_og = self.input.copy()

        for i in range(len(self.input)):
            if self.input[i][0] == 'jmp':
                self.input[i] = ('nop', self.input[i][1])
            elif self.input[i][0] == 'nop':
                self.input[i] = ('jmp', self.input[i][1])
            else:
                continue
            
            if not self.stuck():
                return self.solve1()
            else:
                self.input = inpt_og.copy()

inputpath = '/input/day8.txt'
print(AoCDay8(inputpath))
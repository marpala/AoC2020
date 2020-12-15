from utils import AoCSol


class AoCDay15(AoCSol):
    
    def parse_input(self):
        with open(self.path) as f:
            return [int(i) for i in f.readline().replace('\n', '').split(',')]

    def solve1(self, end=2020):
        last = self.input[-1]
        history = {self.input[i]: [i] for i in range(len(self.input))} # (num, appearances)
        for i in range(len(self.input), end):
            if len(history[last]) > 1: # number appeared more than once
                new_num = history[last][-1] - history[last][-2]
                if new_num in history.keys():
                    history[new_num].append(i)
                else:
                    history[new_num] = [i]
                last = new_num
            else:
                if 0 not in history.keys():
                    history[0] = [i]
                else:
                    history[0].append(i)
                last = 0
        return last
    
    def solve2(self):
        return self.solve1(30000000)


inputpath = '/input/day15.txt'
print(AoCDay15(inputpath))
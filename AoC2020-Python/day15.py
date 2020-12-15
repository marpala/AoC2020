from utils import AoCSol


class AoCDay15(AoCSol):
    
    def parse_input(self):
        with open(self.path) as f:
            return [int(i) for i in f.readline().replace('\n', '').split(',')]

    def solve1(self, end=2020):
        history_lst = [n for n in self.input]   
        history = {self.input[i]: [i] for i in range(len(self.input))} # (num, appearances)
        for i in range(len(self.input), end):
            last = history_lst[-1]
            if len(history[last]) > 1: # number appeared more than once
                new_num = history[last][-1] - history[last][-2]
                if new_num in history.keys():
                    history[new_num].append(i)
                else:
                    history[new_num] = [i]
                history_lst.append(new_num)
            else:
                if 0 not in history.keys():
                    history[0] = [i]
                else:
                    history[0].append(i)
                history_lst.append(0)

        return history_lst[-1]
    
    def solve2(self):
        return self.solve1(30000000)


inputpath = '/input/day15.txt'
print(AoCDay15(inputpath))
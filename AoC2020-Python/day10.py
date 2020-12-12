from utils import AoCSol


class AoCDay10(AoCSol):
    
    def parse_input(self):
        with open(self.path) as f:
            return sorted([int(i) for i in f.readlines()])
    
    def solve1(self):
        prev = 0
        one_jolt = 0
        three_jolts = 1
        inpt = self.input.copy()
        while len(inpt) > 0:
            minn = min(inpt)
            if minn - prev == 1:
                one_jolt += 1
            elif minn - prev == 3:
                three_jolts += 1
            prev = minn
            inpt.remove(minn)

        return one_jolt * three_jolts
    
    def solve2(self):
        dp_table = {}
        adapters = [0] + self.input + [max(self.input) + 3]
        dp_table[0] = 1

        for adapter in adapters[1:]:
            tot = 0
            for i in range(1, 4):
                new_adapter = adapter - i
                if new_adapter in adapters:
                    tot += dp_table[new_adapter]
            dp_table[adapter] = tot

        return dp_table[max(self.input) + 3]


inputpath = '/input/day10.txt'
print(AoCDay10(inputpath))
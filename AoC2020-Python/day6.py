from utils import AoCSol

class AoCDay6(AoCSol):
    
    def parse_input(self):
        with open(self.path) as f:
            return [s for s in f.readlines()]

    def solve1(self):
        c_tot = 0
        unique = set()
        for s in self.input.copy():
            if s == '\n': # new group
                c_tot += len(unique)
                unique = set()
                continue
            s = s.replace('\n', '')
            unique = unique.union(set(s))
        return c_tot
    
    def solve2(self):
        c_tot = 0
        inter = set()
        new = True
        for s in self.input.copy():
            if s == '\n': # new group
                c_tot += len(inter)
                inter = set()
                new = True
                continue
            if new:
                new = False
                inter = set(s.replace('\n', ''))
            else:
                s = s.replace('\n', '')
                inter &= set(s)
        return c_tot

inputpath = '/input/day6.txt'
print(AoCDay6(inputpath))
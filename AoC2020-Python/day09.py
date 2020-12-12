from utils import AoCSol
from collections import deque

class AoCDay9(AoCSol):

    def parse_input(self):
        with open(self.path) as f:
            return [int(i.replace('\n', '')) for i in f.readlines()]
    
    @staticmethod
    def OK(queue, n):
        for i in range(len(queue)):
            for j in range(i+1, len(queue)):
                if queue[i] + queue[j] == n:
                    return True
        return False
    
    def solve1(self):
        N = 25
        seen = deque(maxlen=N)
        for n in self.input:
            if len(seen) != N:
                seen.append(n)
            elif len(seen) >= N:
                if not self.OK(seen, n):
                    return n
                else:
                    seen.append(n)
    
    def solve2(self):
        to_check = self.solve1()
        win_size = 2
        while True:
            rng = deque(maxlen=win_size)
            for n in self.input:
                rng.append(n)
                if len(rng) == win_size:
                    if sum(rng) == to_check:
                        return min(rng) + max(rng)
            win_size += 1


inputpath = '/input/day9.txt'
print(AoCDay9(inputpath))
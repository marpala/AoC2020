from utils import AoCSol

class AoCDay13(AoCSol):
    
    def parse_input(self):
        inpt = {}
        with open(self.path) as f:
            inpt['dep_time'] = int(f.readline())
            inpt['buses'] = [int(i) if i != 'x' else None for i in f.readline().split(',')]
        return inpt

    def solve1(self):
        dep_time = self.input['dep_time']
        buses = [i for i in self.input['buses'] if i is not None]
        table = {}
        for b in buses:
            table[b] = 0
            while table[b] < dep_time:
                table[b] += b
        minn = min(i for i in table.values() if i >= dep_time)
        for k, v in table.items():
            if v == minn:
                return k * (v-dep_time)

    @staticmethod
    def xgcd(a, b):
        if a > b:
            return AoCDay13.xgcd(b, a)
        if a == 0:
            return b, 0, 1
        else:
            g, y, x = AoCDay13.xgcd(b % a, a)
            return g, x - (b // a) * y, y

    @staticmethod
    def CRT(B, M):
        m = 1
        for mi in M:
            m *= mi

        result = 0
        for i in range(len(B)):
            b = B[i]
            n = m//M[i]
            n_inv = AoCDay13.xgcd(n, M[i])[2]
            result += b * n * n_inv
        return result % m

    def solve2(self):
        buses = self.input['buses']
        mods = [bus for bus in buses if bus is not None] # mods
        results = [-i % buses[i] for i in range(len(buses)) if buses[i] is not None]
        return self.CRT(results, mods)

inputpath = '/input/day13.txt'
print(AoCDay13(inputpath))
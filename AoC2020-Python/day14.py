from utils import AoCSol

class AoCDay14(AoCSol):
    
    def parse_input(self):
        inpt = []
        with open(self.path) as f:
            curr = (None, None, None)
            for line in f:
                if line[:4] == 'mask':
                    mask = line[7:].replace('\n','')
                    curr = (mask, curr[1], curr[2])
                else:
                    end_brkt = line.find(']')
                    addr = self.dec_to_bin(int(line[4:end_brkt])) # for part 2
                    equal = line.find('=')
                    val = self.dec_to_bin(int(line[equal+2:].replace('\n', '')))
                    curr = (curr[0], addr, val)
                    inpt.append(curr)
        return inpt
    
    @staticmethod
    def dec_to_bin(n):
        return "{0:036b}".format(n)

    def solve1(self):
        memory = {}
        for mask, addr, val in self.input:
            masked = list(val)
            for i in range(len(mask)):
                if mask[i] == '1':
                    masked[i] = '1'
                elif mask[i] == '0':
                    masked[i] = '0'
            memory[addr] = ''.join(masked)
        return sum(int(i, 2) for i in memory.values())
    
    # refactor these
    @staticmethod
    def generate(n, lst=[]):
        if len(lst) == n:
            return lst
        
        poss = []
        for i in range(2):
            l = AoCDay14.generate(n, lst + [i])
            poss = poss + [l][0]
        
        return poss
    
    @staticmethod
    def formatt(lst, n):
        return [''.join(str(j) for j in lst[i:i+n]) for i in range(0, len(lst), n)]

    def solve2(self):
        memory = {}
        for mask, addr, val in self.input:
            masked_addr = list(addr)
            for i in range(len(mask)):
                if mask[i] == '1':
                    masked_addr[i] = '1'
                elif mask[i] == 'X':
                    masked_addr[i] = 'X'
            num_x = masked_addr.count('X')
            possibilities = self.formatt(self.generate(num_x), num_x)
            for bits in possibilities:
                addr_copy = masked_addr.copy()
                for bit in bits:
                    addr_copy[addr_copy.index('X')] = bit
                memory[''.join(addr_copy)] = val
        return sum(int(i, 2) for i in memory.values())


inputpath = '/input/day14.txt'
print(AoCDay14(inputpath))
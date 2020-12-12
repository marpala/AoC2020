from utils import AoCSol
import copy

DIRECTIONS = [(-1,0), (-1,1), (0,1), (1,1), (1,0), (1,-1), (0,-1), (-1,-1)]

class AoCDay12(AoCSol):
    
    @staticmethod
    def count_occ(lst):
        return len([i for i in lst if i == "#"])

    @staticmethod
    def adj(i, j, inpt):
        adjacent = []
        for d in DIRECTIONS:
            i1 = i + d[0]
            j1 = j + d[1]
            if not(i1 < 0 or i1 >= len(inpt) or j1 < 0 or j1 >= len(inpt[0])):
                seat = inpt[i1][j1]
                adjacent.append(seat)
        return adjacent

    @staticmethod
    def adj2(i, j, inpt):
        adjacent = []
        for d in DIRECTIONS:
            for k in range(1, max(len(inpt), len(inpt[0]))):
                i1 = i + k*d[0]
                j1 = j + k*d[1]
                if not(i1 < 0 or i1 >= len(inpt) or j1 < 0 or j1 >= len(inpt[0])):
                    seat = inpt[i1][j1]
                    if seat == 'L' or seat == '#':
                        adjacent.append(seat)
                        break
        return adjacent

    def parse_input(self):
        with open(self.path) as f:
            return [list(l.replace('\n', '')) for l in f.readlines()]

    def solve(self, threshold, adj):
        count = 0
        input_og = copy.deepcopy(self.input)
        while True:
            new_inpt = copy.deepcopy(input_og)
            count1 = count    
            for i in range(len(input_og)):
                for j in range(len(input_og[i])):
                    if input_og[i][j] == 'L':
                        if self.count_occ(adj(i,j,input_og)) == 0:
                            new_inpt[i][j] = '#'
                            count += 1
                    elif input_og[i][j] == '#':
                        if self.count_occ(adj(i,j,input_og)) >= threshold:
                            new_inpt[i][j] = 'L'
                            count -= 1

            input_og = new_inpt
            if count1 == count:
                break
        return count

    def solve1(self):
        return self.solve(threshold=4, adj=self.adj)

    def solve2(self):
        return self.solve(threshold=5, adj=self.adj2)


inputpath = '/input/day11.txt'
print(AoCDay12(inputpath))
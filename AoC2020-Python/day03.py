from utils import AoCSol

class AoCDay3(AoCSol):
    
    def parse_input(self):
        inpt = []
        with open(self.path) as f:
            for line in f:
                inpt.append(line.replace('\n', ''))
        return inpt

    def solve1(self, dx=3, dy=1):
        x = dx
        y = dy
        n_trees = 0
        while y < len(self.input):
            if self.input[y][x % len(self.input[0])] == '#':
                n_trees += 1
            y += dy
            x += dx 
        return n_trees
    
    def solve2(self):
        slopes = [(1,1), (3,1), (5,1), (7,1), (1,2)]
        n_trees = 1
        for dx, dy in slopes:
            n_trees *= self.solve1(dx, dy)
        return n_trees

inputpath = '/input/day3.txt'
print(AoCDay3(inputpath))
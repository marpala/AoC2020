from utils import AoCSol

ROWS = 128
COLS = 8

class AoCDay5(AoCSol):
    
    def parse_input(self):
        with open(self.path) as f:
            return [line.replace('\n', '') for line in f]
    
    @staticmethod
    def seat_id(string):
        row = (0, ROWS, -1)
        col = (0, COLS, -1)
        for c in string[:-3]:
            if c == 'F':
                row = (row[0], (row[1]+row[0])/2, (row[1]+row[0])/2-1)
            elif c == 'B':
                row = ((row[1]+row[0])/2, row[1], (row[1]+row[0])/2)
        for c in string[-3:]:
            if c == 'L':
                col = (col[0], (col[1]+col[0])/2, (col[1]+col[0])/2-1)
            elif c == 'R':
                col = ((col[1]+col[0])/2, col[1], (col[1]+col[0])/2)
        
        return int(row[2]*8 + col[2])

    def solve1(self):
        maxx = -1
        for seat in self.input:
            maxx = max(maxx, self.seat_id(seat))
        return maxx
    
    def solve2(self):
        seats = {r*8 + c for r in range(0,128) for c in range(0,8)}
        remaining = sorted(list(seats - {self.seat_id(seat) for seat in self.input}))
        for i in range(len(remaining)):
            if i > 0:
                if remaining[i] - remaining[i-1] != 1 and remaining[i+1] - remaining[i] != 1:
                    return remaining[i]


inputpath = '/input/day5.txt'
print(AoCDay5(inputpath))
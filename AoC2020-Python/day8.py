from utils import AoCSol


class AoCDay8(AoCSol):
    
    def parse_input(self):
        with open(self.path) as f:
            return [(line[:3], line[4:].replace('\n', '')) for line in f]


    def solve1:
        ff
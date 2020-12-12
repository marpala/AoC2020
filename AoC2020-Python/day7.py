from utils import AoCSol

MY_BAG = "shiny gold bag"

class AoCDay7(AoCSol):
    
    def parse_input(self):
        inpt = {}
        with open(self.path) as f:
            for rule in f:
                tokens = rule.replace('bags', 'bag').replace('\n', '').split(' ')
                bag = ' '.join(tokens[:3])
                inpt[bag] = []
                for t in range(len(tokens[3:])):
                    if tokens[t].isdigit():
                        inpt[bag].append((tokens[t], ' '.join(tokens[t+1:t+4]).replace(',', '').replace('.', '')))
        return inpt

    def solve1(self):
        can_contain = set()
        history = set()
        while True:
            prev_len = len(can_contain)

            for bag, rule in self.input.items():
                if bag in history:
                    continue
                for _, other_bag in rule:
                    if other_bag == MY_BAG or other_bag in can_contain:
                        can_contain.add(bag)
                        history.add(bag)
                        
            if prev_len == len(can_contain):
                return len(can_contain)
    
    def solve2(self, bag=MY_BAG):
        if self.input[bag] == []:
            return 0
        
        tot = 0
        for n, b in self.input[bag]:
            tot += int(n) + int(n) * self.solve2(b)

        return tot

inputpath = '/input/day7.txt'
print(AoCDay7(inputpath))
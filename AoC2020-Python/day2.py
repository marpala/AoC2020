from utils import AoCSol
import re

pat = re.compile(r"([0-9]*-)|([0-9]* )|([a-z]:)|([a-z]*)")

class AoCDay2(AoCSol):
    
    def parse_input(self):
        lst = []
        with open(self.path) as f:
            for line in f:
                match = re.findall(pat, line)
                match = ["".join(x) for x in re.findall(pat, line) if " " not in x]
                match = [i.replace('-', '').replace(':','').strip() for i in match if i != '']
                lst.append(match)
        return lst


    def solve1(self):
        counter = 0
        for m in self.input:
            minn = int(m[0])
            maxx = int(m[1])
            char = m[2]
            pswd = m[3]
            count = pswd.count(char)
            if count >= minn and count <= maxx:
                counter += 1
        return counter
    
    def solve2(self):
        counter = 0
        for m in self.input:
            fst = int(m[0])
            snd = int(m[1])
            char = m[2]
            s = m[3]
            if s[fst-1] == char and s[snd-1] == char:
                continue
            elif s[fst-1] != char and s[snd-1] != char:
                continue
            else:
                counter += 1
        return counter


inputpath = '/input/day2.txt'
print(AoCDay2(inputpath))
from utils import AoCSol
import re

req = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}
opt = 'cid'

class AoCDay4(AoCSol):
    
    def parse_input(self):
        inpt = []
        with open(self.path) as f:
            passport = {}
            for line in f:
                if line == '\n':
                    inpt.append(passport)
                    passport = {}
                    continue
                line = line.replace('\n', '').split(' ')

                for token in line:
                    token = token.split(':')
                    passport[token[0]] = token[1]
            inpt.append(passport)
        return inpt
    
    @staticmethod
    def is_valid(passport):
        fields = set(passport.keys())
        if fields == req or fields == req.union({opt}):
            return True
        return False
    
    @staticmethod
    def is_hex(s):
        return re.fullmatch(r'^[0-9a-f]$', s or '') is not None

    def solve1(self):
        c_valid = 0
        for passport in self.input:
            if self.is_valid(passport):
                c_valid +=1
        return c_valid

    def solve2(self):
        c_valid = 0
        for p in self.input:
            if not self.is_valid(p):
                continue
            if not(len(p['byr']) == 4 and p['byr'] >= '1920' and p['byr'] <= '2002'):
                continue
            if not(len(p['iyr']) == 4 and p['iyr'] >= '2010' and p['iyr'] <= '2020'):
                continue
            if not(len(p['eyr']) == 4 and p['eyr'] >= '2020' and p['eyr'] <= '2030'):
                continue
            if p['hgt'][-2:] == 'cm':
                if not(p['hgt'].replace('cm', '') >= '150' and p['hgt'].replace('cm', '') <= '193'):
                    continue
            elif p['hgt'][-2:] == 'in':
                if not(p['hgt'].replace('in', '') >= '59' and p['hgt'].replace('in', '') <= '76'):
                    continue
            else:
                continue
            if not(p['hcl'][0] == '#' or len(p['hcl'][1:]) == 6 or self.is_hex(p['hcl'][1:])):
                continue
            if not(p['ecl'] in {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'}):
                continue
            if not(len(p['pid']) == 9 and p['pid'].isdigit()):
                continue
            
            c_valid += 1
        return c_valid

inputpath = '/input/day4.txt'
print(AoCDay4(inputpath))
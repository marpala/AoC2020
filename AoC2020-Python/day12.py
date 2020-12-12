from utils import AoCSol
from math import cos, sin, radians

class AoCDay12(AoCSol):
        
    def parse_input(self):
        inpt = []
        with open(self.path) as f:
            for line in f:
                line = line.replace('\n', '')
                inpt.append((line[0], int(line[1:])))
        return inpt

    @staticmethod
    def rotate(ship, waypoint, ang):
        sx, sy = ship
        wx, wy = waypoint
        wx1 = sx + cos(ang)*(wx - sx) - sin(ang)*(wy - sy)
        wy1 = sy + sin(ang)*(wx - sx) + cos(ang)*(wy - sy)
        return wx1, wy1

    def solve1(self):
        d = (0,0,0) # (x, y, angle)
        for dire, magn in self.input:
            if dire == 'F':
                d = (d[0]+magn*cos(radians(d[2])), d[1]+magn*sin(radians(d[2])), d[2])
            elif dire == 'N':
                d = (d[0], d[1]+magn, d[2])
            elif dire == 'S':
                d = (d[0], d[1]-magn, d[2])
            elif dire == 'E':
                d = (d[0]+magn, d[1], d[2])
            elif dire == 'W':
                d = (d[0]-magn, d[1], d[2])
            elif dire == 'R':
                d = (d[0], d[1], d[2]-magn)
            elif dire == 'L':
                d = (d[0], d[1], d[2]+magn)
        return abs(round(d[0])) + abs(round(d[1]))
    
    def solve2(self):
        w = (10, 1) # (x, y) relative to the ship
        d = (0,0,0) # (x, y, angle)
        for dire, magn in self.input:
            if dire == 'F':
                d = (d[0]+w[0]*magn, d[1]+w[1]*magn, d[2])
            elif dire == 'N':
                w = (w[0], w[1]+magn)
            elif dire == 'S':
                w = (w[0], w[1]-magn)
            elif dire == 'E':
                w = (w[0]+magn, w[1])
            elif dire == 'W':
                w = (w[0]-magn, w[1])
            elif dire == 'R':
                w = self.rotate((d[0], d[1]), (w[0]+d[0], w[1]+d[1]), radians(-magn))
                w = (w[0] - d[0], w[1] - d[1]) # make point relative again
            elif dire == 'L':
                w = self.rotate((d[0], d[1]), (w[0]+d[0], w[1]+d[1]), radians(magn))
                w = (w[0] - d[0], w[1] - d[1]) # make point relative again
        return abs(round(d[0])) + abs(round(d[1]))

inputpath = '/input/day12.txt'
print(AoCDay12(inputpath))
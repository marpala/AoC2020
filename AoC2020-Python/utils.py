import os
from abc import ABC, abstractmethod

class AoCSol(ABC):

    def __init__(self, path):
        self.path = os.getcwd() + path
        self.input = self.parse_input()
    
    @abstractmethod
    def parse_input(self):
        raise NotImplementedError
    
    @abstractmethod
    def solve1(self):
        raise NotImplementedError
    
    @abstractmethod
    def solve2(self):
        raise NotImplementedError
    
    def __str__(self):
        return f'Silver: {self.solve1()}\nGold: {self.solve2()}'
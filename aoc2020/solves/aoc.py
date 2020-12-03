import os
from os.path import join, dirname

class AocDay():
    input_path = join(dirname(__file__), '../inputs/')
    challenge1 = 'tbd'
    challenge2 = 'tbd'

    def __init__(self, day:int):
        if (0 > day > 25):
            raise ValueError("Day must be 1 to 25")
        self.day = day

        inputs = open('{}/day{}_input.txt'.format(self.input_path, day))
        try:
            self.input = inputs.readlines()
        finally:
            inputs.close()
    
    def solve(self):
        print('DAY {} CHALLENGE 1: {}'.format(self.day, self.challenge1))
        print(self.solve1())
        
        print('DAY {} CHALLENGE 2: {}'.format(self.day, self.challenge2))
        print(self.solve2())


    def solve1(self):
        return 'tbd'

    def solve2(self):
        return 'tbd'
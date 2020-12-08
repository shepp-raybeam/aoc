#from parsimonious.grammar import Grammar
import re

from aoc import AocDay

class day8(AocDay):   
    """
    ops:
     acc i
     jmp [+-]i
     nop
    """

    def __init__(self, day):
        AocDay.__init__(self, day)   
        self.reset()

    def reset(self):
        self.pc = 0
        self.acc = 0
        self.instructions = []
        self.process_input()
    
    def process_input(self):
        for inst in self.input:
            self.instructions.append(inst.split())


    challenge1 = "Immediately before any instruction is executed a second time, what value is in the accumulator?"
    def solve1(self):
        return self.run()
        

    def run(self):
        states = {}
        while True:
            inst = self.instructions[self.pc]
            print(inst, self.pc, self.acc)
            if self.pc in states:
                return self.acc
            states[self.pc] = self.acc
            if inst[0] == 'nop':
              self.pc += 1
              continue
            if inst[0] == 'acc':
              self.acc += int(inst[1])
              self.pc += 1
              continue
            if inst[0] == 'jmp':
              self.pc += int(inst[1])
              continue

    challenge2 = "flip a single nop to jmp or jmp to nop to get pc to 1 past the end"
    def solve2(self):
        for i, inst in enumerate(self.instructions):
            self.reset()
            if inst[0] == 'nop' or inst[0] == 'jmp':
                print('flipping at {}'.format(i))
            if inst[0] == 'nop':
                self.instructions[i][0] = 'jmp'
                try:
                    res = self.run()
                except IndexError:
                    return res
                continue
            if inst[0] == 'jmp':
                self.instructions[i][0] = 'nop'
                try:
                    res = self.run()
                except IndexError:
                    return res
                continue
        return ''

day = day8(8)
day.solve()
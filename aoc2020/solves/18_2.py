from parsimonious.grammar import Grammar
import re


class Solution():
    def __init__(self, input):
        self.input = input
        self.statements = []
        self.stack = []
        self.process_input()

    def process_input(self):        
        with open(input) as f:
            for line in f:
                self.statements.append(line.strip())

    def eval(self, statement):
        pass

    def solve1(self):
        grammar = Grammar(
            """
            stmt = expression
            expression = (num op expression) / ("(" expression ")")
            op = ~'[+*]'
            num = ~'[0-9]+'
            """                      
        )
        print(grammar.parse('6+4*2'))
        #sum the results
        result = 0
        for s in self.statements:
            result += eval(s)
        print(self.statements)
        

input = 'inputs/day18_input.txt'
sol = Solution(input)
sol.solve1()




"""
build a tree
ops have left and right children
numbers are terminals
1 + 2 * 3
1 + (2 * 3)
(1 + 2) * 3
left associative

 +
1 *
 2 3


    *
 +     3
1 2


as a stack:
+ 1 + 2 3
+ + 1 2 3

eval:
if pop is op:
    eval(pop) op eval(pop)
if pop is val:
    return Val 
"""
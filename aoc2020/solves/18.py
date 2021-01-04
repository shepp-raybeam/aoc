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

    def parse(self, statement):
        tokens = (t for t in re.findall(r'([0-9]+|[+*]|[()])', statement))
        for token in tokens:
            if re.match(r'[0-9]+', token):
                self.stack.append(token)
            if re.match


expression: 
        "(" expression ")"
            
    def eval(self, ctx):
        while self.stack:
            top = self.stack.pop
            if re.match(r'[0-9]+', top):
                return top
            if top == '+':
                return left + right
            if top == '*':
                return left * right
    
    def solve1(self):
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
1 + (2 + 3)
(1 + 2) + 3
left associative

 +
1 +
 2 3


    +
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
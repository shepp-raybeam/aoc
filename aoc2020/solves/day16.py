import re

class Field():
    def __init__(self, line):
        name, ranges = line.split(':')
        self.name = name
        self.ranges = [range(int(r[0]), int(r[1])+1) for r in re.findall(r'([0-9]+)-([0-9]+)', ranges)]

    def contains(self, value):
        return any(map(lambda x: value in x, self.ranges))
    
class Ticket():
    def __init__(self, line):
        self.values = [int(x) for x in line.split(',')]
    
    def valid(self, fields):
        return len(self.invalid_values(fields)) == 0

    def invalid_values(self, fields): #return the list of values that are invalid
        invals = []
        lol = [field.ranges for field in fields] #list of lists
        ranges = [item for sublist in lol for item in sublist]
        for val in self.values:
            if not any(map(lambda r: val in r, ranges)): #is the value not in any field range
                invals.append(val)
        return invals

class Solution():
    def __init__(self, inputfile):        
        self.inputfile = inputfile
        self.fields = []
        self._tickets = []
        self.process_input(self.inputfile)

    @property
    def tickets(self):
        return self._tickets[1:]
    
    @property
    def myticket(self):
        return self._tickets[0]

    def process_input(self, inputfile):
        blocknum = 0
        with open(inputfile, 'r') as lines:
            for line in lines:
                line = line.strip()
                if line == '': #end of a block
                    blocknum +=1
                    continue
                if line in ['your ticket:', 'nearby tickets:']:
                    continue
                if blocknum == 0:
                    self.fields.append(Field(line))
                if blocknum > 0:
                    self._tickets.append(Ticket(line))
    
    def solve1(self):
        result = 0
        for ticket in self.tickets:
            if not ticket.valid(self.fields):
                result += sum(ticket.invalid_values(self.fields))
        return result
    
    def solve2(self):
        """ map every field to a position in the valid tickets"""
        #only consider valid tickets
        tickets = [ticket for ticket in self.tickets if ticket.valid(self.fields)]
        fields = self.fields
        numfields = len(fields)

        state = []
        #for each position, what fields could it be
        for pos in range(numfields): 
            values = [ticket.values[pos] for ticket in tickets]
            possible_fields = []
            for field in fields:                
                possible = all([field.contains(value) for value in values])
                possible_fields.append(1 if possible else 0)
            state.append(possible_fields)
        


        bound = []
        while len(bound) < numfields:
            for i, states in enumerate(state):
                #print(f'{i:02d}: {states}', sum(states))
                pass

            colsums = []                
            for j in range(numfields):
                colsums.append(sum([states[j] for states in state]))
            #print(f'xx: {colsums}')

            for i in range(numfields): #across
                if sum(state[i]) == 1:
                    j = state[i].index(1)
                    if fields[j].name not in bound:
                        #print(f'pos {i} is {fields[j].name}')
                        bound.append(fields[j].name)
                        for x in range(numfields):
                            if x != i:
                                state[x][j] = 0


            for j in range(numfields):
                col = [states[j] for states in state]
                if sum(col) == 1:
                    i = col.index(1)
                    if fields[j].name not in bound:
                        #print(f'pos {i} is {fields[j].name}')
                        bound.append(fields[j].name)
                        for x in range(numfields):
                            if x != j:
                                state[i][x] = 0
        
        result = 1
        for pos, states in enumerate(state):            
            index = states.index(1)
            fieldname = fields[states.index(1)].name
            if fieldname.startswith('departure'):
                #print(f'{fieldname} is position {pos} - myticket has {self.myticket.values[pos]}')
                result *= self.myticket.values[pos]
        return result




inputfile = 'inputs/day16_small.txt'
inputfile = 'inputs/day16_input.txt'
solution = Solution(inputfile)
print(f'part 1: {solution.solve1()}')
print(f'part 2: {solution.solve2()}')
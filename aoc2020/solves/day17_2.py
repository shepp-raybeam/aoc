import numpy as np

class Solution():
    def __init__(self, input):
        self.input = input
        self.state = self.process_input()
    
    def process_input(self):
        lines = []
        with open(self.input) as f:
            for line in f:
                line = line.strip()
                if line != '':
                    lines.append(list(line))
        size = len(lines)
        cube2d = np.array(lines)
        state = np.full((size+2, size+2, size+2), '.')

        state[int(size/2)+1, 1:-1, 1:-1] = cube2d
        return state
    
    def cycle(self):
        self.add_border()
        #If a cube is active and exactly 2 or 3 of its neighbors are also active, the cube remains active. Otherwise, the cube becomes inactive.
        #If a cube is inactive but exactly 3 of its neighbors are active, the cube becomes active. Otherwise, the cube remains inactive.
        flips = []
        #print(f'ss: {self.state}')
        #active_space = self.state[1:-1, 1:-1, 1:-1]
        #print(f'as: {active_space}')
        iter = np.nditer(self.state[1:-1, 1:-1, 1:-1], flags=['multi_index'])
        for i in iter:
            x,y,z = iter.multi_index
            #add one to the indices to match state space
            x,y,z = x+1, y+1, z+1
            region = self.state[x-1:x+2, y-1:y+2, z-1:z+2]
            #print(f'region of {x} {y} {z}: {region}')
            active_in_region = np.sum(np.where(region == '#', 1, 0))
            if i == '#':
                if not(active_in_region == 3 or active_in_region == 4):
                    flips.append((x,y,z))
            if i == '.':
                if active_in_region == 3:
                    flips.append((x,y,z))

        for i in flips:
            x,y,z = i
            current = self.state[x,y,z]
            self.state[x, y, z] = '#' if current == '.' else '.'

    def add_border(self): #better if it only added when previous plane is not all .
        size = self.state.shape[0]
        newstate = np.full((size+2, size+2, size+2), '.')
        newstate[1:self.state.shape[0]+1, 1:self.state.shape[1]+1, 1:self.state.shape[2]+1] = self.state 
        self.state = newstate

    def solve1(self):
        print(f'{self.state}')        
        for _ in range(6):
            self.cycle()
        print(np.sum(np.where(self.state == '#', 1, 0)))
        print(f'{self.state.shape}')
        #print(f'{self.state[5:-5, 5:-5, 5:-5]}')




input = 'inputs/day17_big_input.txt'
#input = 'inputs/day17_input.txt'
sol = Solution(input)
sol.solve1()
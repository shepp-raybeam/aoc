from aoc import AocDay

class day17(AocDay):   
    """3d game of life"""
    def __init__(self, day):
        AocDay.__init__(self, day)
        self.space = [[[0]*21]*21]*21
        
        self.process_input()

    def process_input(self):
        offset_x, offset_y, offset_z  = 10, 10, 10
        for i, line in enumerate(self.input):
            self.input[i] = line.strip()
        for i in range(len(self.input)):
            for j in range(len(self.input[i])):
                if self.input[i][j] == '#': 
                    val = 1 
                else:
                    val = 0
                self.space[offset_x+i][offset_y+j][offset_z] = val
    

    def update(self):
        newspace = self.space.copy()
        for i in range(len(self.space)):
            for j in range(len(self.space[i])):
                for k in range(len(self.space[i][j])):
                    state = self.space[i][j][k]
                    #check the 3x3x3 surrounding states
                    total = 0

                    total += self.countactive(i-1, j-1, k)
                    total += self.countactive(i+0, j-1, k)
                    total += self.countactive(i+1, j-1, k)
                    total += self.countactive(i-1, j-0, k)
                    total += self.countactive(i+0, j-0, k)
                    total += self.countactive(i+1, j-0, k)
                    total += self.countactive(i-1, j+1, k)
                    total += self.countactive(i+0, j+1, k)
                    total += self.countactive(i+1, j+1, k)

                    if state == '1':
                        total -=1
                        if total < 2 or total > 3:
                            newspace[i][j][k] = '0'
                    if state == '0':
                        if total == 3:
                            newspace[i][j][k] = '1'
        self.space = newspace                          

    def countactive(self, i, j, k):
        if i < 0 or i > 20:
            return 0
        if j < 0 or j > 20:
            return 0
        return sum(self.space[i][j][min(0,k-1):max(20,k+1)])
        

    challenge1 = 'how many active after 6 rounds'
    def solve1(self):
        """
        active and 2 or 3 neighbors active, stay active else inactive
        inactive and 3 neighbors active, active else stay inactive
        """
        for i in range(6):
            self.update()
        active = 0
        for i in range(len(self.space)):
            active += sum(map(sum, self.space[i])) #this line is sus
        print(active)

    
    challenge2 = ''
    def solve2(self):
        pass

day = day17(17)
day.solve()
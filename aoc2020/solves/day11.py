from aoc import AocDay

class day11(AocDay):   
    """
    If a seat is empty (L) and there are no occupied seats adjacent to it, the seat becomes occupied.
    If a seat is occupied (#) and four or more seats adjacent to it are also occupied, the seat becomes empty.
    Otherwise, the seat's state does not change.
    """

    def __init__(self, day):
        AocDay.__init__(self, day)
        self.process_input()

    def process_input(self):
        self.seats = []
        for input in self.input:
            self.seats.append(list(input.strip()))


    challenge1 = "how many seats end up occupied?"
    def solve1(self):
        state1, state2 = [], []
        state2 = self.new_state(self.seats)
        while state1 != state2:
            state1 = state2
            state2 = self.new_state(state1)
        count = 0
        for r in state1:
            count += sum([1 for x in r if x == '#'])
        return count

    

    def new_state(self, seatstate):
        newstate = [[ '.' for i in range(len(seatstate[0]))] for j in range(len(seatstate))]
        for i in range(len(seatstate)):
            for j in range(len(seatstate[i])):
                newstate[i][j] = self._new_state(seatstate, i,j)
        return newstate

    def _new_state(self, seatstate, i, j):
        state = seatstate[i][j]    
        dirs = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        adjacent = []
        for dir in dirs:
            row, col = i+dir[0], j+dir[1]
            if row >= 0 and row < len(seatstate):
                if col >= 0 and col < len(seatstate[0]):
                    adjacent.append(seatstate[row][col])

        if state == 'L':
            if not '#' in adjacent:
                return '#'
        if state == '#':
            if adjacent.count('#') >= 4:
                return 'L'
        return state

            
    challenge2 = ""
    def solve2(self):
        state1, state2 = [], []
        state2 = self.new_state2(self.seats)
        while state1 != state2:
            state1 = state2
            state2 = self.new_state2(state1)
        count = 0
        for r in state1:
            count += sum([1 for x in r if x == '#'])
        return count

    def new_state2(self, seatstate):
        newstate = [[ '.' for i in range(len(seatstate[0]))] for j in range(len(seatstate))]
        for i in range(len(seatstate)):
            for j in range(len(seatstate[i])):
                newstate[i][j] = self._new_state2(seatstate, i,j)
        return newstate

    def _new_state2(self, seatstate, i, j):
        state = seatstate[i][j]    
        dirs = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        adjacent = []
        for dir in dirs:
            check = self.adjacent2(seatstate, i, j, dir)
            if check:
                adjacent.append(check)

        if state == 'L':
            if not '#' in adjacent:
                return '#'
        if state == '#':
            if adjacent.count('#') >= 5:
                return 'L'
        return state

    def adjacent2(self, seatstate, i, j, dir):
        row, col = i+dir[0], j+dir[1]
        if row >= 0 and row < len(seatstate):
            if col >= 0 and col < len(seatstate[0]):
                if seatstate[row][col] == '.':
                    return self.adjacent2(seatstate, row, col, dir)
                else:
                    return seatstate[row][col]
        return None



day = day11(11)
day.solve()
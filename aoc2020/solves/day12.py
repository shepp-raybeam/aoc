from aoc import AocDay

class day12(AocDay):   

    def __init__(self, day):
        AocDay.__init__(self, day)
        self.process_input()

    def process_input(self):
        self.commands = []
        for input in self.input:
            action, value = input[0], input[1:]
            self.commands.append((action, int(value)))

    challenge1 = "What is the Manhattan distance between that location and the ship's starting position?"
    def solve1(self):
        x,y = 0,0
        heading = 90
        honks = [(0,1), (1,0), (0,-1), (-1, 0)]
        cards = ['N', 'E', 'S', 'W']
        for command in self.commands:
            if command[0] == 'L': #port
                heading -= command[1]
                continue
            if command[0] == 'R': #starboard
                heading += command[1]
                continue
            if command[0] == 'F':
                dir = honks[(heading // 90)%4]
            else:
                dir = honks[cards.index(command[0])]
            x = x+(command[1]*dir[0])
            y = y+(command[1]*dir[1])
        return self.taxicabDistance(0,0,x,y)

    def solve2(self):
        boat = (0,0)
        wp = (10,1)
        heading = 90
        honks = [(0,1), (1,0), (0,-1), (-1, 0)]
        cards = ['N', 'E', 'S', 'W']
        for command in self.commands:
            if command[0] == 'L': #port
                heading -= command[1]
                for x in range((command[1] // 90) % 4):
                    wp = self.rotate(wp, command[0])
                continue
            if command[0] == 'R': #starboard
                heading += command[1]
                for x in range((command[1] // 90) % 4):
                    wp = self.rotate(wp, command[0])
                continue
            if command[0] == 'F':
                boat = (boat[0]+(command[1] * wp[0]), boat[1]+(command[1] * wp[1]))
            else:
                wp = self.translate(wp, honks[cards.index(command[0])], command[1])
        return self.taxicabDistance(0,0,boat[0],boat[1])

    def translate(self, pos, dir, amount):
        return (pos[0] + dir[0]*amount, pos[1] + dir[1]*amount)

    def rotate(self, pos, dir):
        #its cheeky
        #rotate the RELATIVE position so base is always 0,0
        #you ready for this shit?
        x,y = pos[0], pos[1]
        if dir == 'L':
            return [-y, x]
        if dir == 'R':
            return [y, -x]

        

        

    def taxicabDistance(self, xA,yA,xB,yB):
        distance = abs(xA-xB) + abs(yA-yB)
        return distance


day = day12(12)
day.solve()
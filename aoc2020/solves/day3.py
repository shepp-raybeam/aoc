from aoc import AocDay

class day3(AocDay):
    challenge1 = "at slope (3,1) how many trees do you hit"
    def solve1(self):
        slope=(3,1)
        return self.countTrees(slope)

    challenge2 = "what is the product of trees hit with slopes (1,1), (3,1), (5,1), (7,1), (1,2)"
    def solve2(self):
        slopes=[(1,1), (3,1), (5,1), (7,1), (1,2)]
        product = 1
        for slope in slopes:
            product = product*self.countTrees(slope)
        return product

    def countTrees(self, slope):
        x,y,hit=0,0,0
        for i,row in enumerate(self.input):
            if i%slope[1] !=0:
                continue
            length = len(row)-1
            if row[x%length] == '#':
                hit=hit+1
            x=x+slope[0]
            y=y+slope[1]
        return hit

day = day3(3)
day.solve()
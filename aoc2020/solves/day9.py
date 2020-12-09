from aoc import AocDay
from itertools import combinations

class day9(AocDay):   


    def __init__(self, day):
        AocDay.__init__(self, day)
        self.values = []
        self.process_input()

    def process_input(self):
        for input in self.input:
            self.values.append(int(input))

    challenge1 = "what number is not the sum of 2 of the previous 25"
    def solve1(self):
        size = 25

        for pos in range(size, len(self.values)):
            combs = set(list(combinations(self.values[pos-size:pos], 2)))
            sums = map(lambda x: sum(x), combs)
            if not self.values[pos] in sums:
                return self.values[pos]
        return -1
        
    challenge2 = "find a contiguous set of at least two numbers in your list which sum to the invalid number from step 1 then sum the smallest and largest in that set"
    def solve2(self):
        challenge = self.solve1()
        window = 2
        while window < len(self.values):
            for i in range(0, len(self.values)-window):
                cont_sum = sum(self.values[i:window])
                if cont_sum == challenge:
                    return min(self.values[i:window]) + max(self.values[i:window])
            window += 1
        return -1

day = day9(9)
day.solve()
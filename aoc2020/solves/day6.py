import re

from aoc import AocDay

class day6(AocDay):  
    "sum counts"  
    def __init__(self, day):
        AocDay.__init__(self, day)   
        self.process_input()

    challenge1 = "count uniq chars per group and sum all counts"
    def solve1(self):
        sum = 0
        for group in self.results:
            #get the uniq chars from the strings in this group
            full = ''.join(group)
            sum = sum + len(set(full))
            print(group, sum)
        return sum

    challenge2 = "count chars common to every string in group and sum all counts"
    def solve2(self):
        sum = 0
        for group in self.results:
            temp = {}
            for str in group:
                for char in str:
                    if char in temp:
                        temp[char] += 1
                    else:
                        temp[char] = 1
            for k,v in temp.items():
                if v == len(group):
                    sum += 1
        return sum

    def process_input(self):
        self.results = []
        group = []
        for i,input in enumerate([i.strip() for i in self.input]):
            #blank line means end of group
            print(i, len(self.input), input)
            if input != '':
                group.append(input)
            if input == '' or i == len(self.input)-1:
                self.results.append(group)
                group = []

                

            


day = day6(6)
day.solve()
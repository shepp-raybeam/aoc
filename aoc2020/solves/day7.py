#from parsimonious.grammar import Grammar
import re

from aoc import AocDay

class day7(AocDay):   
    def __init__(self, day):
        AocDay.__init__(self, day)   
        self.process_input()

    challenge1 = "how many bag colors can contain (nested) shiny gold bag"
    def solve1(self):
        #count containers that contain shiny gold
        color = 'shiny gold'
        results = []
        self.allcontains(color, results)
        return len(results)

    def allcontains(self, color, results):
        for c in self.contains(color):
            if c in results:
                continue
            results.append(c)
            self.allcontains(c, results)

    def contains(self, color):
        return [c[0] for c in self.rules for cc in c[1] if color in cc]        

    challenge2 = "how many bags are in given bag"
    def solve2(self):
        result = self.allholds('shiny gold')
        return result-1

    def holds(self, color):
        found = [c[1] for c in self.rules if c[0] == color][0]
        print(found)
        return found

    def allholds(self, color):
        sum = 1
        holding = self.holds(color)
        for bag in holding:
            sum += int(bag[0]) * self.allholds(bag[1])        
        return sum


    def process_input(self):
        self.rules = []
        #represent as (<color>, [(num, color), ...])
        pattern1 = r'^([a-z ]+?) bags contain'
        pattern2 = r'([0-9]+) ([a-z ]+?) bag[s]?[,.]'
     
        for input in [i.strip() for i in self.input]:
            parse1 = re.match(pattern1, input)
            parse2 = re.findall(pattern2, input)
            container = parse1.group(1)
            self.rules.append((container, parse2))
        return

day = day7(7)
day.solve()
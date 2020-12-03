from aoc import AocDay

import re        
class day2(AocDay):
    pattern = r'^(\d+)-(\d+) (\w): (\w+)$'

    challenge1 = 'find the number of passwords that are valid'

    def solve1(self):
        count = 0
        for input in self.input:
            m = re.match(self.pattern, input)
            min = int(m.group(1))
            max = int(m.group(2))
            char = m.group(3)
            str = m.group(4)
            found = str.count(char)
            if min <= found <= max:
                count = count + 1
        return count

    challenge2 = 'find the number of passwords that are valid'
    def solve2(self):
        count = 0
        for input in self.input:
            m = re.match(self.pattern, input)
            pos1 = int(m.group(1))
            pos2 = int(m.group(2))
            char = m.group(3)
            str = m.group(4)
            found = (str[pos1-1] == char) ^ (str[pos2-1] == char)
            if found: count = count + 1
        return count



day = day2(2)
day.solve()

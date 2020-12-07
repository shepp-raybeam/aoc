import re

from aoc import AocDay

class day5(AocDay):
    """BSP"""
    def __init__(self, day):
        AocDay.__init__(self, day)   
        self.process_input()

    challenge1 = "what is the highest seat id"
    def solve1(self):        
        return max(self.seatids)

    challenge2 = "which seat is missing from list"
    def solve2(self):
        self.seatids.sort()
        print(self.seatids)
        prev=self.seatids[0]
        for seatid in self.seatids:
            if seatid - prev > 1:
                print(seatid-1)
            prev=seatid
        return ''

    def process_input(self):
        self.seatids = []
        for input in self.input:
            self.seatids.append(self.seatid_convert(input))

    def seatid_convert(self, input):
        row = input[:7]
        row = row.replace('F', '0')
        row = row.replace('B', '1')
        seat = input[-4:]
        seat = seat.replace('L', '0')
        seat = seat.replace('R', '1')
        seatid = int(row, 2)*8 + int(seat, 2)
        #print(input, row, seat, seatid)
        return seatid

day = day5(5)
day.solve()
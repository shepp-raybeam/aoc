#!/bin/python

### find the two entries that sum to 2020 and then multiply those two numbers together.



#x + y = 2020 so x = 2020-y
with open('../inputs/day1_input1.txt', 'rb') as input:
  entries = [int(entry) for entry in input.readlines()]


for entry in entries:
    if 2020-entry in entries:
        print('ans: {}\n e1: {}\n e2: {}\n'.format(entry*(2020-entry), entry, 2020-entry))


#x+y+z = 2020 so x = 2020-y-z
for entry in entries:
    for entry2 in entries:
        if 2020-entry-entry2 in entries:
            print('ans: {}\ne1: {}\ne2: {}\ne3: {}\n'.format(entry*entry2*(2020-entry-entry2), entry, entry2, 2020-entry-entry2))

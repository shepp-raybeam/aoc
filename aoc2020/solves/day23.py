class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Solution:
    def __init__(self, input):
        self.input = input        

    def process_input(self, input):
        cups = [int(c) for c in str(input)]
        nodes = {i:Node(i) for i in range(1, 1000001)}
        for i,c in enumerate(cups):
            next_cup = cups[(i+1)%len(cups)] #cup value
            nodes[c].next = nodes[next_cup]
        for i in range(len(cups)+1, 1000000):
            next_cup = i+1
            nodes[i].next = nodes[next_cup]
        self.extra = nodes[len(cups)+1]
        nodes[1000000].next = nodes[cups[0]]
        self.cups = cups
        self.nodes = nodes
        self.current = nodes[cups[0]]
       

    def solve1(self):
        self.process_input(self.input)
        self.run(100, 9)
        n = self.nodes[1].next
        res = ''
        for _ in range(len(self.cups)-1):
            res += str(n.value)
            n = n.next
        print(res)


    def solve2(self):
        self.process_input(self.input)
        self.nodes[self.cups[-1]].next = self.extra
        print('test', self.nodes[7].next.value)
        self.run(10000000, 1000000)
        n1 = self.nodes[1]
        print(n1.next.value, n1.next.next.value)
        print(n1.next.value * n1.next.next.value)



    def run(self, steps, maxvalue):
        current = self.current
        for _ in range(steps):
            picked = current.next
            current.next = current.next.next.next.next            

            x = current.value-1 if current.value != 1 else maxvalue
            dest = self.nodes[x]            
            while True:
                if dest.value in [picked.value, picked.next.value, picked.next.next.value]:
                    x= x-1 if x != 1 else maxvalue
                    dest = self.nodes[x]
                else:
                    break

            
            picked.next.next.next = dest.next
            dest.next = picked            
            current = current.next



input = 215694783
#input = 389125467
sol = Solution(input)
sol.solve1()

for i in sol.cups:
    print(i, sol.nodes[i].value, sol.nodes[i].next.value)

for i in [999999, 1000000, sol.extra.value]:
    print(i, sol.nodes[i].value, sol.nodes[i].next.value)
sol.solve2()
from aoc import AocDay

class vm():
    def __init__(self, program):
        print('creating vm')
        self.mem = {}            
        self.assembly = []
        self.mask = 'X'*36
        self.ops = ['mask', 'mem']
        self.load(program)

    def load(self, program):
        for inst in program:
            tokens = [x.strip() for x in inst.split('=')]
            if tokens[0] == 'mask':                    
                op = 'mask'
                oper1 = tokens[1]
                oper2 = None
            if tokens[0][0:3] == 'mem':
                op = 'mem'
                oper1 = int(tokens[0][4:-1])
                oper2 = int(tokens[1])
            self.assembly.append((op, oper1, oper2))

    def run(self):
        for inst in self.assembly:
            if not inst[0] in self.ops:
                raise ValueError
            if inst[0] == 'mask':
                self.mask = inst[1]
            if inst[0] == 'mem':
                self.mov(inst[2], inst[1])

    def mov(self, val, dest):
        mask1 = self.mask.replace('X', '1')
        mask2 = self.mask.replace('X', '0')
        val = val & int(mask1, 2)
        val = val | int(mask2, 2)
        self.mem[dest] = val

    def run2(self):
        for inst in self.assembly:
            if not inst[0] in self.ops:
                raise ValueError
            if inst[0] == 'mask':
                self.mask = inst[1]
            if inst[0] == 'mem':
                self.mov2(inst[2], inst[1])

    def mov2(self, val, dest):
        zeromasks = self._fakemasks(self.mask, [])
        mask1 = self.mask.replace('X', '1')
        for zeromask in zeromasks:              
            newdest = dest | int(mask1, 2)
            newdest = newdest & int(zeromask, 2)
            self.mem[newdest] = val
            #print(f'mask1: {mask1[-6:]} mask0: {zeromask[-6:]} dest: {dest} newdest: {newdest} val: {val}')

    def _fakemasks(self, mask, zeroes):
        if mask.count('X') == 0:
            mask0 = ['1'] * 36
            for zero in zeroes:
                mask0[zero] = '0'
            return [''.join(mask0)]
        
        ind = mask.index('X')
        mask1 = mask[:ind] + '1' + mask[ind+1:]
        mask0 = mask[:ind] + '0' + mask[ind+1:]
        return self._fakemasks(mask1, zeroes) + self._fakemasks(mask0, zeroes + [ind])


class day14(AocDay): 


    def __init__(self, day):
        AocDay.__init__(self, day)
        self.process_input()

    def process_input(self):
        pass

    challenge1 = 'sum the memory'
    def solve1(self):        
        vm1 = vm(self.input)
        vm1.run()
        return sum(vm1.mem.values())


    challenge2 = 'sum the memory'
    def solve2(self):
        vm2 = vm(self.input)
        vm2.run2()
        return sum(vm2.mem.values())
        

day = day14(14)
day.solve()
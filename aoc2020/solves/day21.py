import numpy as np

class Solution():
    def __init__(self, input):
        self.lines = []
        self.process_input(input)

    def process_input(self, input):
        with open(input) as f:
            for line in f:
                line = line.strip()
                div = line.index('(') - 1
                ingredients = line[0:div].split(' ')
                stripme = ' (contains '
                allergens = line[div+len(stripme):-1].split(',')
                allergens = [a.strip() for a in allergens]
                self.lines.append((ingredients, allergens))
                #vslznhr pjgmtx vgpgn gbbbjxj vqsf pxhg (contains eggs, wheat, sesame)
        
        all_ingredients = []
        all_allergens = []
        for line in self.lines:
            all_ingredients += line[0]
            all_allergens += line[1]
        self.all_ingredients = list(set(all_ingredients))
        self.all_allergens = list(set(all_allergens))
    
    def solve2(self):
        state = []
        results = {}
        for a in self.all_allergens:
            #intersect all ing lists that may contain a
            sets = [set(line[0]) for line in self.lines if a in line[1]]
            results[a] = sets[0].intersection(*sets[1:])

        #print(results)
        found_ing = set([])
        for k,v in results.items():
            found_ing = found_ing.union(v)
        good_ing = set(self.all_ingredients) - found_ing
        
        ingredients = list(set(self.all_ingredients) - good_ing)

        #for each questionable ing, which allergens might it contain        
        for i in ingredients:
            may_contain = list(map(lambda x: 1 if i in results[x] else 0, self.all_allergens))
            print(f'{i:10s}: {may_contain}')
        print(self.all_allergens)
            
    
    def solve1a(self):
        results = {}
        for a in self.all_allergens:
            #intersect all ing lists that may contain a
            sets = [set(line[0]) for line in self.lines if a in line[1]]
            results[a] = sets[0].intersection(*sets[1:])

        #print(results)
        found_ing = set([])
        for k,v in results.items():
            found_ing = found_ing.union(v)
        good_ing = list(set(self.all_ingredients) - found_ing)
        count = 0
        for ing in good_ing:
            count += sum([1 for line in self.lines if ing in line[0]])
        print(count)

input = 'inputs/day21_input.txt'
#input = 'inputs/day21_small_input.txt'
sol = Solution(input)
sol.solve2()
#print(sol.lines)
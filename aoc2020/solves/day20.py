import numpy as np
import numpy.ma as ma
import re
import math

class Tile():
    def __init__(self, data):
        self.title = re.match(r'Tile ([0-9]+):', data[0]).group(1)
        self.data = np.array(data[1:])
        self.edgemap = [-1, -1, -1, -1]

    def rotate(self):
        self.data = np.rot90(self.data)
        self.edgemap = self.edgemap[1:] + self.edgemap[:1]
        return self

    def flip(self, axis=0):
        self.data = np.flip(self.data, axis)
        if axis==0: #top/bottom flip
            self.edgemap[0], self.edgemap[2] = self.edgemap[2], self.edgemap[0]
        if axis==1: #left/right flip
            self.edgemap[1], self.edgemap[3] = self.edgemap[3], self.edgemap[1]
        return self
    
    def edges(self):
        return [
            self.data[0],     #top
            self.data[:, -1], #right
            self.data[-1],    #bottom 
            self.data[:, 0]   #left
        ]
        

TOP, RIGHT, BOTTOM, LEFT = 0,1,2,3    
class Solution():
    def __init__(self, input):
        self.tiles = []        
        self.process_input(input)
        self.topleft = self.solve_puzzle(self.tiles[0])
        
    def process_input(self, input):
        with open(input) as f:
            data = []
            for line in f:
                line = line.strip()
                if line == '':
                    self.tiles.append(Tile(data))
                    data = []
                else:
                    if line.startswith('Tile'):
                        data.append(line)
                    else:
                        data.append(list(line))
    
    def find_tile(self, title):
        for t in self.tiles:
            if t.title == title:
                return t
        return None

  
    def solve_puzzle(self, tile):
        leftmost = self._solve_puzzle(tile, LEFT)
        topleft = self._solve_puzzle(leftmost, TOP)
        #visit every tile in both axes to complete the edgemaps
        topright = self._solve_puzzle(topleft, RIGHT)        
        tile = topleft
        while tile: #go up/down from every tile in top row
            self._solve_puzzle(tile, BOTTOM)
            self._solve_puzzle(tile, TOP)
            tile = self.find_tile(tile.edgemap[RIGHT])
        
        tile = topleft
        while tile: #go right/left from every tile in left col
            self._solve_puzzle(tile, RIGHT)
            self._solve_puzzle(tile, LEFT)
            tile = self.find_tile(tile.edgemap[BOTTOM])

        return topleft

        

        
    def _solve_puzzle(self, tile, dir):        
        odir = (dir+2) % 4
        match = self._match(tile, dir) #has edge that matches the <dir> edge of tile
        while match is not None:
            self._orient(match, tile, dir)
            tile.edgemap[dir] = match.title
            match.edgemap[odir] = tile.title            
            tile = match
            match = self._match(tile, dir)
        tile.edgemap[dir] = 'e'
        return tile


    def _orient(self, match, tile, dir):
        #print(f'orienting {match.title}')
        edge = tile.edges()[dir]
        match_edge = match.edges()[(dir+2)%4]
        while not(np.array_equal(edge, match_edge) or np.array_equal(edge[::-1], match_edge)):
            match.rotate()
            match_edge = match.edges()[(dir+2)%4]
        if np.array_equal(edge[::-1], match_edge):
            axis = 0 if dir == RIGHT or dir == LEFT else 1
            match.flip(axis)
            match_edge = match.edges()[(dir+2)%4]
        if not(np.array_equal(edge, match_edge)):
            print(f'ERROR {edge}, {match_edge}')
        
    def _match(self, tile, dir):
        edge = tile.edges()[dir]
        for t in self.tiles:
            if t.title == tile.title:
                continue
            #if tile.title in t.edgemap:
            #    continue
            for e in t.edges():
                if np.array_equal(edge, e) or np.array_equal(edge[::-1], e):
                    return t
        return None                
    
    def count_monsters(self, board):
        monster = np.array([
        list('                  # '),
        list('#    ##    ##    ###'),
        list(' #  #  #  #  #  #   ')
        ])

        size = len(board)
        count = 0
        r,c = 0,0        
        for r in range(size-3):
            for c in range(size-20):
                check = board[r:r+3, c:c+20]
                #get the 15 elements of this region that match the mask
                result = check[monster == '#']
                count += 1 if not '.' in result else 0
                c+=1
            r+=1
        print(count)
        return count

                



    def solve1(self):
        """ return the product of the corner tile titles """
        print([tile.title for tile in self.tiles if tile.edgemap.count('e') == 2])
        #print([int(tile.title) for tile in self.tiles if tile.edgemap.count(-1) == 2])
        return math.prod([int(tile.title) for tile in self.tiles if tile.edgemap.count('e') == 2])

    def solve2(self):
        tile_3d = []
        row = self.topleft
        while row:
            tile = row
            while tile:
                tile_3d.append(tile.data[1:-1, 1:-1])
                tile = self.find_tile(tile.edgemap[RIGHT])
            row = self.find_tile(row.edgemap[BOTTOM])

        side = int(math.sqrt(len(tile_3d)))
        data_side = len(tile_3d[0])
        board = np.array(tile_3d).reshape((side,side,data_side,data_side)).transpose(0,2,1,3,).reshape((side*data_side,side*data_side))

        result = ''
        for r in board:
            result+=''.join(r)
            result+='\n'
        #print result
        
        #board could be flipped/rotated, try all 4 rotations and both flips of each (12 total)
        #count the total '#' on the board
        total = np.sum(np.where(board == '#', 1, 0))
        print(total)
        count = 0        
        if count == 0:
            count = self.count_monsters(board)
            
        if count == 0:
            board = np.flip(board, 0)
            count = self.count_monsters(board)
        
        if count == 0:
            board = np.flip(board, 0)
            board = np.flip(board, 1)        
            count = self.count_monsters(board)
        print(f'p2: {total - 15*count}')


input = 'inputs/day20_input.txt'
#input = 'inputs/day20_small_input.txt'
sol = Solution(input)
print(sol.solve1())
print(sol.solve2())

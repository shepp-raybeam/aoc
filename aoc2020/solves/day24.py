import re

class Tile():
    
    def __init__(self, r,c):
        self.color = WHITE
        self.coords = (r, c)
    
    def flip(self):
        self.color = BLACK if self.color == WHITE else WHITE
        
    
    def dirindex(self, dir):
        #row is going to be [-1, 0, +1]
        #col is going to be [-1, 0, +1]
        #3x3 = 9 but we only have 7 positions in a hex and its neighbors
        r,c = self.coords
        if r % 2 == 0:
            if dir == 'ne': return (r-1, c+0) #not c+1
            if dir == 'e':  return (r+0, c+1)
            if dir == 'se': return (r+1, c+0) #not c+1
            #if dir == 'n':  return (r-1, c+0)
            if dir == '.':  return (r+0, c+0)
            #if dir == 's':  return (r+1, c+0)            
            if dir == 'nw': return (r-1, c-1)
            if dir == 'w':  return (r-0, c-1)
            if dir == 'sw': return (r+1, c-1)
            
                        
        if r % 2 == 1:
            if dir == 'ne': return (r-1, c+1)
            if dir == 'e':  return (r+0, c+1)
            if dir == 'se': return (r+1, c+1)
            #if dir == 'n':  return (r-1, c+0)
            if dir == '.':  return (r+0, c+0)
            #if dir == 's':  return (r+1, c+0)
            if dir == 'nw': return (r-1, c+0) #not c-1
            if dir == 'w':  return (r-0, c-1)
            if dir == 'sw': return (r+1, c+0) #not c-1
            
            
input = 'inputs/day24_input.txt'
#input = 'inputs/day24_small_input.txt'
directions = []
with open(input) as f:
    for line in f:
        tokens = re.findall(r'(e|se|sw|w|nw|ne)', line)
        directions.append(tokens)

WHITE, BLACK = 0, 1        


tiles = {}
tile = Tile(0,0)
tiles['0_0'] = tile
for input in directions:
    tile = tiles['0_0']
    for token in input:
        newcoords = tile.dirindex(token)
        key = '{0}_{1}'.format(*newcoords)
        if key in tiles:
            tile = tiles[key]
        else:
            tile = Tile(*newcoords)
            tiles[key] = tile
    tile.flip()
print(f'{len(tiles)} tiles')
print('p1: ', sum([v.color for k,v in tiles.items()]))

def add_border():
    dirs = ['nw', 'w', 'sw', 'ne', 'e', 'se']
    for k, tile in list(tiles.items()):
        neighbor_coords = [tile.dirindex(dir) for dir in dirs]
        neighbor_keys = list(map(lambda nc: '{0}_{1}'.format(*nc), neighbor_coords))
        for i, nk in enumerate(neighbor_keys):
            if not nk in tiles:
                neighbor = Tile(*neighbor_coords[i])
                tiles[nk] = neighbor

def art(days):
    dirs = ['nw', 'w', 'sw', 'ne', 'e', 'se']
    for day in range(1,days+1):
        add_border()
        flips = []
        for k, tile in tiles.items():
            neighbor_coords = [tile.dirindex(dir) for dir in dirs]
            neighbor_keys = list(map(lambda nc: '{0}_{1}'.format(*nc), neighbor_coords))
            neighbors = []
            for nk in neighbor_keys:
                if nk in tiles:
                    neighbors.append(tiles[nk])
            neighborsum = sum([tile.color for tile in neighbors])
            #print(f'{tile.coords}: {[n.color for n in neighbors]} : ({tile.color} - {neighborsum})')
            #Any black tile with zero or more than 2 black tiles immediately adjacent to it is flipped to white.
            #Any white tile with exactly 2 black tiles immediately adjacent to it is flipped to black.
            if tile.color == BLACK and (neighborsum == 0 or neighborsum > 2):
                    flips.append(tile)
            if tile.color == WHITE and neighborsum == 2:
                    flips.append(tile)

        for tile in flips:
            #print(f'flipping {tile.coords} from {tile.color}')
            tile.flip()
        print(f'{day:02d}', sum([v.color for k,v in tiles.items()]))        

art(100)

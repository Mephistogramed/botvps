import numpy as np

BLACK = (0, 0, 0)
YELLOW = (228, 163, 59)
GREEN = (134, 185, 29)
BROWN = (125, 54, 24)
DARK_GREEN = (30, 106, 46)
LIGHT_YELLOW = (238, 232, 145)
WHITE = (255, 255, 255)
DARK_GREY = (175,168,168)
GREY = (216,213,213)
BLUE = (61, 139, 216)
RED = (204, 0, 0)
LIGHT_BLUE = (221, 224, 249)
ICE_BLUE = (164, 172, 249)
simple_map = [BLACK, YELLOW, GREEN, BROWN, DARK_GREEN, LIGHT_YELLOW, WHITE, DARK_GREY, GREY, WHITE, BLUE, RED, LIGHT_BLUE, ICE_BLUE]

TILE_SIZE_IN_PX = 12 # this number have to be divisible by STEP_MARK_SIZE_FACTOR
STEP_MARK_SIZE_FACTOR = 4
STEP_SIZE = int(TILE_SIZE_IN_PX/STEP_MARK_SIZE_FACTOR)

class Tile:
    def __init__(self, x, y, terrain):
        self.row = x
        self.column = y
        self.terrain = terrain
        self.is_on_path = 0
        self.closed = 0
        self.open = 0
        self.g_score = 0
        self.h_score = 0
        self.f_score = 0
        self.prev = None
    def __str__(self):
        if self.prev == None:
            return "Tile:(%s,%s) %s cost:%s f_score:%s prev: None " % ( self.column +1, self.row +1, self.terrain, self.g_score, self.f_score)
        else:
            return "Tile:(%s,%s) %s cost:%s f_score:%s prev: (%s,%s)step cost:%s " % (self.column +1, self.row +1, self.terrain, self.g_score, self.f_score, self.prev.column +1, self.prev.row +1, self.g_score-self.prev.g_score)

    def __lt__(self, other):
        return self.f_score < other.f_score

    def is_same(self, other):
        return self.row == other.row and self.column == other.column

    def to_img(self):
        row_size = TILE_SIZE_IN_PX
        col_size = TILE_SIZE_IN_PX
        colour_size = 3
        tile_img = np.zeros((row_size, col_size, 3))
        # make tile
        for i in range(row_size):
            for j in range(col_size):
                for z in range(3):
                    tile_img [i][j][z] = simple_map [self.terrain][z]
        # make frame
        for i in range(row_size):
            if i ==0 or i== TILE_SIZE_IN_PX-1:
                for j in range(col_size):
                    for z in range(3):
                        tile_img [i][j][z] = simple_map [6][z]
            else:
                for z in range(3):
                    tile_img [i][0][z] = simple_map [6][z]
                    tile_img [i][TILE_SIZE_IN_PX-1][z] = simple_map [6][z]
        # mark step
        if self.is_on_path == 1:
            for i in range(row_size):
                if i >= STEP_SIZE and i < TILE_SIZE_IN_PX-STEP_SIZE :
                    for j in range(col_size):
                        if j>=  STEP_SIZE and j < TILE_SIZE_IN_PX - STEP_SIZE:
                            for z in range(3):
                                tile_img [i][j][z] = simple_map [0][z]

        return tile_img

class Map:
    def __init__(self):
        array_of_tiles = np.empty((0,350), dtype=np.int32)
        with open('map.txt') as f:
            for line in f:
                array_of_tiles = np.vstack((array_of_tiles, np.array(list(map(int, line.split())))))
        self.raw_map = array_of_tiles
        rows = 350
        columns = 350
        self.map_of_tiles = np.empty((350,350), dtype=Tile)
        for i in range(rows):
            for j in range(columns):
                self.map_of_tiles[i,j] = Tile(i,j,self.raw_map[i,j])

class MvpMod:
    def __init__(self, tribe, item, overloaded):
        self.tribe = tribe
        self.item = item
        self.overloaded = overloaded

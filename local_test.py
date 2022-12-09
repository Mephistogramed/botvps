import script
import t as tt
import numpy as np
from PIL import Image

agoniasMap = tt.Map()

def do_magic():

    min_x = 300
    max_x = 260
    min_y = 300
    max_y = 148

    rows = []
    for row in range (min_x,max_x):
        columns_of_row = []
        for column in range (min_y,max_y):
            columns_of_row.append(agoniasMap.map_of_tiles[row,column].to_img())
        rows.append(columns_of_row)

    pixels = np.zeros(((max_x-min_x)*tt.TILE_SIZE_IN_PX, (max_y-min_y)*tt.TILE_SIZE_IN_PX, 3))
    for ii in range((max_x-min_x)*tt.TILE_SIZE_IN_PX):
        for jj in range ((max_y-min_y)*tt.TILE_SIZE_IN_PX):
            for zz in range(3):
                red = rows[int(ii/tt.TILE_SIZE_IN_PX)][int(jj/tt.TILE_SIZE_IN_PX)]
                pixels[ii][jj][zz] = red[ii%tt.TILE_SIZE_IN_PX][jj%tt.TILE_SIZE_IN_PX][zz]

    return pixels
pixels = do_magic()
img = Image.fromarray(np.uint8(pixels), 'RGB')
img.save("Infra.png")

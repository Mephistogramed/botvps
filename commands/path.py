import discord
from discord.ext import commands
import numpy as np
from PIL import Image
import heapq
import asyncio
import io
import t


# Defining an Evo class, within the class, passing client to make the discord module applicable here.
class path(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(pass_context = True)
    # Defining the command "path" as an embed with user's race, x1, y1, x2 and y2 Coordinates as positional arguments.
    async def path(self, ctx, tribe: str, x1: int, y1: int, x2: int, y2: int):
        # Introducing asyncio.cleep with ctx.typing. This will make the bot appear as it's typing,
        # for a given duration of time.
        async with ctx.typing():
            await asyncio.sleep(2)
        
        # Making a list.
        myDict = {}

        # Adding value to the list
        myDict["dwarr"] = [5, 13, 22, 22, 31, 23, 35, 25, 36, -1, -1, -1, -1, -1]
        myDict["leafborn"] = [5, 13, 20, 24, 18, 25, 36, 48, 68, -1, -1, -1, -1, -1]
        myDict["lightfoot"] = [5, 13, 21, 22, 22, 22, 32, 40, 57, -1, 200, -1, -1, -1]
        myDict["mythos"] = [5, 13, 18, 22, 27, 22, 35, 35, 50, -1, -1, -1, -1, -1]
        myDict["giant"] = [5, 13, 19, 20, 38, 22, 32, 32, 45, -1, -1, -1, -1, -1]
        myDict["kiith"] = [5, 13, 22, 19, 22, 18, 38, 46, 65, -1, -1, 200, -1, -1]
        myDict["norsk"] = [5, 13, 20, 23, 26, 24, 27, 31, 44, -1, -1, -1, -1, -1]
        myDict["nuruk"] = [5, 13, 18, 18, 22, 20, 31, 27, 40, -1, -1, -1, -1, -1]

        def get_neigbours(current, agoniasMap):
            neighbours = []
            for i in range (current.row - 1, current.row + 2):
                if i > -1 and i < 350:
                    for j in range (current.column - 1, current.column + 2):
                        if j > -1 and j < 350:
                            candidate_for_neighbour = agoniasMap.map_of_tiles[i, j]
                            if not current.is_same(candidate_for_neighbour):
                                neighbours.append(agoniasMap.map_of_tiles[i, j])

            return neighbours


        def get_straight_step_cost(terrain, mvp_mods):
            return myDict.get(mvp_mods.tribe)[terrain] # TODO other modifiers


        def build_and_mark_path_to(e_tile):
            path=[]
            current_tile = e_tile
            current_tile.is_on_path=1
            path.append(current_tile)
            while current_tile.prev != None:
                current_tile=current_tile.prev
                current_tile.is_on_path=1
                path.append(current_tile)
            return path


        def step_cost(current, neighbour, mvp_mods):
            straight_step_cost = get_straight_step_cost(neighbour.terrain, mvp_mods)
            if current.row==neighbour.row or current.column == neighbour.column: # stright step
                return straight_step_cost
            else:
                return int(1.414 * straight_step_cost)


        def heuristic_estimate_of_distance_between(start, end):
            lowest_diagonal_step_cost = 5
            lowest_straight_step_cost = 3
            x_diff = abs(start.row - end.row)
            y_diff = abs(start.column - end.column)
            number_of_diagonal_steps = min(x_diff, y_diff)
            number_of_straight_steps = abs(x_diff-y_diff)
            return number_of_diagonal_steps * lowest_diagonal_step_cost + number_of_straight_steps * lowest_straight_step_cost


        def find_path(s_tile, e_tile, agoniasMap, mvp_mods):
            print("A* start")
            # https://pl.wikipedia.org/wiki/Algorytm_A*#Algorytm_A*_w_pseudokodzie

            # open_set priority heap of tiles to be checked at start there is only start_tile
            open_set = []
            x = heuristic_estimate_of_distance_between(s_tile, e_tile)
            s_tile.h_score = heuristic_estimate_of_distance_between(s_tile, e_tile)
            s_tile.f_score = s_tile.g_score + s_tile.h_score
            s_tile.open = 1
            print("Start tile %s" % (s_tile))
            heapq.heappush(open_set,(s_tile))
            try:
                while 1>0:
                    current = heapq.heappop(open_set)
                    if current.is_same(e_tile):
                        print("Found path to %s" % (e_tile))
                        return build_and_mark_path_to(e_tile)
                    current.open = 0 # mark as reamoved from open
                    current.closed = 1 # mark as closed
                    neighbours_of_current = get_neigbours(current, agoniasMap)
                    for neighbour in neighbours_of_current:
                        if neighbour.closed == 1 or myDict.get(mvp_mods.tribe)[neighbour.terrain] == -1:
                            continue # this tile was already checked
                        if not neighbour.open == 1:
                            tentative_g_score = current.g_score + step_cost(current,neighbour, mvp_mods)
                            heuristic_estimate = heuristic_estimate_of_distance_between(neighbour, e_tile)
                            neighbour.h_score = heuristic_estimate
                            neighbour.g_score = tentative_g_score
                            neighbour.f_score = tentative_g_score + heuristic_estimate
                            neighbour.prev = current
                            neighbour.open = 1
                            heapq.heappush(open_set,(neighbour))
                        else:
                            if neighbour.g_score > current.g_score + step_cost(current,neighbour, mvp_mods):
                                tentative_g_score = current.g_score + step_cost(current,neighbour, mvp_mods)
                                heuristic_estimate = heuristic_estimate_of_distance_between(neighbour, e_tile)
                                neighbour.prev = current
                                neighbour.g_score = tentative_g_score
                                neighbour.f_score = tentative_g_score + heuristic_estimate

            except:
                print("No path found")

            pass

        def find_path_bounds(path):
            first = path[0]
            bonds = [(first.row, first.row),(first.column, first.column)]
            for tile in path:
                if bonds[0][0] > tile.row:
                    bonds[0] = (tile.row, bonds [0][1])
                if bonds[0][1] < tile.row:
                    bonds[0] = (bonds [0][0],tile.row)
                if bonds[1][0] > tile.column:
                    bonds[1] = (tile.column , bonds[1][1])
                if bonds[1][1] < tile.column:
                    bonds[1] = (bonds[1][0],tile.column)

            return bonds


        def do_magic(path):
            bonds = find_path_bounds(path)

            min_x=bonds[0][0]-1
            max_x=bonds[0][1]+2
            min_y=bonds[1][0]-1
            max_y=bonds[1][1]+2

            rows = []
            for row in range (min_x,max_x):
                columns_of_row = []
                for column in range (min_y,max_y):
                    columns_of_row.append(agoniasMap.map_of_tiles[row,column].to_img())
                rows.append(columns_of_row)

            pixels = np.zeros(((max_x-min_x)*t.TILE_SIZE_IN_PX, (max_y-min_y)*t.TILE_SIZE_IN_PX, 3))
            for ii in range((max_x-min_x)*t.TILE_SIZE_IN_PX):
                for jj in range ((max_y-min_y)*t.TILE_SIZE_IN_PX):
                    for zz in range(3):
                        tt = rows[int(ii/t.TILE_SIZE_IN_PX)][int(jj/t.TILE_SIZE_IN_PX)]
                        pixels[ii][jj][zz] = tt[ii%t.TILE_SIZE_IN_PX][jj%t.TILE_SIZE_IN_PX][zz]

            return pixels

        # Importing the map class from t.py.
        agoniasMap = t.Map()    

        mvp_mods = t.MvpMod(tribe.lower(), None, None)
        #TODO ingame coordinast must be modified by -1 as arrays are indexed from 0
        #TODO also ingame coords in oposit order row, coll then here
        # ingame location 109,122 is in matrix agoniasMap.map_of_tiles[121,108]
        # from(257,172) to (240, 148)
        star_tile = agoniasMap.map_of_tiles[y1 - 1,x1 - 1]
        end_tile = agoniasMap.map_of_tiles[y2 - 1,x2 - 1]

        # Finding the shortest path using A* Algorithm
        path = find_path(star_tile, end_tile, agoniasMap, mvp_mods)
        # Generating the array that has just the start coordinates and the end coordinates. 
        pixels = do_magic(path)
        # Making the Image from the generated array. 
        img = Image.fromarray(np.uint8(pixels), 'RGB')

        # Introducing IO to save the image into memory rather than locally.
        with io.BytesIO() as image_binary:
            img.save(image_binary, 'PNG')
            image_binary.seek(0)

            # Defining the embed for the Pathfind.
            finalembed = discord.Embed(
                title = "Path Finder",
                color = discord.Color.dark_green()
            )

            finalembed.set_footer(text='Forsaken!')
            finalembed.set_thumbnail(url='https://agonialands.com/assets/images/logos/Agonia_Mini_logo_alpha.png')
            finalembed.set_author(name='Calc Bot')
            finalembed.add_field(name = "Tribe", value = tribe.capitalize(), inline = True)
            finalembed.add_field(name = "Current Tile", value = f'({x1},{y1})', inline = True)
            finalembed.add_field(name = "Target Tile", value = f'({x2},{y2})', inline = True)
            finalembed.add_field(name = "Total Movement Costs", value = f'{path[0].g_score} moves needed', inline = False)
            # Using "image_binary" as a fp(filepath) for obtaining the image and using the filename as "image.png". 
            # Discord sees the filename as "image.png", irrespective of the actuale filename.
            # The only area of caution should be the file extension.
            # If the file you want to send is a "gif", then it should be renamed as "image.gif"
            file = discord.File(fp=image_binary, filename='image.png')
            # "embed.set_image" only accepts urls, so we can make it as an attachment if the file is pulled locally.
            finalembed.set_image(url="attachment://image.png")
            # Sending the embed to the respective channel along with the file.
            await ctx.send(file=file, embed=finalembed)
           
    @path.error
    async def path_error(self, ctx, error):
        if isinstance(error, commands.CommandInvokeError):
            embed = discord.Embed(title = "No Path Found.", description = "Error Handling", color = discord.Color.dark_green())
            embed.set_footer(text = 'Forsaken!')
            embed.set_thumbnail(url = 'https://agonialands.com/assets/images/logos/Agonia_Mini_logo_alpha.png')
            embed.set_author(name= "Calc Bot")
            embed.add_field(name = "Possible Error 1", value = "The tribe is spelt incorrectly.", inline = True)
            embed.add_field(name = "Possible Error 2", value = "The given coords are on non-walkable tiles.", inline = False)
            embed.add_field(name = "Possible Error 3", value = "The given coordinates are passing through, starting or reaching from/to water and lava tiles. These are specific to Kiiths and Lightfoots only.", inline = False)
            await ctx.send(embed = embed)
        elif isinstance(error, commands.MissingRequiredArgument):
            embed1 = discord.Embed(title = "Missing Arguments", descripton = "Error Handling", color = discord.Color.dark_green())
            embed1.set_footer(text = 'Forsaken!')
            embed1.set_thumbnail(url = 'https://agonialands.com/assets/images/logos/Agonia_Mini_logo_alpha.png')
            embed1.set_author(name= "Calc Bot")
            embed1.add_field(name = "Possible Error", value = "You may have missed some coordinates, or race type. Please check the required arguments.", inline = True)
            await ctx.send(embed = embed1)
        elif isinstance(error, commands.TooManyArguments):
            embed2 = discord.Embed(title = "Too Many Arguments", description = "Error Handling", color = discord.Color.dark_green())
            embed2.set_footer(text = 'Forsaken!')
            embed2.set_thumbnail(url = 'https://agonialands.com/assets/images/logos/Agonia_Mini_logo_alpha.png')
            embed2.set_author(name= "Calc Bot")
            embed2.add_field(name = "Possible Error", value = "You may have passed too many coordinates or race type. Please check the required arguments.", inline = True)
            await ctx.send(embed = embed2)

# Basic setup of a command. Necessary for loading the commands with the actual main.py file.
async def setup(client):
    await client.add_cog(path(client))

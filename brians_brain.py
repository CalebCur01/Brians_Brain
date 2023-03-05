import arcade
import random
import numpy as np


ROW_COUNT = 100
COLUMN_COUNT = 100
DENSITY = .3

SCREEN_TITLE = "Brian's Brain"

WIDTH = 10
HEIGHT = 10

MARGIN = 0

SCREEN_WIDTH = (WIDTH + MARGIN) * COLUMN_COUNT + MARGIN
SCREEN_HEIGHT = (HEIGHT + MARGIN) * ROW_COUNT + MARGIN

grid = np.zeros((COLUMN_COUNT,ROW_COUNT))
grid2 = np.zeros((COLUMN_COUNT,ROW_COUNT)) #for copying state each turn
sprite_grid = arcade.SpriteList()

COL_0 = arcade.color.BLACK #DEAD
COL_1 = arcade.color.BLUE  #DYING
COL_2 = arcade.color.WHITE #ALIVE


step = 0 #to keep track of what step we are on



class MyGame(arcade.Window):
    def __init__(self,width,height,title):
        super().__init__(width,height,title)

        arcade.set_background_color(arcade.color.WHITE)
        self.spritelist0 = arcade.SpriteList() #list of sprites for tiles
        self.spritelist1 = arcade.SpriteList()
        self.spritelist2 = arcade.SpriteList()

        for row in range(ROW_COUNT):
            for column in range(COLUMN_COUNT):      #We make 3 different lists of spirtes for the 3 different colors
                x = column * (WIDTH + MARGIN) + (WIDTH / 2 + MARGIN)
                y = row * (HEIGHT + MARGIN) + (HEIGHT / 2 + MARGIN)
                sprite_0 = arcade.SpriteSolidColor(WIDTH,HEIGHT,COL_0)
                sprite_1 = arcade.SpriteSolidColor(WIDTH,HEIGHT,COL_1)
                sprite_2 = arcade.SpriteSolidColor(WIDTH,HEIGHT,COL_2)

                sprite_0.center_x = x
                sprite_0.center_y = y

                sprite_1.center_x = x
                sprite_1.center_y = y

                sprite_2.center_x = x
                sprite_2.center_y = y
                

                self.spritelist0.append(sprite_0)
                self.spritelist1.append(sprite_1)
                self.spritelist2.append(sprite_2)

    def on_draw(self):
        self.clear()
        self.spritelist0.draw()
        self.spritelist1.draw()
        self.spritelist2.draw()
        

    def on_update(self,delta_time):
        update_state()
        for row in range(ROW_COUNT):                    
            for column in range(COLUMN_COUNT):          
                location = row * COLUMN_COUNT + column  
                if grid[row][column] == 0:
                    self.spritelist1[location].visible = False
                    self.spritelist2[location].visible = False
                    self.spritelist0[location].visible = True
                if grid[row][column] == 1:
                    self.spritelist0[location].visible = False
                    self.spritelist2[location].visible = False
                    self.spritelist1[location].visible = True
                if grid[row][column] == 2:
                    self.spritelist0[location].visible = False
                    self.spritelist1[location].visible = False
                    self.spritelist2[location].visible = True
        
            
            


def initialize_grid(grid):
    for row in range(ROW_COUNT):
        for column in range(COLUMN_COUNT):
            rand_val = random.random()
            if rand_val <= DENSITY:
                grid[row][column] = 2
                
    
    copy(grid,grid2)
            
            
                

def copy(grid1, grid2): #copies values from left to right
    for row in range(ROW_COUNT):
        for column in range(COLUMN_COUNT):
            grid2[row][column] = grid1[row][column]

def living_neighbors(row,column):
    sum = 0
    if(within_bounds(row-1,column-1)):
        if(grid[row-1][column-1] == 2):
            sum +=1
    if(within_bounds(row-1,column)):
        if(grid[row-1][column] == 2):
            sum+=1
    if(within_bounds(row-1,column+1)):
        if(grid[row-1][column+1] == 2):
            sum+=1
    if(within_bounds(row,column-1)):
        if(grid[row][column-1] == 2):
            sum+=1
    if(within_bounds(row,column+1)):
        if(grid[row][column+1] == 2):
           sum+=1
    if(within_bounds(row+1,column-1)):
       if(grid[row+1][column-1]) == 2:
           sum+=1
    if(within_bounds(row+1,column)):
       if(grid[row+1][column]) == 2:
          sum+=1
    if(within_bounds(row+1,column+1)):
       if(grid[row+1][column+1]) == 2:
          sum+=1
    return sum
    

def within_bounds(x,y):
    if x < 0 or x >= ROW_COUNT:
        return False
    if y < 0 or y >= COLUMN_COUNT:
        return False
    return True


        
def update_state():
    global step


    print("step {}".format(step))
    step +=1


    for row in range(ROW_COUNT):
        for column in range(COLUMN_COUNT):
            if(grid[row][column] == 0): #dead
               neighbors_alive = living_neighbors(row,column)
               if(neighbors_alive == 2):
                   grid2[row][column] = 2 #alive

            if(grid[row][column] == 1): #dying
               grid2[row][column] = 0 #dead

            if(grid[row][column] == 2): #alive
               grid2[row][column] = 1 #dying
    copy(grid2,grid)
               

def main():
    initialize_grid(grid)
    game = MyGame(SCREEN_WIDTH,SCREEN_HEIGHT,SCREEN_TITLE)
    arcade.run()

    
if __name__ == "__main__":
    main()


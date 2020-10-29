import dataclasses
from dataclasses import dataclass

from config import GRID_SIZE 

@dataclass
class Grid:
    position: (int, int) = (0,0)
    graphic: (bool) = False
    text: (str) = ""
    index: (str) = "A0"

    def middle(self) -> (int, int):
        mid_x = GRID_SIZE * self.position[0] + int((GRID_SIZE/2))
        mid_y = GRID_SIZE * self.position[1] + int((GRID_SIZE/2))
        return (mid_x, mid_y)
    
    def is_graphic(self) -> bool:
        return self.graphic



def create_grid(col_total: int, row_total: int):
    total_grid = []
    # the '@' ugly way to offset ascii table, to convert number to Capital letter
    top_row = [Grid(text=(chr(ord('@')+(i))), position=(0,i)) for i in range(0, row_total+1)]
    total_grid.insert(0, top_row)

    for col in range(1, col_total+1):
        grid_row = []
        grid_row.append( Grid(position=(col, 0), text=col) ) # first row will always be the index 
       # print(f'text at {col}, 0')
        for row in range(1, row_total+1):
            index = chr(ord('@')+(row)) + str(col)
            new_grid = Grid(position=(col, row), graphic=True, index=index)
            grid_row.append( new_grid )
        
        total_grid.append(grid_row)
    
    #print(f'total grid size: {len(total_grid)} x {len(total_grid[0])}')
    return total_grid
    

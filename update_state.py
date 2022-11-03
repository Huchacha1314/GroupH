import numpy as np
from utility_functions import *

def update(Grid, pedestrians, targets, distance_matrix, click_flag):
    '''
    Grid : List of Cells row X col
    pedestrian : x, y coordinate values of the pedestrian
    '''

    neighbour_locs = np.array([[1, 1], [1, 0], [1, -1], [0, -1], [0, 1], [-1, 1], [-1, 0], [-1, -1]])
    
    targets = np.array(targets)
    pedestrians = np.array(pedestrians)

    row_size = len(Grid)
    col_size = len(Grid[0])
    
    flag = click_flag
    # 1s
    if flag%5 == 0 or flag%7 == 0 :
        
        for i, p_loc in enumerate(pedestrians):

            p_loc = np.array(p_loc)
            max_loc = p_loc
            present_utility = utility(p_loc, distance_matrix)
            max_utility = present_utility

            for loc in neighbour_locs:
                
                neighbour_loc = p_loc + loc
                x, y = neighbour_loc
                if check_grid_bound(neighbour_loc, col_size, row_size):
                    # If neigbour loc is target, pedestrian or obstacle. Do not move                
                    if Grid[x][y].state in ['target', 'pedestrian', 'obstacle']:
                        continue
                    neighbour_utility = utility(neighbour_loc, distance_matrix)
                    if neighbour_utility > max_utility:
                        max_utility = neighbour_utility
                        max_loc = neighbour_loc

            if abs(max_loc[0]-p_loc[0])==abs(max_loc[1]-p_loc[1]) and flag%7 == 0 :
                Grid[p_loc[0]][p_loc[1]].state = 'empty'
                Grid[max_loc[0]][max_loc[1]].state = 'pedestrian'
                pedestrians[i] = max_loc
                flag = flag - 7
                
            elif abs(max_loc[0]-p_loc[0])!=abs(max_loc[1]-p_loc[1]) and flag%5 == 0:
                Grid[p_loc[0]][p_loc[1]].state = 'empty'
                Grid[max_loc[0]][max_loc[1]].state = 'pedestrian'
                pedestrians[i] = max_loc
                flag = flag - 5
                
            

     
            
   

    return Grid, pedestrians

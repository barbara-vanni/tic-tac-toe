

def ia(grid, player):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == '':  
                return i * 3 + j  
    return False 








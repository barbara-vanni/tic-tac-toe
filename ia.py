import random


# def ia(grid, player, difficulty):
#     if difficulty == "easy" :
#         return easy_move(grid, player)
#     elif difficulty == "medium":
#         return medium_move(grid, player)
#     elif difficulty == "hard":
#         pass
    
# # mouvement aléatoire de l'ia sur des cases vide donc valide 
# def random_move(grid, player):
#     empty_cells = [(i, j) for i in range(3) for j in range(3) if grid[i][j] == '']
#     return random.choice(empty_cells)

def ia(grid, player):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == '':  
                return i * 3 + j  
    return False 

# def medium_move(grid, player):
#     for i in range(len(grid)):
#         for j in range(len(grid[i])):
#             if grid[i][j] == '':  
#                 grid[i][j] = player
#                 if check_winner(grid, player):
#                     return i, j 
#                 grid[i][j]=0
    
#     opponent = 3 - player
#     for i in range(len(grid)):
#         for j in range(len(grid[i])):
#             if grid[i][j] == '':  
#                 grid[i][j] = opponent
#                 if check_winner(grid, opponent):
#                     return i, j 
#                 grid [i][j] = 0
#     return easy_move(grid, player)




    







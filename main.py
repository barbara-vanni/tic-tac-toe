# coding: utf-8

import tkinter as tk
from tkinter import *


# Identifier les 9 cases de mon jeu
# grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
grid = [["", "", ""], ["", "", ""], ["", "", ""]]
# Identifier les joueurs
player = 1

# Création et ouverture fenêtre tkinter
window = tk.Tk()
window.title("TIC.TAC.TOE")
window.geometry("800x800")

center_frame = Frame(window)
center_frame.grid(row=0, column=0, padx=35, pady=50)


# Variable pour compter le nombre de coups
count = 0

# Fonction appelée lorsqu'un bouton est cliqué
def on_button_click(row, col):
    global player, count
    if grid[row][col] == "" and count < 9:
        if player == 1:
            text = "X"
            player = 2
        else:
            text = "O"
            player = 1
        btn = tk.Button(center_frame, text=text, borderwidth=2, relief=tk.GROOVE, font=("Arial", 50), height=2, width=6, bg="white", fg="black", cursor="heart")
        btn.grid(row=row, column=col)
        grid[row][col] = text
        count += 1
        check_winner()


# combinaison gagnante 
def check_winner():
    win= []
    for x in range(3):
        # check pour les lignes et les colonnes 
        if grid[x][0] == grid[x][1] == grid[x][2] != "":
            win += grid[x][0]
            return
        if grid[0][x] == grid[1][x] == grid[2][x] != "":
            win += grid[0][x]
            return
    # check pour les deux diagonales
    if grid[0][0] == grid[1][1] == grid[2][2] != "":
        win += grid[0][0]
        return
    if grid[0][2] == grid[1][1] == grid[2][0] != "":
        win += grid[0][2]
        return
    

# Création de la grille de jeu
def create_board():
    for i in range(3):
        for j in range(3):
            btn = tk.Button(center_frame, text="", borderwidth=2, relief=tk.GROOVE, font=("Arial", 50), height=2, width=6, bg="white", fg="black", cursor="heart", command=lambda i=i, j=j: on_button_click(i, j))
            btn.grid(row=i, column=j)

create_board()

# Ajouter un bouton pour quitter
quit_button = tk.Button(center_frame, text="Quit", command=window.destroy)
quit_button.grid(row=4, column=0, columnspan=1, pady=10)
# ajouter bouton nouvelle partie
new_game_button = tk.Button(center_frame, text="New Game")
new_game_button.grid(row=4, column=0, columnspan=10, pady=0)

window.mainloop()


 

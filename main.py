# coding: utf-8

import tkinter as tk
from tkinter import *


# Identifier les 9 cases de mon jeu
grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# Identifier les joueurs
player = 1

# Création et ouverture fenêtre tkinter
window = tk.Tk()
window.title("TIC.TAC.TOE")
window.geometry("800x800")
# Création de la grille de jeu
def create_board():
    for i in range(3):
        for j in range(3):
            btn_text = str(grid[i][j])
            btn = Button(window, text=btn_text, borderwidth=2, relief=GROOVE, font=("Arial", 50), height=2, width=6, bg="lightblue")
            btn.grid(row=i, column=j)

create_board()


# Ajouter un bouton pour quitter
quit_button = tk.Button(window, text="Quitter", command=window.destroy)
quit_button.grid(row=3, column=0, columnspan=3, pady=10)

window.mainloop()


 

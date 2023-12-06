# coding: utf-8

from subprocess import BELOW_NORMAL_PRIORITY_CLASS
import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk

# Identifier les 9 cases de mon jeu
grid = [["", "", ""], ["", "", ""], ["", "", ""]]
# Identifier les joueurs
player = 1
win_X=0
win_Y=0
tie = 0

# Création et ouverture fenêtre tkinter
window = tk.Tk()
window.title("TIC.TAC.TOE")
window.geometry("1000x800")

center_frame = tk.Frame(window)
center_frame.grid(row=0, column=0, padx=35, pady=50)

message_frame = tk.Frame(window)  
message_frame.place(relx = 0.87, 
                   rely = 0.26,
                   anchor = 's')
# message_frame.grid(row=0, column=1)
 

message_frame.grid_rowconfigure(0, weight=1) 
message_frame.grid_columnconfigure(0, weight=1)  

# Variable pour compter le nombre de coups
count = 0

# images à la place du x et du o
image_x = ImageTk.PhotoImage(Image.open("./assets/X_flamme.png"))
image_o = ImageTk.PhotoImage(Image.open("./assets/O_flamme.png"))

# Fonction appelée lorsqu'un bouton est cliqué
def on_button_click(row, col):
    global player, count
    if grid[row][col] == "" and count < 9:
        if player == 1:
            image = image_o
            player = 2
        else:
            image = image_x
            player = 1

        btn = tk.Button(center_frame, image=image, borderwidth=0, relief=tk.GROOVE, height=200, width=200,bg="white", cursor="heart")
        btn.grid(row=row, column=col)
        grid[row][col] = player  
        count += 1
        check_winner()

# combinaison gagnante 
def check_winner():
    for x in range(3):
        # check pour les lignes et les colonnes 
        if grid[x][0] == grid[x][1] == grid[x][2] != "":
            win(grid[x][0])
            return
        if grid[0][x] == grid[1][x] == grid[2][x] != "":
            win(grid[0][x])
            return
    # check pour les deux diagonales
    if grid[0][0] == grid[1][1] == grid[2][2] != "":
        win(grid[0][0])
        return
    if grid[0][2] == grid[1][1] == grid[2][0] != "":
        win(grid[0][2])
        return

# Fonction pour vérifier s'il y a match nul
def check_tie_game():
    global tie
    if count == 9 and not check_winner():
        msg = tk.Message(message_frame, text = "Match nul !")
        msg.config(font=('impact', 25), borderwidth=5, justify=CENTER)
        msg.grid()
        tie += 1
        reset_game()
        return True
    return False

# Fonction pour réinitialiser le jeu
def reset_game():
    global grid, player, count
    grid = [["", "", ""], ["", "", ""], ["", "", ""]]
    player = 1
    count = 0
    create_board()  

current_message = 0
# message gagnant
def win(winner):
    global player, win_X, win_Y, current_message

    if player == 1:
        win_X += 1
    else:
        win_Y += 1

    msg_text = f"Player{winner} win!"
    current_message = tk.Message(message_frame, text=msg_text)
    current_message.config(font=('impact', 25), borderwidth=5, justify=CENTER)
    current_message.grid(row=0, column=0, pady=8)
    
    update_scores()  # Mettre à jour les scores après chaque victoire
    reset_game()

# Création de la grille de jeu
def create_board():
    for i in range(3):
        for j in range(3):
            btn = tk.Button(center_frame, text="", borderwidth=2, relief=tk.GROOVE, font=("Arial", 50), height=2, width=6, bg="white", fg="black", cursor="heart", command=lambda i=i, j=j: on_button_click(i, j))
            btn.grid(row=i, column=j)

def show_game():
    create_board()

    quit_button.grid(row=4, column=0, columnspan=1, pady=10)
    new_game_button.grid(row=4, column=0, columnspan=10, pady=0)

def start_game():
    # Fonction pour démarrer le jeu depuis la page d'accueil
    welcome_label.grid_forget()
    start_button.grid_forget()
    canvas.destroy()
    show_game()

def new_game():
    # Effacer le contenu du message_frame
    for widget in message_frame.winfo_children():
        # print(widget.winfo_class())
        widget.destroy()


    reset_game()
    show_game()

# Ajouter deux étiquettes pour afficher les scores
label_X = tk.Label(window, text="Joueur X: 0", font=('impact', 25))
label_Y = tk.Label(window, text="Joueur O: 0", font=('impact', 25))
label_X.place(relx = 0.87, 
                   rely = 0.45,
                   anchor = 's')
label_Y.place(relx = 0.87, 
                   rely = 0.55,
                   anchor = 's')

# Fonction pour réinitialiser les scores
def reset_scores():
    global win_X, win_Y
    win_X = 0
    win_Y = 0
    update_scores()

# Fonction pour mettre à jour les étiquettes des scores
def update_scores():

    label_X.config(text=f"Joueur X: {win_X}")
    label_Y.config(text=f"Joueur O: {win_Y}")

def game_loop():

    check_tie_game()
    check_winner()
    update_scores()
    window.after(100, game_loop)# Appel récursif pour continuer la boucle

# Page d'accueil
bg_image = ImageTk.PhotoImage(Image.open("./assets/tictac.png"))
welcome_label = tk.Label(window, image=bg_image)
welcome_label.grid()

# Création du canevas pour afficher l'image de fond
canvas = tk.Canvas(window, width=bg_image.width(), height=bg_image.height())
canvas.grid(row=0)
# Affichage de l'image de fond sur le canevas
canvas.create_image(0, 0, image=bg_image, anchor=tk.NW)

photo = PhotoImage(file='./assets/start_flamme.png')
start_button = tk.Button(window,image=photo, command=start_game)
start_button.grid(row=0, column=0)

# Bouton pour quitter
quit_button = tk.Button(center_frame, text="Quit", command=window.destroy)

# Bouton nouvelle partie
new_game_button = tk.Button(center_frame, text="New Game", command=new_game)

# Lancement de la boucle principale
window.after(100, game_loop)
window.mainloop()

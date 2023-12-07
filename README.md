# tic-tac-toe

Marche à suivre :

    REGLE DU TIC-TAC-TOE

    - choix utilisation PYGAME ou TKINTER
    - 2 pages "différentes" 
        - ACCUEIL : [image en fond] 
            - choix du mode de jeu : solo ou duo 
            - si choix duo, possibilité de cliquer sur un bouton start qui lance le jeu 
            - si choix solo, selection du niveau de difficulté, puis possibilité de sélectionner le bouton start. 
        - GAME: 
            - création fenêtre sur tkinter(1000*800)
            - division de l'écran en plusieurs frame ( définition avec tk.FRAME) 
                    * 2/3 gauche la board de jeu et les boutons quit / new game 
                    * 1/3 droit le compteur de point et les messages de victoire/ match nul

            - création de la board de 3*3 (donc boucle dans une boucle)
                - créer une variable grid en mode tableau de tableau pour identifier les 9 cases du jeu 
            - identification des joueurs avec la variable player ( joueur X et joueur Y)

            GAMEPLAY:
                - def on_click() : si une case est vide et qu'on clique dessus on à le signe qui correspond à notre player qui apparait sur la board. Des qu'un signe est posé, un compteur tourne
                - def check_winner() : en même temps que le remplissage de la grille, on fait la vérification de chaque colonne et ligne ou diagonal 
                - def tie_game() : pour les matchs nuls on fait une fonction où si notre compteur atteint 9 coups et que check_winner() n'a pas marché alors match nul
                - def winner (): pour savoir lequel du joueur 1 ou joueur 2 est le vainqueur 
                    creation variable win_y et win_x defini à zero, qui augmenteront à chaque victoire 
                        - création messages pour afficher les victoires ( faire attention à ce que ça ne soit pas réinitialisé à chaque game)
                        -def update_score() pour mettre a=à jour à chaque fois qu'il y a une victoire de l'un ou de l'autre 
                -def show-game() : qui permet de montrer la board créer plus haut et les deux bouton quit/ new game 
                - bouton quit et bouton new-game à mettre sous la board 
                    - bouton quit avec .commanddestroy
                    -bouton new-game, création d'une fonction new-game() pour quand on clique sur le bouton et qui active une autre fonction reset_game() qui permet de remettre à zero la board en effancant les entrées de la game précédente 

                -gameloop() permettant de faire que le jeu tourne et check_winner/tie_game et update les scores 

    
    IA : 


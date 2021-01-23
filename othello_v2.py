#finir de tt mettre en fonction, puis faire cas par cas vert, horizontalement et les deux diagonales
# problemes des bords a regler 
# affichage





def principal():


    in_game = True
    
    damier = [["." for i in range(8)] for j in range(8)]    #creation et affichage du damier

    damier[3][3], damier[3][4] = "X", "O"           #initialisation des premiers pions de chaque partie
    damier[4][3], damier[4][4] = "O", "X"


    tour = 0



    while in_game:
        

        for ligne in damier:
            print(ligne, end = '\n')

        if tour % 2 == 0:                           # a qui vient le tour
            player, inverse_player = "X", "O"
        else:
            player, inverse_player = "O", "X"

        print(f"C'est à player {inverse_player} de jouer")
        print('Tour =', tour)
        
    
        
        x = int(input("player rentre x : "))                                #ce que rentre le player (x et y dans le damier)
        y = int(input("player rentre y : "))

        x_bis = x
        y_bis = y
    
        if peut_poser_pion(x, y, damier, player, inverse_player):                                               #appelle des fonctions
            damier[y][x] = inverse_player
            vertical(damier, x, inverse_player)
            horizontal(damier, y, inverse_player)
            diagonal_droite(y_bis, x_bis, damier, inverse_player, y, x)
            diagonal_gauche(y_bis, x_bis, damier, inverse_player, y, x)
        
            tour += 1






def peut_poser_pion(x, y, damier, player, inverse_player):
    peut_poser = False
    bord =False
    tour = 0        #init variables 


    if y == 0 or y == 7:
        bord = True
            
    if x == 0 or x == 7:
        bord = True

    if bord:
        print('BORD !')

    if damier[y][x] == ".": #verif que la place n'est pas deja occupé par un pion
        if damier[y+1][x] == player or damier[y-1][x] == player or damier[y][x+1] == player or damier[y][x-1] == player:        #test haut, bas, gauche, droite
            peut_poser = True
            tour += 1
    else:
        print("PAS POSSIBLE, PLACE DEJA OCCUPE PAR UN PION")
        

    if damier[y][x] == ".": #verif que la place n'est pas deja occupé par un pion
        if damier[y+1][x] != inverse_player or damier[y+1][x] == '.':                                #test diagonale et verif que le joueur ne veut pas mettre son
            if damier[y-1][x] != inverse_player or damier[y-1][x] == '.':                            # pion a cote d'un a a lui (haut, bas, gauche, droite)
                if damier[y][x+1] != inverse_player or  damier[y][x+1] == '.':
                    if damier[y][x-1] != inverse_player or damier[y][x-1] == '.':
                        if damier[y-1][x-1] == player or damier[y+1][x+1] == player or damier[y-1][x+1] == player or damier[y+1][x-1] == player:
                            peut_poser = True
                            tour += 1
                
    
    return peut_poser






def horizontal(damier, y, inverse_player):
    # retournement des pions horizontalement
    
    compteur = 0
    ma_liste = []
    pos_x = 1



    for j in damier[y]:
        if j == inverse_player:
            debut_x = (y, compteur)
            break
        compteur += 1
    for pions in damier[y][compteur+1:-1]:
        if pions != '.':
            ma_liste.append((y, debut_x[1]+pos_x))
        if pions == inverse_player:
            print('ma liste =', ma_liste)
            for lignes in ma_liste:
                damier[lignes[0]][lignes[1]] = inverse_player
        pos_x += 1

    pos_x = 1
    compteur = 0
    ma_liste = []
    erreur = False


def vertical(damier, x, inverse_player):
    # retournement des pions verticalement
    
    compteur = 0
    boul = False
    ma_liste = []
    pos_y = 1


    for ligne in damier:

        print(ligne[x])
        if ligne[x] == inverse_player:
            debut_x = (compteur, x)
            print("debut =",debut_x)
            boul = True
            break
        compteur += 1
        if boul:
            break


    print('compteur =', compteur)

    for ligne in damier[compteur+1:-1]:
        if ligne[x] != '.':

            ma_liste.append((debut_x[0]+pos_y, x))
        print('ma liste =', ma_liste)
        if ligne[x] == inverse_player:

            for lignes in ma_liste:
                damier[lignes[0]][lignes[1]] = inverse_player
                boul_2 = True


        pos_y += 1


    pos_y = 1
    compteur = 0
    ma_liste = []
    erreur = False
    boul = False
    boul_2 = False


def diagonal_droite(y_bis, x_bis, damier, inverse_player, y, x):
    #retournement des pions diagonales droite
    erreur = False 
    pos_xx = 1
    ma_liste = []
    avanc = 0

    init = (y_bis, x_bis)
    while y_bis != 0 and x_bis != 0:
        y_bis -= 1
        x_bis -= 1
    init = [y_bis, x_bis]
    print("init = ", init)

    j = damier[init[0]][init[1]]
    for ligne in damier:
        if damier[init[0]][init[1]] == inverse_player:
            debut_x = (init[0], init[1])
            print("debut =",debut_x)
            trouve = True
            break
        else:
            init[0] += 1
            init[1] += 1
            print("init", init)
            print(j)

    for ligne in damier[debut_x[0]+1:-1]:
        if ligne[debut_x[1]+pos_xx] != '.':
            ma_liste.append((debut_x[0]+pos_xx, debut_x[1] + pos_xx))
            print('ma liste =', ma_liste)

        if ligne[debut_x[1]+pos_xx] == inverse_player:
            for ligneuh in ma_liste:
                damier[ligneuh[0]][ligneuh[1]] = inverse_player
            
        pos_xx += 1
        avanc += 1
    
    #                         #variable ancien code, a voir si besoin ;)
    # print('pos xx =', pos_xx)
    # pos_xx = 1
    # ma_liste = []
    # compteur = 0
    # erreur = False 
    # y_bis = y
    # x_bis = x

def diagonal_gauche(y_bis, x_bis, damier, inverse_player, y, x):
    #retournement des pions diagonales gauche
    erreur = False
    pos_xx = 1
    ma_liste = []
    avanc = 0

    init = (y_bis, x_bis)
    while y_bis != 0 and x_bis != 7 :
        y_bis -= 1
        x_bis += 1
    init = [y_bis, x_bis]
    print("init = ", init)

    # j = damier[init[0]][init[1]]
    for ligne in damier[0:-1]:
        if damier[init[0]][init[1]] == inverse_player:
            debut_x = (init[0], init[1])
            print("debut =",debut_x)
            trouve = True
            break
        else:
            init[0] += 1
            init[1] -= 1
            print("init", init)
                

    for ligne in damier[debut_x[0]+1:-1]:
        print(pos_xx)
        if ligne[debut_x[1]-pos_xx] != '.':
            ma_liste.append((debut_x[0]+pos_xx, debut_x[1] - pos_xx))
            print('ma liste =', ma_liste)

        if ligne[debut_x[1]-pos_xx] == inverse_player:
            for ligneuh in ma_liste:
                damier[ligneuh[0]][ligneuh[1]] = inverse_player

        pos_xx += 1
        avanc += 1
                
    pos_xx = 1
    ma_liste = []
    compteur = 0
    erreur = False 












principal()






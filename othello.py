	
import sys, os, random
import pygame



white_color = (220, 220, 220)  # couleur dans variable pour mieux s'y retrouver 
black_color = (0, 0, 0)
red_color = (255, 0, 0)
green_color = (0, 255, 0)



class jeu:  #class principale 



    def __init__(self):

        #Mise en place de la fenêtre et de sa taille
        window_surface_x = 700 #Largeur de la fenêtre
        window_surface_y = 700 #Longueur de la fenêtre



        self.window_surface = pygame.display.set_mode((window_surface_x, window_surface_y))   #resolution de la fenetre
        pygame.display.set_caption('JEU_OTHELLO')                                   #Nom de la fenêtre 


        self.ecran_debut = True         #bool pour changer de fenetre
        self.jeu_en_cours = True        #bool pour changer de fenetre
        self.rectangle = afficher_divers(self.window_surface)  # afficher le rectangle definit dans la class afficher_ divers qui sert pour les contours
        self.grille = afficher_divers(self.window_surface)  #affiche le damier de l'othello definit dans la classafficher_divers
        self.afficher_la_liste_grille = afficher_divers(self.window_surface) #afficher la liste de si il y a un pion ou pas sur la case 
        self.pion = afficher_divers(self.window_surface) 


        self.player_O = 'O'  # pion blanc = O
        self.player_X = 'X'  # pion noir = X


        self.compteur = 0    # compteur pour savoir à qui de jouer 


    def fonction_principale(self):
        
        

        while self.ecran_debut :
            for event in pygame.event.get():
                
                if event.type == pygame.QUIT:
                    sys.exit()             #fermeture du jeu si on appuie sur fermer 
            
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        self.ecran_debut = False            #passage à la fenetre self.jeu_en_cours
                
               
            
                self.window_surface.fill(white_color)   # couleur ecran de debut 
                
                
                pygame.display.flip() #actualise la page 


        while self.jeu_en_cours:
            
            for event in pygame.event.get():
                
                if event.type == pygame.QUIT:
                    sys.exit()                  #fermeture du jeu si on appuie sur fermer
                 
                if event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0]:  # si click gauche 
                    
                    position = pygame.mouse.get_pos() # recup de la position de la souris 
                    position_x, position_y = position[0] , position[1]   

                    if position_x >= 150 and position_x <= 550 and position_y >= 150 and position_y <= 550: # si position de la souris dans le cadre definit du rectangle 
                        print(position)

                        if position_x >= 150:  # pour definir pos_x a partir de zero
                            position_x-=150

                        if position_y >= 150:  # pour definir pos_y a partir de zero 
                            position_y-=150

                        position_x, position_y = position[0]//50 , position[1]//50   # indexiation du cadrillage du damier 
                        position_x-=3  # a partir de zero
                        position_y-=3
                        print(position_x, position_y)

                        if self.compteur % 2 == 0:  # au joueur noir de jouer 
                            self.afficher_la_liste_grille.fixer_valeur(position_x, position_y, self.player_X)

                        else:   # au joueur blanc de jouer 
                            self.afficher_la_liste_grille.fixer_valeur(position_x, position_y, self.player_O)
                        
                        self.compteur += 1  # incrementation du compteur pour les différents tour des joueurs 


                self.window_surface.fill(white_color) 
                self.rectangle.afficher_rectangle()
                self.grille.afficher_grilles()
                self.afficher_la_liste_grille.afficher_liste_grille()
                self.pion.afficher_pion()

                pygame.display.flip()  # actualisation de la page 


class afficher_divers:  # seconde classe pour les elements a afficher 
        
        def __init__(self, window_surface):

            self.window_surface = window_surface 

            self.lignes = [ ((150, 150), (150, 550)), # damier sous forme de liste 
                ((200, 150), (200, 550)),
                ((250, 150), (250, 550)),
                ((300, 150), (300, 550)),
                ((350, 150), (350, 550)),
                ((400, 150), (400, 550)),
                ((450, 150), (450, 550)),
                ((500, 150), (500, 550)),
                ((550, 150), (550, 550)),
                ((150, 150), (550, 150)),
                ((150, 200), (550, 200)),
                ((150, 250), (550, 250)),
                ((150, 300), (550, 300)),
                ((150, 350), (550, 350)),
                ((150, 400), (550, 400)),
                ((150, 450), (550, 450)),
                ((150, 500), (550, 500)),
                ((150, 550), (550, 550)),
                ]
            
            self.grille = [[None for x in range (0, 8)] for y in range (0, 8)] # liste par comprehension pour afficher une liste avec soit None,
                                                                               # soit X, soit O si il y a un pion blanc, noir ou rien !
            
        
        def afficher_grilles(self): # fonction permettant de construire le damier grace a une boucle 
            
            for ligne in self.lignes:
                pygame.draw.line(self.window_surface, black_color, ligne[0], ligne[1], 2)
            
            
        def afficher_pion(self):
            
            for y in range(0, len(self.grille)):
                for x in range(0, len(self.grille)):
                    if self.grille[y][x] == 'X':
                        pygame.draw.circle(self.window_surface, black_color, (100 + (x*50), 100 + (y*50)), 20)
            
            
            
            
                

        def afficher_rectangle(self):  # creation du rectangle 'cadre'

            self.rectangle_principale = pygame.draw.rect(self.window_surface, red_color, (150, 150, 400, 400), 3)
    
        def afficher_liste_grille(self): # print la liste par comprehension
            pass
            # print(self.grille)

        def fixer_valeur(self, x, y, valeur):  # definit si c'est X ou O dans le tableau à deux dimensions 

            self.grille[x][y] = valeur
        


if __name__ =='__main__':  

    pygame.init()                   #initialisation de toutes les méthodes pygame 
    jeu().fonction_principale()     
    pygame.quit()                   # fermeture de toutes les méthodes pygame 
                
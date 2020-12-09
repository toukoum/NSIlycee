# ##----------------------------
# ##exercice 1
# ##----------------------------

# def carre() -> str:
#     """
#         fonction qui renvoit les carré des entiers de 1 à 10
#     """
#     carré = 0
#     valeur = []
#     for i in range(1, 11):
#         carré = i ** 2
#         valeur.append(carré)
#     return valeur

# print(carre())


# ##----------------------------
# ##exercice 2
# ##----------------------------

# def valeur_chiffre(valeur : int) -> list:
#     """
#         fonction qui prend un nombre en parametre et qui renvoit la liste
#         des chiffres qui le compose
#     """
#     assert(valeur)>= 0
#     assert(type(valeur) == int)
#     valeur = str(valeur)
#     ma_liste = []
#     for i in valeur:
#         ma_liste.append(int(i))
#     return ma_liste

# assert(valeur_chiffre(123) == 1, 2, 3)
# print(valeur_chiffre(154))


# def valeur_chiffre(valeur : int) -> list: #pas fini
#     """
#         fonction qui prend un nombre en parametre et qui renvoit la liste
#         des chiffres qui le compose
#     """
#     assert(valeur)>= 0
#     assert(type(valeur) == int)

#     compteur_d = 0
#     compteur = 0


# assert(valeur_chiffre(123) == 1, 2, 3)
# print(valeur_chiffre(11))

# ##----------------------------
# ##exercice 3
# ##----------------------------

# from math import *

# def crible(n : int) -> list:
#     """
#         fonction qui renvoit un liste des nombre premier inferieur ou egal a n
#     """
#     assert(n >= 10)
#     assert(type(n) == int)

#     nombres, premiers = [],[]

#     for i in range(2,n+1):
#         nombres.append(True)
#     for i in range(2,n+1):
#         if nombres[i-2]:
#             premiers.append(i)
#             for j in range(2*i, n+1, i):
#                 nombres[j-2] = False
#     return premiers

# assert(crible(10) == [2, 3, 5, 7])
# print(crible(100))

##----------------------------
##exercice 4
##----------------------------

def mot_liste(test: str) -> list: #pas fini
    """
        Fonction qui renvoit la liste de mot d'une phrase
    """
    assert(type(test)== str)
    list_return = []
    mot = []
    for lettre in test:
        if lettre != ' ':
            mot.append(lettre)
        else:
            list_return.append(''.join(mot))
            mot = []
    return list_return

test = 'tu aimes la salade, mais pas la sauce'
print(mot_liste(test))
print(test.split())
# # ----------------------------
# # Exercice 1
# # ----------------------------

# from random import *

# def nbre_fois(nbre_tirage, nbre_return : int) -> int:
#     """
#         Fonction renvoyent le nombre de fois qu'un nombre est tiré au sort d'un dictionaire.
#     """
#     assert(type(nbre_return) == int and type(nbre_tirage) == int)
#     assert(nbre_return > 0 and nbre_return <= 6)
#     assert(nbre_tirage > 0)

#     mon_diko = {1: 0, 2: 0, 3: 0, 4: 0, 5:0, 6:0}

#     for i in range(nbre_tirage):
#         x = randint(1, 6)
#         mon_diko[x] += 1
    
#     return mon_diko[nbre_return]

# assert(nbre_fois(100, 1) >= 0)
# print(nbre_fois(100, 3))



# # ----------------------------
# # Exercice 2
# # ----------------------------


# def compte_lettre(chaine_de_test : str) -> dict:
#     """
#         Fonction qui prend en parametre une chaine de caractère et qui renvoit un dictionaire avec les lettres
#         présente dans la chaine de caractère et le nombre de fois où elles apparaissent.
#     """
#     assert(type(chaine_de_test) == str)
#     assert(len(chaine_de_test) > 0)

#     mon_diko = {}

#     for i in chaine_de_test:
#         if i not in mon_diko:
#             mon_diko[i] = 1
#         else:
#             mon_diko[i] += 1
        
#     return mon_diko


# assert(compte_lettre("hello") == {"h": 1, "e": 1, "l": 2, "o": 1})

# print(compte_lettre("comment ca va la street ??"))


# ----------------------------
# Exercice 3
# ----------------------------


dico = {'I':'je','am':'suis','is':'est','a':'un(e)','girl':'fille',
        'boy':'garçon', 'nice':'joli(e)','he' : 'il', 'she' : 'elle',
        'eats' : 'mange', 'apple' : 'pomme', 'banana' : 'banane'}

def traduis(ch:str)->str :
    """
        Traduit la chaine ch de l'anglais en français
    """
    assert(type(ch) == str)
    assert(len(ch)>0)

    liste_francais = []
    liste_mot = ch.split(' ')
    
    for mot in liste_mot:
        mot = dico[mot]
        liste_francais.append(mot)
    
    trad = ' '.join(liste_francais)

    return trad



def translate(ch:str)->str :
    """
        Traduit la chaine ch du français en anglais
    """
    assert(type(ch) == str)
    assert(len(ch)>0)
    liste_anglais = []
    liste_mot = ch.split(' ')

    for mot in liste_mot:
        mot = [k  for (k, val) in dico.items() if val == mot]
        liste_anglais.append(''.join(mot))
    
    trad = ' '.join(liste_anglais)
    return trad


assert(traduis('she eats a banana') == 'elle mange un(e) banane')
assert(translate('elle mange un(e) banane') == 'she eats a banana')
print(traduis('he is a nice boy'))
print(translate('un(e) fille mange un(e) joli(e) pomme'))








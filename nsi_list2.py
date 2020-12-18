#----------------------------
# EXERCICE 1
#----------------------------

liste_carre = [k*k for k in range(1, 11)]
print(liste_carre)


#----------------------------
# EXERCICE 2
#----------------------------


liste_multiple = [ k for k in range(101) if k%5 == 0 or k% 7 == 0 ]
print(liste_multiple)


#----------------------------
# EXERCICE 3
#----------------------------


"""
    Ce programme liste tous les nombres premiers de 1 à 100
    il affiche donc dans la console :
    >>> [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

"""


#----------------------------
# EXERCICE 4
#----------------------------

Daltons = [('Joe', 150), ('William', 165), ('Jack', 180), ('Averell', 195)]
taille_de_Jack = Daltons[2][1]

for nom in Daltons:
    print('Nom : ', nom[0], ', il mesure :', nom[1], 'cm; ')

#----------------------------
# EXERCICE 5
#----------------------------

def damier(n:int) -> list:
    """
        Fonction qui renvoit un damier de longeur et de largeur n
    """
    assert(n >= 0)
    assert(type(n)==int)

    damiex = []
    if n%2 != 0:
        x = n+1
    else:
        x = n
    while len(damiex) != x:
        listeuh_1 = [0 for i in range(n//2)]
        for i in range(0, n, 2): 
            listeuh_1.insert(i, 1)
        damiex.append(listeuh_1)

        listeuh_0 = [1 for i in range(n//2)]
        for i in range(0, n, 2): 
            listeuh_0.insert(i, 0)
        damiex.append(listeuh_0)    

    return damiex

assert(damier(2) == [1, 0], [0, 1])

for k in damier(8):
    print(k, end ='\n')

print('\n')
print('________________________________')
print('\n')

for k in damier(8):    
    string = [str(integer) for integer in k]
    a_string = "".join(string)
    print(a_string)

   
#----------------------------
# EXERCICE 6
#----------------------------
         

def matrice_true(matrice : list) -> bool:
    """
        Fonction qui verifie si une matrice est symetrique ou non
    """

    assert(type(matrice) == list)

    return colonne_ligne(matrice) and index(matrice)
    

def colonne_ligne(matrice : list) -> bool:
    """
        Fonction qui verifie si il y a autant de lignes que de colonees dans matrice et qui vérifie si 
        chaque ligne comporte le même nombre d'éléments
    """
    for k in matrice:
        if len(matrice)!=len(k):
            return False
            break
        else :
            return True



def index(matrice : list) -> bool:
    """
        Fonction qui vérifie que pour tout i et j, on a m[i][j] == m[j][i]
    """
    compteur = 0
    for liste in range(len(matrice)):
        for j in range(len(matrice)):

            i = compteur
            if matrice[i][j] == matrice[j][i]:
                a = True
            else:
                a = False
                break
        
        compteur+=1
    
    return a  
        

assert(matrice_true([[0, 3, 2], [3, 0, 1], [2, 1, 0]]) == True)

matrice_test = [[0, 1, 2, 3], [1, 4, 3, 2 ], [2, 3, 0, 1 ], [3, 2, 1, 0]]
print(matrice_true(matrice_test))


#----------------------------
# EXERCICE 7
#----------------------------

def modif_ls(l1 : list) -> list:
    """
        Fonction qui renvoit une copie de liste qu'on peut modifier sans mosifier l1
    """
    assert(type(l1)== list)

    l2 = [i for i in l1]
    l2.pop(1)
    return l2


test_liste = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print(modif_ls(test_liste))
print(test_liste)



def modif_ls(l1 : list) -> list:
    """
        Fonction qui renvoit une copie de liste qu'on peut modifier sans mosifier l1
    """
    assert(type(l1)== list)

    l2 = [i for i in l1]
    del l2[1]
    return l2


test_liste = [[0, 1], [1, 2], [3, 4], [5, 6], [7, 8, 9]]

print(modif_ls(test_liste))
print(test_liste)


#----------------------------
# EXERCICE 8
#----------------------------



def inverse(l : list) -> list:
    """
        Fonction qui revoit la liste inverse de l mais sans modifier l
    """
    assert(type(l) == list)
    
    l2 = [i for i in l]
    for i in range(len(l)//2):
        l2[i], l2[len(l2) - i - 1] = l2[len(l) - i - 1], l2[i]
    return l2


assert(inverse([1, 2, 3]) == [3, 2, 1])

test_listeuh = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(inverse(test_listeuh))
print(test_listeuh)

assert(test_listeuh == [1, 2, 3, 4, 5, 6, 7, 8, 9])
# ----------------------------------
# EXERCICE 1
# ---------------------------------

l1 = ['pomme', 'abricot', 'fraise']

def dans(liste: list, fruit: str)-> bool:
    """
        Fonction qui verifie si le fruit est présent dans le catalogue
    """
    assert(type(l1)== list)
    assert(type(fruit)== str)

    dedans = False
    for i in liste:
        if i == fruit:
            dedans = True

    return dedans


assert(dans(l1, 'banane') == False)
print(dans(l1, 'abricot'))


# ----------------------------------
# EXERCICE 2
# ---------------------------------

l1 = ['pomme', 'abricot', 'fraise']

def indice(liste: list, valeur: str)-> bool:
    """
        Fonction qui renvoit la position (index) de l'élément si il est présent dans la liste
    """
    assert(type(l1)== list)
    assert(type(valeur)== str)

    i = 0

    for élément in liste:
        if élément == valeur:
            return i
        i += 1

    else:
        return None


assert(indice(l1, 'banane') == None)
print(indice(l1, 'pomme'))


# ----------------------------------
# EXERCICE 3
# ---------------------------------

l1 = ['pomme', 'abricot', 'fraise', 'pomme']

def compte(liste: list, valeur: str)-> bool:
    """
        Fonction qui compte le nombre de fois où un élément est présent dand la liste
    """
    assert(type(l1)== list)
    assert(type(valeur)== str)

    i = 0

    for élément in liste:
        if élément == valeur:
            i += 1


    return i


assert(compte(l1, 'banane') == 0)
print(compte(l1, 'pomme'))


# ----------------------------------
# EXERCICE 4
# ---------------------------------

l1 = ['pomme', 'abricot', 'fraise']

def minimum(liste: list)-> str:
    """
        Fonction qui renvoit l'élément le plus petit de la liste ('banane' < 'pastèque')
    """
    assert(type(l1)== list)

    petit = l1[0]

    for élément in liste:
        if élément < petit:
            petit = élément

    if liste != []:
        return petit
    else:
        return None


print(minimum(l1))


# ----------------------------------
# EXERCICE 5
# ----------------------------------

l1 = ['pomme',  'abricot', 'fraise']

def indice_min(liste: list)-> str:
    """
        Fonction qui renvoit l'index de l'élément le plus petit de la liste ('banane' < 'pastèque')
    """
    assert(type(l1)== list)

    petit = l1[0]
    i = 0
    index = 0

    for élément in liste:
        if élément < petit:
            petit = élément
            index = i
        i += 1

    if liste != []:
        return index
    else:
        return None

assert(indice_min(l1) == 1)
print(indice_min(l1))



# Question à l'écrit :

# -  On définit la liste du catalogue de fruit (avec tous les fruits dedans).

# -  On parcours la liste à l’aide de la boucle for et si l’élément i de la liste correspond à l’élément rechercher, on retourne True, sinon on retourne False.

 

# -  On définit la liste du catalogue de fruit (avec tous les fruits dedans).

# - On définit la valeur la plus petite de la liste qui sera par défaut le premier élément de la liste

# - En parcourant la liste, si l’élément est plus petit que le premier élément de la liste, il devient l’élément le plus petit de la liste.

# - On vérifie si la liste n’est pas vide puis on retourne l’élément le plus petit de la liste.

 
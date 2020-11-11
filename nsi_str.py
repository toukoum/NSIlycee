


# ____________________________________________________________
# EXERCICE 1
# ____________________________________________________________


def demande() -> str:
    """
        chaine affichée caractère par caratctère
    """
    x = 1
    while x == 1:
        chaine = input('Entrez une chaine de caractère : ')
        if not "".join(chaine.split(' ')).isalpha():
            print("Ooops ! Ce n'est pas une chaine de caractère !")
            x = 1
        else:
            x = 0
    for i in chaine:
        print(i)

print(demande())



# ____________________________________________________________
# EXERCICE 2
# ____________________________________________________________

def nbr_e() -> int:
    """
        Détermine combien il y a de 'e' dans une chaine de caractère saisie par l'utilisateur
    """
    x = 1
    while x == 1:
        chaine = input('Entrez une chaine de caractère : ')
        if not "".join(chaine.split(' ')).isalpha():
            print("Ooops ! Ce n'est pas une chaine de caractère !")
            x = 1
        else:
            x = 0
    compteur = 0
    for i in chaine:
        if i == 'e' or i == 'é' or i == 'è' or i == 'E' or i == 'É':
            compteur += 1

    return compteur

print(nbr_e())


# ____________________________________________________________
# EXERCICE 3
# ____________________________________________________________

def double_vowels() -> str:
    """
        Fonction qui double le voyelles d'une chaines de caractère saisie pas l'utilisateur
        avec la boucle while et l'indexiation
    """
    x = 1
    while x == 1:
        chaine = input('Entrez une chaine de caractère : ')
        if not "".join(chaine.split(' ')).isalpha():
            print("Ooops ! Ce n'est pas une chaine de caractère !")
            x = 1
        else:
            x = 0
    i = 0
    while i<len(chaine):
        print(chaine[i], end = '')
        if chaine[i] == 'a' or chaine[i] == 'e' or chaine[i] == 'i' or chaine[i] == 'o' or chaine[i] == 'u' or chaine[i] == 'y':
            print(chaine[i], end = '')
        i += 1
    print('\n')



print(double_vowels())


def double_vowels_bis() -> str:
    """
        Fonction qui double le voyelles d'une chaines de caractère saisie pas l'utilisateur
        avec la méthode .replace
    """
    x = 1
    while x == 1:
        chaine = input('Entrez une chaine de caractère : ')
        if not "".join(chaine.split(' ')).isalpha():
            print("Ooops ! Ce n'est pas une chaine de caractère !")
            x = 1
        else:
            x = 0
    chaine_1 = chaine.replace('a', 'aa')
    chaine_2 = chaine_1.replace('e', 'ee')
    chaine_3 = chaine_2.replace('i', 'ii')
    chaine_4 = chaine_3.replace('o', 'oo')
    chaine_5 = chaine_4.replace('u', 'uu')
    chaine_6 = chaine_5.replace('y', 'yy')
    return chaine_6

print(double_vowels_bis())



# ____________________________________________________________
# EXERCICE 4
# ____________________________________________________________

def reverse() -> str:
    """
        Fonction qui inverse les lettres d'un mot saisie par l'utilisateur
    """
    x = 1
    while x == 1:
        chaine = input('Entrez une chaine de caractère : ')
        if not "".join(chaine.split(' ')).isalpha():
            print("Ooops ! Ce n'est pas une chaine de caractère !")
            x = 1
        else:
            x = 0
    return chaine[::-1]

print(reverse())

def zorglangue() -> str:
    """
        Fonction qui inverse les lettres d'un mot mais pas de la phrase entière
    """
    x = 1
    while x == 1:
        chaine = input('Entrez une chaine de caractère : ')
        if not "".join(chaine.split(' ')).isalpha():
            print("Ooops ! Ce n'est pas une chaine de caractère !")
            x = 1
        else:
            x = 0
    chaine_2 = "".join(reversed(chaine))
    chaine_3 = chaine_2.split(' ')
    chaine_4 = ' '.join(reversed(chaine_3))
    return chaine_4

print(zorglangue())

# ____________________________________________________________
# EXERCICE 5
# ____________________________________________________________


def palindrome() -> str:
    """
        Fonction qui vérifie si un mot est un palindrome ou non
    """
    x = 1
    while x == 1:
        chaine = input('Entrez une chaine de caractère : ')
        if not "".join(chaine.split(' ')).isalpha():
            print("Ooops ! Ce n'est pas une chaine de caractère !")
            x = 1
        else:
            x = 0
    if chaine.replace(' ', '').lower() == chaine.replace(' ', '').lower()[::-1]:
        return True
    else:
        return False

print(palindrome())

# ____________________________________________________________
# EXERCICE 6
# ____________________________________________________________

# Si s est la chaîne, on la découpe en tranches de longueur 1 avec un slice de la forme
# s[k*p:(k+1)*p] qu’on place ensuite dans une liste en compréhension dont on rassemble les éléments tout en insérant
# le séparateur avec la méthode join. D’où le code suivant :

def asterisque(sep) -> str:
    """
        Fonction qui intercalle des asterisque entre les mot
        d'une chaine de caractère saisie par l'utilisateur
    """
    x = 1
    while x == 1:
        chaine = input('Entrez une chaine de caractère : ')
        if not "".join(chaine.split(' ')).isalpha():
            print("Ooops ! Ce n'est pas une chaine de caractère !")
            x = 1
        else:
            x = 0
    return sep.join([chaine[i*1:(i+1)*1] for i in range(len(chaine)//1)])

print(asterisque('*'))


# ____________________________________________________________
# EXERCICE 7
# ____________________________________________________________


def compte_mots_1() -> int:
    """
        Fonction qui revoit le nombre de mot d'une phrase
    """
    phrase = input('Entrez une chaine de caractère : ')
    return len(phrase.split())

print(compte_mots_1())

def compte_mots_2() -> int:
    """
        Fonction qui revoit le nombre de mot d'une phrase (bis)
    """
    chaine = input('Entrez une chaine de caractère : ')
    charactère_précedent = ' '
    nb_mots = 0
    for char in chaine:
        nb_mots += int(charactère_précedent == ' ' and char != ' ')
        charactère_précedent = char
    return nb_mots

print(compte_mots_2())
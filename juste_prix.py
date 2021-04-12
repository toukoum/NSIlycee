
def dicho () -> tuple:
    """
        Fonction qui trouve le nombre qu'a choisie l'utilisateur entre 1 et 100
    """
    
    a = 1
    b = 100
    nbre_coup = 0

    while a != b:
        nbre_coup += 1
        milieu = (a+b)//2
        print(milieu)
        demande = input('Plus (+), Moins (-) ou Egale(=) ?  : ')

        if demande == '+':
            a = milieu + 1
        
        elif demande == '-':
            b = milieu - 1

        else:
            a = b = milieu
        
    return milieu, nbre_coup



result = dicho()

print("Le nombre que tu as choisis est : {} J'ai trouvé en {} coups, je suis le boss !!!".format(result[0], result[1]))
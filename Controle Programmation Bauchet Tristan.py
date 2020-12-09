grille =['*','*','*','*','*','*','*','*','*']

print("1 2 3")
print("4 5 6")
print("7 8 9")

joueur = "X"
tour = 1
victoire_user = 0



def ajouteSymbole(joueur):

    caseOk = 0

    while(caseOk != 1):

        numeroCase = int(input("Numero de case ?"))
        numeroCase = numeroCase - 1

        if(grille[numeroCase]=='*'):

            caseOk = 1

    grille[numeroCase] = joueur




def afficher_grille():

    for i in range(3):

        print(grille[i*3],grille[i*3+1],grille[i*3+2])




def joueur_O_X(joueur_f):

    if(joueur_f == "X"):
        joueur = "O"
    else:
        joueur = "X"
    return joueur




def win(victoire):
    for i in range(3):

        if (grille[i*3] == grille[i*3+1] == grille[i*3+2] != "*"):
            victoire = 1

        if (grille[i] == grille[i+3] == grille[i+6] != "*"):
            victoire = 1

    for i  in range(2):

        if (grille[i+i] == grille[i+4-i] == grille[i+8-(i*3)] != "*"):
            victoire = 1

    return victoire






while (tour<=9 and victoire_user ==0):

    ajouteSymbole(joueur)
    afficher_grille()
    victoire_user = win(victoire_user)
    joueur = joueur_O_X(joueur)
    tour = tour+1


if(victoire_user ==1):
    joueur = joueur_O_X(joueur)
    print("le joueur",joueur,"a gagné")

else:

    print ("match nul")


input()

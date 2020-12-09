import random

from colorama import init
init()
from colorama import Fore, Back, Style


i = 0

grille = ["*","*","*","*","*","*"]

mot_joueur = ["1","2","3","4","5","6"]

nombre_aleatoire = random.randint(0,9)




def compare_mot():

    for i in range (0,6): #len = longueur du mot
        x1 = 0
        x2 = 0

        if mot_joueur[i] in motchoisi[i]:

            grille[i] = mot_joueur[i]

            print("La lettre",end=" ")
            print(Fore.RED + mot_joueur[i],end=" ")
            print(Style.RESET_ALL,end="")
            print("est bien placé")

            if mot_joueur[i] in motchoisi[1] or mot_joueur[i] in motchoisi[2] or mot_joueur[i] in motchoisi[3] or mot_joueur[i] in motchoisi[4] or mot_joueur[i] in motchoisi[5]:
                for a in range (0,6):

                    if mot_joueur[i] in motchoisi[a]:

                        x1 = x1+1

                print("La lettre",end=" ")
                print(Fore.RED + mot_joueur[i],end=" ")
                print(Style.RESET_ALL,end="")
                print("est presente",x1,"fois dans le mot")


        else :

            if mot_joueur[i] in motchoisi[1] or mot_joueur[i] in motchoisi[2] or mot_joueur[i] in motchoisi[3] or mot_joueur[i] in motchoisi[4] or mot_joueur[i] in motchoisi[5]:
                print("La lettre",end=" ")
                print(Fore.YELLOW + mot_joueur[i],end=" ")
                print(Style.RESET_ALL,end="")
                print("n'est pas au bonne endroit")
                for a in range (0,6):

                    if mot_joueur[i] in motchoisi[a]:

                        x2 = x2+1

                print("La lettre",end=" ")
                print(Fore.YELLOW + mot_joueur[i],end=" ")
                print(Style.RESET_ALL,end="")
                print("est presente",x2,"fois dans le mot")

            else :
                print("lettre",mot_joueur[i],"fausse")
                print("La lettre",end=" ")
                print(Fore.BLUE + mot_joueur[i],end=" ")
                print(Style.RESET_ALL,end="")
                print("fausse")


    print("les lettre  correct sont",end=" ")
    print(Fore.RED,grille)
    print(Style.RESET_ALL,end="")



def lettre_mot():

    for i in range(0,6):

        mot_joueur[i] = input("lettre ?")

    print("votre mot est",mot_joueur)






if (nombre_aleatoire == 0):
    motchoisi = ["c","i","t","r","o","n"]

if (nombre_aleatoire == 1):
    motchoisi = ["w","a","p","i","t","i"]

if (nombre_aleatoire == 2):
    motchoisi = ["w","e","b","c","a","m"]

if (nombre_aleatoire == 3):
    motchoisi = ["w","a","s","a","b","i"]

if (nombre_aleatoire == 4):
    motchoisi = ["t","w","i","s","t","e"]

if (nombre_aleatoire == 5):
    motchoisi = ["s","w","i","n","g","s"]

if (nombre_aleatoire == 6):
    motchoisi = ["a","c","a","j","o","u"]

if (nombre_aleatoire == 7):
    motchoisi = ["a","b","u","s","e","e"]

if (nombre_aleatoire == 8):
    motchoisi = ["a","b","i","m","e","s"]

if (nombre_aleatoire == 9):
    motchoisi = ["a","b","u","t","e","z"]



print(motchoisi)

while i != 8 :
    i=i+1
    lettre_mot()
    compare_mot()
    #victoire ?
    if grille == motchoisi :
        print ("bravo vous avez win")
        i=8;
    else :
        print("Réessayer :D")
print("perdu,cheeh !")

import random
nombre_aleatoire = random.randint(0,9)

i = 0
x = 0

motchoisi = ["c","i","t","r","o","n"]
print(motchoisi)

grille = ["*","*","*","*","*","*"]

mot_joueur = ["1","2","3","4","5","6"]




def compare_mot():

    for i in range (0,6): #len = longueur du mot

        if mot_joueur[i] in motchoisi[i]:

            print("lettre",i+1,"vrai")

            grille[i] = mot_joueur[i]

        else :


            if mot_joueur[i] in motchoisi[1] or mot_joueur[i] in motchoisi[2] or mot_joueur[i] in motchoisi[3] or mot_joueur[i] in motchoisi[4] or mot_joueur[i] in motchoisi[5]:

                for a in range (0,6):

                    if mot_joueur[i] in motchoisi[a] :
                        x = x+1
                        print("la lettre",i+1,"n'est pas au bonne endroit")
                        print("la lettre",i+1"est presente",x,"fois dans le mot")

            else :
                print("lettre",i+1,"fausse")


    print("les lettre  correct sont",grille)



def lettre_mot():

    for i in range(0,6):

        mot_joueur[i] = input("lettre ?")

    print("votre mot est",mot_joueur)



while i != 8 :

    lettre_mot()
    compare_mot()
    #victoire ?
    if grille == motchoisi :
        print ("bravo vous avez win")
        i=8;
    else :
        print("alors on trouve pas le bouffe ?")

import random


motchoisi = ["bonjour"]
mot_joueur = ["bonjou5"]

nombre_aleatoire = random.randint(0,9)





def teste():

      for i in range (0,6): #len = longueur du mot

        if mot_joueur[i] in motchoisi[i]:
            print("boby")
        else :
            print("boby faux")

teste()


input()

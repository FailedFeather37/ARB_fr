import random
from affiche_dot import *

GAUCHE = 0
DROITE= 1
compteur=0

def lire_mots():
    with open("liste_mot.txt","r",encoding="utf-8") as fichier:
         mots=[]
         for i in range(20):
             l=fichier.readline()
             l=l.strip()
             mots.append(l)
    random.shuffle(mots)
    return mots


MOTS = lire_mots()

class ABR:
    def __init__(self, mot=None):
        self.value = mot
        self.fils = [None, None]

    def presence_fils(self):
        if self.fils[GAUCHE]==None and self.fils[DROITE]==None:
           return False
        else:
             return True

    def hauteur(self):
        if MOTS == 0:
           return "Hauteur Nulle, Arbre vide"
        else:
             pass

    def ajouter(self, mot):
        global compteur
        if compteur==0:
        #if self.presence_fils()==False:
            self.value=mot
        else:
             if mot > self.value:
                if self.fils[DROITE]!=None:
                    pass
                else:
                    self.fils[DROITE]=mot
             else:
                if self.fils[GAUCHE]!=None:
                    pass
                else:
                    self.fils[GAUCHE]=mot

    def nb_operation_pour_trouver(self, mot):
        # compte le nombre d'operation pour trouver le mot dans l'ABR
        pass

    def afficher(self):
        contenu, _ = self.afficher_interne(0)
        return contenu

    def afficher_interne(self, id_noeud):
        id_initial = id_noeud
        contenu = str(id_initial) + '[label="' + self.value + '"]\n'

        if self.fils[GAUCHE]:
            contenu_fils, id_noeud = self.fils[GAUCHE].afficher_interne(id_noeud + 1)
            contenu += contenu_fils + str(id_initial) + "->" + str(id_initial + 1) + "\n"

        if self.fils[DROITE]:
            id_droite = id_noeud + 1
            contenu_fils, id_noeud = self.fils[DROITE].afficher_interne(id_droite)
            contenu += contenu_fils + str(id_initial) + "->" + str(id_droite) + "\n"

        return contenu, id_noeud

def trouver_lineaire(mot):
    liste=lire_mots()
    for i in range(len(liste)):
        if liste[i]==mot:
            return i

print("Nombre de mot :", len(MOTS))


arbre = ABR()
for mot in MOTS:
    arbre.ajouter(mot)
    compteur+=1
print(compteur)

#creer_image_depuis_contenu("arbre", arbre.afficher())

print("Hauteur :", arbre.hauteur())
print("Nombre d'operation pour trouver avec ABR :", arbre.nb_operation_pour_trouver("abaissa"))
print("Nombre d'operation pour trouver dans la liste :", trouver_lineaire("abaissa"))

print(lire_mots())

#comparer mot avec self.value

import random
from affiche_dot import *

GAUCHE = 0
DROITE= 1

def lire_mots():
    with open("liste_mot.txt","r",encoding="utf-8") as fichier:
         mots=[]
         for i in range(1000):
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

    def est_vide(self):
        if self.fils[GAUCHE]==None and self.fils[DROITE]==None:
           return True
        else:
             return False

    def hauteur(self):
        if self.est_vide():
            return 0
        else:
            hauteur_gauche = self.fils[GAUCHE].hauteur() if self.fils[GAUCHE] else 0
            hauteur_droite = self.fils[DROITE].hauteur() if self.fils[DROITE] else 0
            return 1 + max(hauteur_gauche, hauteur_droite)

    def ajouter(self, mot):
        if self.value==None:
            self.value=mot
        else:
             if mot > self.value:
                if self.fils[DROITE]!=None:
                   self.fils[DROITE].ajouter(mot)
                else:
                     abr=ABR(mot)
                     self.fils[DROITE]=abr
             else:
                if self.fils[GAUCHE]!=None:
                   self.fils[GAUCHE].ajouter(mot)
                else:
                     abr=ABR(mot)
                     self.fils[GAUCHE]=abr


    def nb_operation_pour_trouver(self, mot):
        if self.value == mot:
            return 1

        cote = GAUCHE
        if mot > self.value:
            cote = DROITE

        if not self.fils[cote]:
            return None

        resultat = self.fils[cote].nb_operation_pour_trouver(mot)
        if resultat is not None:
            return 1 + resultat
        else:
            return None
        
        
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

creer_image_depuis_contenu("arbre", arbre.afficher())

print("Hauteur :", arbre.hauteur())
print("Nombre d'operation pour trouver avec ABR :", arbre.nb_operation_pour_trouver("abois"))
print("Nombre d'operation pour trouver dans la liste :", trouver_lineaire("abois"))
import os
import subprocess

DOSSIER_DOT = "dot"
DOSSIER_IMAGE = "output"

DOT_EXEC = os.path.join("Graphviz", "bin", "dot.exe")

def creer_dossier(nom_dossier):
    os.makedirs(nom_dossier, exist_ok=True) # a completer avec un appel a os.mkdirs

def creer_fichier_dot(nom_fichier, contenu_fichier):
    creer_dossier(DOSSIER_DOT)

    with open(os.path.join(DOSSIER_DOT, nom_fichier), "w",encoding="utf-8") as f:
        print("digraph { ", contenu_fichier, " }", file=f)

def creer_image(nom_image, nom_fichier_dot):
    creer_dossier(DOSSIER_IMAGE)
    cmd = [DOT_EXEC, "-Tpng", os.path.join(DOSSIER_DOT, nom_fichier_dot), "-o", os.path.join(DOSSIER_IMAGE, nom_image)]
    subprocess.call(cmd)

def creer_image_depuis_contenu(nom, contenu):
    creer_fichier_dot(nom+".dot", contenu)
    creer_image(nom+".png", nom+".dot")

if __name__ == "__main__":
    creer_fichier_dot("test.dot", "A->B;A->C;B->C")
    creer_image("test.png", "test.dot")

    creer_image_depuis_contenu("test2", "A->B;A->C;B->C")


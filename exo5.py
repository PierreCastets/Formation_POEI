'''
*** Exo 5: flags => flagsBis ***
Créer un programme qui produira un dossier flagsBis
Ce dossier contiendra tous les fichier png d'origine mais
renommés en ne conservant que les deux premières lettres.
Ces lettres seront en masjuscule.
ex: 
  exos/flags/allemagne.png => exos/flagsBis/AL.png
  exos/flags/belgique.png => exos/flagsBis/BE.png
Le fichier missing.png devra être ignoré
'''
print("*** EXO 5: flags => flagsBis ***")

import os, shutil
try:
    os.mkdir("flagsBis")
except:
    print("Le dossier 'flagsBis' existe déjà. Copie des fichiers dans ce dossier.")

flagsList = os.listdir("flags")

for file in flagsList:
    if not file.startswith('missing'):
        newName = file[:2].upper() + ".png"
        shutil.copy("flags/" + file, "flagsBis/" + newName)

print("Liste des fichiers dans 'flags': ",os.listdir("flags"))
print("Liste des fichiers dans 'flagsBis': ",os.listdir("flagsBis"))
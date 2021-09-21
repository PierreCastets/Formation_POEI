'''
*** Exo 2 ***
Ecrire un programme python qui propose à l'utilisateur
de deviner un nombre caché (exemple: 560) et
affichera en fonction de la réponse de l'utilisateur:
 - "c'est plus" si le nombre saisi est inférieur au nombre caché
 - "c'est moins" si le nombre saisi est supérieur au nombre caché
Tant que l'utilisateur n'a pas trouvé le nombre caché
on lui demande la saisie
'''
print("*** EXO 2: chiffre mystère à deviner --- version 2 --- ***")
guessNumber = 42

# Votre code ici

isFound = False

while not isFound:
    num = int(input("Entrez un nombre: "))
    if num > guessNumber:
        print("c'est moins")
    elif num < guessNumber:
        print("c'est plus")
    else:
        print("Bravo, tu as devnié !")
        isFound = True
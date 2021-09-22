'''
*** Exo 1 ***
Demander à l'utilisateur de saisir un chiffre
Si le chiffre saisi est supérieur à guess_number
on affiche "c'est moins"
Si le chiffre saisi est inférieur à guess_number
on affiche "c'est plus"
Si le chiffre saisi est égal à guess_number
on affiche "Bravo, tu as deviné !"
'''
print("*** EXO 1: chiffre mystère à deviner ***")
guess_number = 42

# votre code ici
try:
    num = int(input("Saisir un nombre: "))
except:
    print("L'entrée doit être un nombre!")
    exit()

if num > guess_number:
    print("c'est moins")
elif num < guess_number:
    print("c'est plus")
else:
    print("Bravo, tu as devnié !")

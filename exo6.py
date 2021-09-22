'''
*** Exo 6: Générateur de mot de passe ***
Créer un programme qui génère un mot de passe de longueur variable
en concaténant des caractères de façon aléatoire.
Le mot de passe devra contenir:
- au moins une majuscule
- au moins une minuscule
- au moins une valeur numérique
- au moins un caractère spécial (/;|%, etc.)
La longeur sera donnée par une saisie utilisateur
ex: longueur: 8 => Hn_y9l2%
'''
import string, random

print("*** EXO 6: Générateur de mot de passe ***")

length = 0
try:
    while length < 4:
        length = int(input("Entrez la taille du mot de passe (un nombre supérieur à 4): "))
except:
    print("L'entrée n'est pas valable")
    exit()

password = ""
alphabet_lower = list(string.ascii_lowercase)
alphabet_upper = list(string.ascii_uppercase)
specials = list(string.punctuation)
digits = list(string.digits)

password += random.choice(alphabet_lower)
password += random.choice(alphabet_upper)
password += random.choice(specials)
password += random.choice(digits)

allCaracters = alphabet_lower + alphabet_upper + specials + digits

for type in range(length-4):
    password += random.choice(allCaracters)

password_list = list(password)
random.shuffle(password_list)
password = ''.join(password_list)

print("Proposition de mot de passe:",password)
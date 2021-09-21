students = ["Afouda Pamela", "Castets Pierre", "Debals Alexandre", "Pelle Pierre-Jean"]

emails =[]
for p in students:
    nom = ""
    prenom = ""
    n = 0
    while p[n] != " ":
        nom += p[n]
        n+=1
    n += 1
    while n < len(p):
        prenom += p[n]
        n+=1
    email = prenom.lower() + "." + nom.lower() + "@python.com"
    emails.append(email)

#print(emails)

char = "*"
char = char*5
print(char)


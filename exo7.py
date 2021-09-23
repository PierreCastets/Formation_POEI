'''
*** EXO 7: CSV De Niro ***
Créer un programme qui, à partir du fichier deniro.csv,
produira en sortie un fichier deniro-report.txt" 
affichant les informations suivantes:

Nom du film le mieux noté
Nombre de films entre 2000 et 2010

'''
print("*** EXO 7: CSV De Niro ***")

countMovies = 0
bestMark = 0
bestMovie = ""

with open("deniro.csv", "r") as file:
    deniro = file.read().splitlines()
    for row in deniro[1:]:
        line = row.split(',')
        if int(line[1]) > bestMark:
            bestMark = int(line[1])
            bestMovie = line[2]
        if int(line[0]) <= 2010 and int(line[0]) >= 2000:
            countMovies += 1

final = open("deniro-report.txt", "w")
final.write("Le film le mieux noté de Deniro est: %s \n" % bestMovie)
final.write("Deniro a fait %s films entre 2000 et 2010 \n" % countMovies)
final.close()
    
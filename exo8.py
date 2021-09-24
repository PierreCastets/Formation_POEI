'''
*** EXO 8: Health Check ***
Créer un programme qui, à partir du fichier websites.txt
vérifie que chacun des sites listées répond
à raison d'une requête toutes les n secondes

la périodicité sera fournie en entrée par l'utilisateur

On produira en sortie un fichier de log "health.log" qui contiendra:
- la date de la requete
- l'url interrogée
- le status code obtenu ou une indication d'erreur en cas de non réponse
'''
print("*** EXO 8: Health Check ***")

# votre code ici
import time, datetime
import requests

startTime = time.time()
logFilePath = "health.log"

sleepTime = int(input("Entrez le temps en seconde entre deux requêtes: "))
maxTime = 30

with open("websites.txt", "r") as sites:
    websites = sites.read().splitlines()

while True:
    logFile = open(logFilePath, "a")
    for w in websites:
        newLogLine = ""
        newLogLine += str(datetime.datetime.now()) + " " + w + " "
        print(newLogLine)
        try:
            response = requests.get(w)
            newLogLine += str(response.status_code)
        except:
            newLogLine += "error when requesting the website"
        logFile.write(newLogLine + "\n")
    logFile.close()
    time.sleep(sleepTime)
    if time.time() - startTime > maxTime:
        break
    
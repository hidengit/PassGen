import os.path
import random
import string
import sys
from datetime import datetime
from tqdm import tqdm

# Lis les fichiers dans wordlist.txt et verifie si le 1 existe et 2 c'est pas obligatoire
if os.path.exists("wordlist.txt"):
    with open("wordlist.txt", "r") as files:
        mots = files.read().splitlines()
else:
    sys.exit("Error: wordist1.txt doesn't exist")

if os.path.exists("wordlist2.txt"):
    with open("wordlist2.txt", "r") as files:
        mots += files.read().splitlines()
else:
    print("Important : wordlist2.txt doesnt' exist")

if not mots:
    sys.exit("Error : Aucun mot trouvé dans les X fichiers flemme")

allwords = []

# nombre de mots a generer
number = int(input("Combien de variations voulez vous ? : "))

def verif_number():
    if number == 0:
        sys.exit("Error : Vous ne pouvez pas générer 0 mots")
    else:
        print(f"Vous allez generer {number} mots")

verif_number()

# barre de progression
with tqdm(total=number) as pbar:
    for _ in range(number):

        mot = random.choice(mots)

        #creer une variation du mot
        variation = mot

        # met une maj aleatoirement
        for _ in range(random.randint(0, 1)):
            variation = variation.capitalize()

        # + nombre et mots aleatoire
        for _ in range(random.randint(0, 2)):
            variation += random.choice(mots)

        # + année aleatoire (date recente pour naissance ou une date proche)
        variation += random.choice([str(random.randint(1900, 2023)), str(random.randint(0o1, 99))])

        # + caracteres speciaux
        for _ in range(random.randint(0, 2)):
            variation += random.choice(string.punctuation)

        allwords.append(variation)

        # met a jour la barre de progression
        pbar.update(1)

maintenant = datetime.now()
date_heure = maintenant.strftime("%Y-%m-%d_%H-%M-%S")

nom_fichier = f"results/result_{date_heure}.txt"

with open(nom_fichier, "w") as fichier:
    for variation in allwords:
        fichier.write(variation + "\n")

print(f"Variations générées et enregistrées dans le fichier '{nom_fichier}'.")

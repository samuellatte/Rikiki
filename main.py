# Script Python pour le calcul des points du jeu Rikiki.

from colorama import Fore
from colorama import Style

tour = 1
nombreJoueurs = int(input("Nombre de joueurs : "))
score = {}
annonce = {}
resultat = {}
continuer = True
descendre = "F"



def plisAnnonces():
    somme = 0
    count = 0
    tot = 0
    for nom in annonce: # On initialise le dictionnaire
            annonce[nom] = 0
    for nom in score:  # On itère sur chacun des noms
        if count == nombreJoueurs - 1:  # Vérifie que le nombre de plis est != du tour
            for cle in annonce:
                tot += annonce[cle]
            if tot <= tour:
                print(Fore.GREEN + Style.BRIGHT + f"{nom} ne peut pas dire : {tour - tot}" + Style.RESET_ALL)
            else:
                print(Fore.GREEN + Style.BRIGHT + f"{nom} peut annoncer ce qu'il/elle veut " + Style.RESET_ALL)
        annonce[nom] = int(input(f"{nom} annonce : "))
        count += 1
    for val in annonce.values():
        somme += val
    if somme == tour:
        print(Fore.RED + Style.BRIGHT + "Nombre de plis = nombre de cartes... Recommencer les annonces" + Style.RESET_ALL)
        plisAnnonces()


def plisRealises():
    for nom in resultat: # On initialise le dictionnaire
        resultat[nom] = 0
    for nom in score:
        resultat[nom] = int(input(f"{nom} a réalisé : "))


def calculPoints():
    for nom in score:
        if annonce[nom] == resultat[nom]:
            score[nom] += (10 + resultat[nom] * 5)
        else:
            score[nom] -= (5 + abs(resultat[nom] - annonce[nom]) * 5)
    print(sorted(score.items(), key=lambda t: t[1]))


if __name__ == '__main__':
    # Inititalisation de la partie
    for i in range(nombreJoueurs):
        score[str(input(f"Nom du joueur {i + 1}: "))] = 0

    # Déroulement de la partie
    while continuer:
        print(f'Tour : {tour}')

        plisAnnonces()
        reponse = str(input(Fore.BLUE + Style.BRIGHT + "Est-ce que l'encodage est correct ? (T/F) " + Style.RESET_ALL))
        if reponse == "F":
            plisAnnonces()

        print('-' * 50)

        plisRealises()
        reponse = str(input(Fore.BLUE + Style.BRIGHT + "Est-ce que l'encodage est correct ? (T/F) " + Style.RESET_ALL))
        if reponse == "F":
            plisRealises()

        calculPoints()

        # Réinitialisation
        if descendre == "F":
            monter = str(input(Fore.MAGENTA + Style.BRIGHT + "Voulez-vous continuer à monter ? (T/F) " + Style.RESET_ALL))
            if monter == "T":
                tour += 1
                for cle in score:
                    copieCle = cle
                    copieValeur = score[cle]
                    del score[cle]
                    break
                score.setdefault(copieCle, copieValeur)
                print(Fore.RED + Style.BRIGHT + "*" * 80 + Style.RESET_ALL)

        if monter == "F":
            tour -= 1
            if tour >= 1:
                descendre = str(input(Fore.MAGENTA + Style.BRIGHT + "Voulez-vous descendre ? (T/F) " + Style.RESET_ALL))
                if descendre == "T":
                    for cle in score:
                        copieCle = cle
                        copieValeur = score[cle]
                        del score[cle]
                        break
                    score.setdefault(copieCle, copieValeur)
                    print(Fore.RED + Style.BRIGHT + "*" * 80 + Style.RESET_ALL)
                else:
                    continuer = False
            else:
                continuer = False

# Fin de la partie
print(Fore.RED + Style.BRIGHT + "SCORE FINAL = " + Style.RESET_ALL,f"{sorted(score.items(), key=lambda t: t[1])}")

# Si on se met à descendre alors ne plus demander à monter à nouveau
import csv
from Article import *
from ListeChainee import *

fichier_csv = "recettes.csv"
achats = ListeChainee()

try:
    with open(fichier_csv, newline="") as f:
        lecteur = csv.reader(f)
        next(lecteur)  # sauter l'entête
        for ligne in lecteur:
            nom = ligne[0]
            prix = float(ligne[1])
            achats.inserer(Article(nom, prix))
    print("Données chargées.")
except FileNotFoundError:
    print("Aucun fichier trouvé, un nouveau sera créé.")

print("""=======================
     STORE MANAGER
=======================""")
print("Que voulez-vous faire ?")
while True:
    print("\t1 – Ajouter un achat d'article")
    print("\t2 – Afficher les finances du magasin")
    print("\t3 – Quitter")
    print('='*40) 
    choice = input("Répondez Ici!!!") # The rules says every name has to be self-explainatory, so you never know if i get -1 

    if choice == "1":
        nom = input("Nom de l'article : ")
        prix = float(input("Prix HT : "))
        article = Article(nom, prix)
        achats.inserer(article)
        print("-> Article ajouté !")

    elif choice == "2":
        total = 0
        courant = achats._ListeChainee__tete

        if courant is None:
            print("Aucun achat.")
        else:
            while courant is not None:
                a = courant.valeur
                print(a.get_nom(), ":", a.get_prix_hors_taxe(), "€")
                total += a.get_prix_hors_taxe()
                courant = courant.suivant
            print("TOTAL =", total, "€")

    elif choice == "3":
        with open(fichier_csv, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["nom", "prix"])
            courant = achats._ListeChainee__tete
            while courant is not None:
                a = courant.valeur
                writer.writerow([a.get_nom(), a.get_prix_hors_taxe()])
                courant = courant.suivant
        print("Données sauvegardées. GET OUTTTT !")
        break  # shitty thing... I HATE IT

    else:
        print("Choix invalide.")

import csv
from Article import *
from ListeChainee import *
from Depense import *

fichier_csv = "recettes.csv"
fichier_depenses = "depenses.csv"
achats = ListeChainee()
depenses = ListeChainee()

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
    print("Aucun fichier trouvé, un nouveau sera créé")

try:
    with open(fichier_depenses, newline="") as f:
        lecteur = csv.reader(f)
        next(lecteur)
        for ligne in lecteur:
            categorie = ligne[0]
            montant = float(ligne[1])
            depenses.inserer(Depense(categorie, montant))
    print("Dépenses chargées.")
except FileNotFoundError:
    print("Aucun fichier dépenses trouvé, un nouveau sera créé")

print("""=======================
     STORE MANAGER
=======================""")
print("Que voulez-vous faire ?")
while True:
    print("\t1 – Ajouter un achat d'article")
    print("\t2 – Ajouter une dépense")
    print("\t3 – Afficher les finances du magasin")
    print("\t4 – Quitter")
    print('='*40) 
    choice = input("Répondez Ici!!!") # The rules says every name has to be self-explainatory, so you never know if i get -1 

    if choice == "1":
        nom = input("Nom de l'article : ")
        prix = float(input("Prix HT : "))
        article = Article(nom, prix)
        achats.inserer(article)
        print("-> Article ajouté !")

    elif choice == "2":
        categorie = input("Catégorie : ")
        montant = float(input("Montant : "))
        depenses.inserer(Depense(categorie, montant))
        print("-> Dépense ajoutée !")

    elif choice == "3":
        total_recettes = 0
        courant = achats._ListeChainee__tete
        if courant is None:
            print("Aucun achat.")
        else:
            while courant is not None:
                a = courant.valeur
                print(a.get_nom(), ":", a.get_prix_hors_taxe(), "€")
                total_recettes += a.get_prix_hors_taxe()
                courant = courant.suivant
            print("TOTAL =", total_recettes, "€")
    
        total_depenses = 0
        courant = depenses._ListeChainee__tete
        if courant is None:
            print("Aucune dépense.")
        else:
            while courant is not None:
                d = courant.valeur
                print(d.get_categorie(), ":", d.get_montant(), "€")
                total_depenses += d.get_montant()
                courant = courant.suivant
            print("Dépenses =", total_depenses, "€")

        print("\n=== Bénéfice net ===")
        print("Bénéfice =", total_recettes - total_depenses, "€")

    elif choice == "4":
        with open(fichier_csv, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["nom", "prix"])
            courant = achats._ListeChainee__tete
            while courant is not None:
                a = courant.valeur
                writer.writerow([a.get_nom(), a.get_prix_hors_taxe()])
                courant = courant.suivant

        with open(fichier_depenses, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["categorie", "montant"])
            courant = depenses._ListeChainee__tete
            while courant is not None:
                d = courant.valeur
                writer.writerow([d.get_categorie(), d.get_montant()])
                courant = courant.suivant # Reminder : Passe au maillon suivant de la liste chaînée
        print("Données sauvegardées. GET OUTTTT !")
        break  # shitty thing... I HATE IT

    else:
        print("Choix invalide.")

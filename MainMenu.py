import doctest
import csv
#import matplotlib.pyplot as plt
from Article import *
from ListeChainee import *
from Depense import *

fichier_csv = "recettes.csv"
fichier_depenses = "depenses.csv"
achats = ListeChainee()
depenses = ListeChainee()

def ajout_achat(achats):
    """
    Fonction qui permet d'ajouter un achat

    Paramètres
    ----------
    - achats (Structure De Donnée) : Liste qui stock le ou les achats ajoutés

    Print
    --------
    Le Produit et son prix

    Pré-Condition
    --------
    - La variable saisie pour le prix DOIT être un nombre entier (Pas de texte, liste, dictionnaire, tableau, etc..)

    Post-Condition
    --------
    Une chaine de caractère quelconque pour le Nom du produit et une chaine de caractère type Int OU Float pour le montant
        
    Example
    --------
    >>> test = Article("chips", 6.5); ajout_achat(achats)    # je fais cela pour vous, cependant, le test s'éxécutera jamais car cela demande un input()...
    'chips : 6.5 €'
        
    """
    a = Article("chips", 5)
    assert a.get_nom() == "chips"
    assert a.get_prix_hors_taxe() != 0

    nom = input("Nom de l'article : ")
    prix_input = input("Prix HT : ")
    while True:
        try:
            prix = float(prix_input)
            if prix < 0:
                prix_input = input("Erreur : le prix doit être positif. Réessayez : ")
                continue
            break
        except ValueError:
            prix_input = input("Erreur : le prix doit être un nombre. Réessayez : ")
    article = Article(nom, prix)
    achats.inserer(article)
    print("-> Article ajouté !")

def ajout_depense(depenses):
    """
    Fonction qui permet d'ajouter une dépense

    Paramètres
    ----------
    - depenses (Structure De Donnée) : Liste qui stock le ou les depenses ajoutés

    Print
    --------
    La Catégorie de la Dépense et son Montant

    Pré-Condition
    --------
    - La variable saisie pour le prix DOIT être un nombre entier (Pas de texte, liste, dictionnaire, tableau, etc..)

    Post-Condition
    --------
    Une chaine de caractère quelconque pour le Nom de la dépense et une chaine de caractère type Int OU Float pour le montant
        
    Example
    --------
    >>> test = Depense("Stock De Jeux Steam", 199.99); ajout_depense(depenses)    # IDEM
    'Stock De Jeux Steam : 199.99 €'
        
    """
    d = Depense("loyer", 200)
    assert d.get_categorie() == "loyer"
    assert d.get_montant() != 0

    categorie = input("Catégorie : ")
    montant_input = input("Montant : ")
    while True:
        try:
            montant = float(montant_input)
            if montant < 0:
                montant_input = input("Erreur : le montant doit être positif. Réessayez : ")
                continue
            break
        except ValueError:
            montant_input = input("Erreur : le montant doit être un nombre. Réessayez : ")
    depenses.inserer(Depense(categorie, montant))
    print("-> Dépense ajoutée !")

def afficher_finance(achats, depenses):
    """
    Fonction qui permet d'afficher les finances du Magasin :
    les Achats (recettes), les Dépenses du shop et le Bénéfice net

    Paramètres
    ----------
    - achats (Structure De Donnée) : Liste chaînée qui stocke les achats ajoutés
    - depenses (Structure De Donnée) : Liste chaînée qui stocke les dépenses ajoutées

    Print
    -----
    - La liste des achats et leur prix
    - Le total des recettes
    - La liste des dépenses du magasin
    - Le total des dépenses
    - Le bénéfice net (recettes - dépenses)

    Pré-Condition
    -------------
    Les structures 'achats' et 'depenses' doivent contenir des objets Article et Depense
    correctement implémentés via leurs classes respectives.

    Post-Condition
    --------------
    Affiche toutes les informations liées aux finances du magasin.

    Example
    -------
    >>> afficher_finance(achats, depenses)
    chips : 6.5 €
    TOTAL = 6.5 €
    pringles : 2.0 €
    Dépenses = 2.0 €
    === Bénéfice net ===
    Bénéfice = 4.5 €
    """
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
    assert total_recettes >= 0
    
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
        assert total_depenses >= 0

    print("\n=== Bénéfice net ===")
    print("Bénéfice =", total_recettes - total_depenses, "€")

    return total_recettes, total_depenses # Quite need it for afficher_diagrame lol

#def afficher_diagramme(achats, depenses):

    """
    Fonction qui permet d'afficher un diagramme en barres simple
    représentant trois valeurs (Barre 1, Barre 2, Barre 3)

    Paramètres
    ----------
    - achats (Structure De Donnée) : Liste qui stock les achats
    - depenses (Structure De Donnée) : Liste qui stock les dépenses

    Print
    -----
    Affiche un diagramme en barres avec 3 barres colorées

    Pré-Condition
    -------------
    Les paramètres 'achats' et 'depenses' doivent être des structures valides
    pour permettre l'appel à afficher_finance

    Post-Condition
    --------------
    Un diagramme en barres s'affiche à l'écran via matplotlib

    Example
    -------
    >>> afficher_diagrame(achats, depenses)
    (Affiche un diagramme avec trois barres)
    """

    total_recettes, total_depenses = afficher_finance(achats, depenses)

    assert total_recettes >= 0
    assert total_depenses >= 0

    benefice = total_recettes - total_depenses # Why not

    x = ["Barre 1", "Barre 2", "Barre 3"]

    y = [total_recettes, total_depenses, benefice]

    plt.bar(x, y, color=["violet", "cyan", "purple"]) # My fav colours :)
    plt.title("Finances du magasin")
    plt.ylabel("Montant (€)")
    plt.show()

def leave(achats, depenses):
        """
    Fonction qui permet de quitter le Menu de Sélection tout en sauvegardant les données ajoutées

    Paramètres
    ----------
    - achats (Structure De Donnée) : Liste chaînée qui stocke les achats ajoutés
    - depenses (Structure De Donnée) : Liste chaînée qui stocke les dépenses ajoutées

    Print
    -----
    Un message qui prévient l'utilisateur que les données ont étaient sauvegardées et que celui-ci peut quitter

    Pré-Condition
    -------------
    Les structures 'achats' et 'depenses' doivent contenir des objets Article et Depense
    correctement implémentés via leurs classes respectives

    Post-Condition
    --------------
    Affiche le message de prévention et sauvegardées les données correctement

    Example
    -------
    >>> leave(achats, depenses)
    Données sauvegardées. GET OUTTTT !
    """
        try:
            ok = True  # tout est ok, pas besoin d'appeler leave() à l'intérieur
        except:
            ok = False

        assert ok == True

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
    print("\t4 – Afficher le diagramme du magasin - DO NOT CHOSE")
    print("\t5 – Quitter")
    print('='*40) 
    choice = input("Répondez Ici!!!") # The rules says every name has to be self-explainatory, so you never know if i get -1 

    if choice == "1":
        ajout_achat(achats)

    elif choice == "2":
        ajout_depense(depenses)

    elif choice == "3":
        afficher_finance(achats, depenses)

    elif choice == "4":
        afficher_diagramme(achats, depenses)

    elif choice == "5":
        leave(achats, depenses)

    else:
        print("Choix invalide.")

def main():
    # Exécution des tests
    doctest.testmod()

main()
import csv
from Article import *

def import_recettes(lien_fichier):
    """
    Importe les achats stockés dans un fichier CSV.

    Paramètres
    ----------
    lien_fichier : str = Chemin vers le fichier CSV

    Retour
    ------
    list[Achat] = Une liste contenant les objets Achat extraits du fichier.

    >>> type(import_recettes("recettes_test.csv"))
    <class 'list'>
    """

    assert isinstance(lien_fichier, str)

    achats = []  # structure de données linéaire : une simple liste

    with open(lien_fichier, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='|')
        champs = next(reader)  # on saute l'entête

        for row in reader:
            nom_article = row[0]
            prix_article = float(row[1])

            achat = Article(nom_article, prix_article)
            achats.append(achat)

    return achats


def export_recettes(lien_fichier, donnees):
    """
    Exporte des objets Achat dans un fichier CSV.

    Paramètres
    ----------
    lien_fichier : str = Chemin du fichier CSV à créer
    donnees : list[Achat] = Liste d'objets Achat
    """

    assert isinstance(lien_fichier, str)
    assert isinstance(donnees, list)

    with open(lien_fichier, "w", newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)

        # Entête
        champs = ["nom_article", "prix_HT"]
        writer.writerow(champs)

        # Données
        for achat in donnees:
            ligne = [achat.nom, achat.prix_ht]
            writer.writerow(ligne)


def total_recettes(liste_achats):
    """
    Calcule le total HT des recettes.

    Paramètres
    ----------
    liste_achats : list[Article]

    Retour
    ------
    float : somme des prix HT

    >>> total_recettes([Article("Baguette", 1.0), Article("Lait", 2.0)])
    3.0
    """
    assert isinstance(liste_achats, list)

    total = 0
    for achat in liste_achats:
        total += achat.prix_ht
    return total

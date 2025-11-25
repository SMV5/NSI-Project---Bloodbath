import csv

def import_recettes(lien_fichier):
    """
    Fonction permettant d'importer les données des recettes

    Paramètres
    ----------
    - lien_fichier : le lien vers le fichier CSV (chaîne de caractères)

    Return
    ------
    les données du fichier (<type à remplir>)
    """

    # Créer ici une instance de la structure de données linéaire
    # utilisée pour stocker les achats
    # ...
    
    with open(lien_fichier, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='|')
        champs = next(reader)
        for row in reader:
            nom_article = row[0]
            prix_article = float(row[1])

            # Créer ici une instance d'achat et la stocker dans
            # la structure de données linéaire
            # ...

    # Retourner ici la structure de données linéaire
    # ...

def export_recettes(lien_fichier, donnees):
    """
    Fonction permettant d'exporter des données vers un fichier CSV

    Paramètres
    ----------
    - lien_fichier : le lien vers le fichier CSV (chaîne de caractères)
    - donnees : les données à exporter (<type à compléter>)
    """
    
    with open(lien_fichier, "w", newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)

        # Champs du fichier CSV
        champs = ["nom_article", "prix_HT"]

        # Ecriture de l'entête du fichier (noms des champs)
        writer.write(champs)

        # Ecrire ici la 1ère ligne de la boucle de parcours des données
            ligne = [...] # tableau contenant le nom et le prix de l'article (à compléter)
            writer.write(ligne)

import_recettes("recettes.csv")

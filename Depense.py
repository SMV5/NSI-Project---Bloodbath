import doctest

class Depense:
    __categorie = ""
    __montant = 0.0

    def __init__(self, categorie, montant):
        """
        Méthode présente dans toutes les classes, qui sert à construire un objet Depense

        Paramètres
        ----------
        - self (instance) : Permet d’accéder aux attributs/méthodes propres de l'objet
        - categorie (str) : Catégorie de la dépense
        - montant (float) : Montant dépensé
        """
        self.__categorie = categorie
        self.__montant = montant


    def get_categorie(self):
        """Retourne la catégorie de la dépense.

        >>> h = Depense("loyer", 1200.0)
        >>> h.get_categorie()
        'loyer'
        """
        return self.__categorie

    def get_montant(self):
        """Retourne le montant de la dépense.

        >>> h = Depense("loyer", 1200.0)
        >>> h.get_montant()
        1200.0
        """
        return self.__montant

    def set_categorie(self, categorie):
        """Méthode publique qui permet de modifier la catégorie."""
        self.__categorie = categorie

    def set_montant(self, montant):
        """Méthode publique qui permet de modifier le montant.

        Pré-Condition
        --------
        - La variable saisie pour le prix DOIT être un nombre entier (Pas de texte, liste, dictionnaire, tableau, etc..)
        
        """
        assert self.__montant == int or self.__montant == float, "Le Montant doit être un nombre"
        assert self.__montant != 0, "Le Montant ne peut guère etre Gratuit.."
        assert self.__montant < 0, "Le Montant ne peut point etre négatif..."

        self.__montant = montant

def main():
    # Exécution des tests
    doctest.testmod()

main()
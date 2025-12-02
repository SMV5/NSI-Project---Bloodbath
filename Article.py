import doctest

class Article:
    __nom = ""
    __prix_hors_taxe = 0.0

    def __init__(self, nom, prix_hors_taxe):
        """
        méthode présente dans toutes les classes, qui sert à construire un objet. En L'occurenc le Nom et le Prix Hors Taxe

        Paramètres
        ----------
        - self (instance) : Permet d’accéder aux attributs/méthodes propres de l'objet.
        - nom (str) : le Nom de l'Objet
        - prix_hors_taxe (int) : le Prix Hors Taxe de l'Objet

        """
        self.__nom = nom
        self.__prix_hors_taxe = prix_hors_taxe
        
    def get_nom(self):
        """
        Méthode type Getters qui prend le Nom en compte

        Paramètres
        ----------
        - self (instance) : Permet d’accéder aux attributs/méthodes propres de l'objet.

        Retourne
        --------
        Le Nom de l'Objet

        Post-Condition
        --------
        Une chaine de caractère type Str (donc un Texte qui contient le Nom)
        
        Example
        --------
        >>> test = Article("chips", 6.5); test.get_nom()
        'chips'
        
        """
        return self.__nom

    def get_prix_hors_taxe(self):
        """
        Méthode type Getters qui prend le Prix Hors Taxe en compte

        Paramètres
        ----------
        - self (instance) : Permet d’accéder aux attributs/méthodes propres de l'objet.

        Retourne
        --------
        Le Prix Hors Taxe

        Post-Condition
        --------
        Une valeur type Int ou Float (donc un Résultat qui contient le Prix Hors Taxe)
        
        Example
        --------
        >>> test2 = Article("Geometry Dash", 2.99); test2.get_prix_hors_taxe()
        2.99
        
        """
        return self.__prix_hors_taxe
    
    def set_nom(self, nouveau_nom):
        """
        Méthode publique qui permet de modifier l'attribut privé de "Nom" depuis l'extérieur de la classe.

        Paramètres
        ----------
        - self (instance) : Permet d’accéder aux attributs/méthodes propres de l'objet.
        - nouveau_nom : Attribut qui sera modifié

        Retourne
        --------
        L'Attribut modifié 

        Post-Condition
        --------
        Une chaine de caractère type Str (donc un Texte qui contient le Nouveau Nom)
        
        """
        self.__nom = nouveau_nom

    def set_prix_hors_taxe(self, nouveau_prix):
        """
        Méthode publique qui permet de modifier l'attribut privé de "Prix_Hors_Taxe" depuis l'extérieur de la classe.

        Paramètres
        ----------
        - self (instance) : Permet d’accéder aux attributs/méthodes propres de l'objet.
        - nouveau_prix : Attribut qui sera modifié

        Retourne
        --------
        L'Attribut modifié 

        Pré-Condition
        --------
        - La variable saisie pour le prix DOIT être un nombre entier (Pas de texte, liste, dictionnaire, tableau, etc..)

        Post-Condition
        --------
        Une valeur de type Int (donc une Valeur qui contient le Nouveau Prix)
        
        """
        assert self.__prix_hors_taxe == int or self.__prix_hors_taxe == float, "Le Prix doit être un nombre"
        assert self.__prix_hors_taxe != 0, "L'Article ne peut guère etre Gratuit.."
        assert self.__prix_hors_taxe < 0, "L'Article ne peut point etre négatif..."

        self.__prix_hors_taxe = nouveau_prix

def main():
    # Exécution des tests
    doctest.testmod()

main()
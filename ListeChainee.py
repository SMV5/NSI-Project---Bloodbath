class MaillonFaible:
    valeur = 0.0
    suivant = None

    def __init__(self, valeur):
        self.valeur = valeur


class ListeChainee:
    def __init__(self):
        self.__tete = None

    def est_vide(self):
        return self.__tete == None

    def inserer(self, element):
        if self.__tete == None:
            self.__tete = MaillonFaible(element)
        else:
            maillon = MaillonFaible(element)
            maillon.suivant = self.__tete
            self.__tete = maillon

    def tete(self):
        if self.est_vide():
            return None
        else:
            return self.__tete.valeur

    def queue(self):
        if self.est_vide():
            return ListeChainee()
        else:
            nouvelle_liste = ListeChainee()
            nouvelle_liste.__tete = self.__tete.suivant
            return nouvelle_liste

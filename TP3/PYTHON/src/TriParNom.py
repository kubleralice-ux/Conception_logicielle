from ITriStrategy import ITriStrategy

class TriParNom(ITriStrategy):
    def trier(self, liste_etudiants):
        return sorted(liste_etudiants, key=lambda e: e.nom)
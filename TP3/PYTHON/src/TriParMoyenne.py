from src.ITriStrategy import ITriStrategy

class TriParMoyenne(ITriStrategy):
    def trier(self, liste_etudiants):
        return sorted(liste_etudiants, key=lambda e: e.moyenne, reverse=True)
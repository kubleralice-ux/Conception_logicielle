from src.pattern.Decorator.EtudiantDecorator import EtudiantDecorator

class EtudiantBoursier(EtudiantDecorator):
    def afficher_statut(self):
        nom = self._etudiant.get_nom()
        return f"{nom} est un étudiant boursier, il est exonéré de frais."
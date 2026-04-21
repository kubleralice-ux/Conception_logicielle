from src.EtudiantDecorator import EtudiantDecorator

class EtudiantBoursier(EtudiantDecorator):
    def afficher_statut(self):
        return f"{self.nom} est un étudiant boursier, il est exonéré de frais."
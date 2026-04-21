from src.EtudiantDecorator import EtudiantDecorator

class EtudiantDelegue(EtudiantDecorator):
    def organiser_reunion(self):
        return f"{self.nom}, le délégué de la classe, organise une réunion de classe."

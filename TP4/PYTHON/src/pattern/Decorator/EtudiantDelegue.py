from src.pattern.Decorator.EtudiantDecorator import EtudiantDecorator

class EtudiantDelegue(EtudiantDecorator):
    def organiser_reunion(self):
        nom = self._etudiant.get_nom()
        return f"{nom}, le délégué de la classe, organise une réunion de classe."

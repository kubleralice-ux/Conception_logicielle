from src.codes_initiaux.etudiant import Etudiant

class EtudiantDecorator(Etudiant): 
    def __init__(self, etudiant_objet):
        self._etudiant = etudiant_objet

    def get_nom(self):
        return self._etudiant.get_nom()

    def get_age(self):
        return self._etudiant.get_age()

    def afficher_details(self):
        return self._etudiant.afficher_details()
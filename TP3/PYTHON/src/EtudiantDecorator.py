from src.etudiant import Etudiant

class EtudiantDecorator(Etudiant): 
    def __init__(self, etudiant_objet):
        self._etudiant = etudiant_objet

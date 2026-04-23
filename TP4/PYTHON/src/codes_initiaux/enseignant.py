from src.codes_initiaux.personne import Personne

class Enseignant(Personne):
    def __init__(self, nom, age, salaire):
        super().__init__(nom, age)
        self.salaire = salaire

    def afficher_details(self):
        return f"Enseignant: {self.get_nom()}, Age: {self.get_age()}, Salaire: {self.salaire}"
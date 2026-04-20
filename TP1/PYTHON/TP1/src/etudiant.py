from src.personne import Personne

class Etudiant(Personne):
    def __init__(self, nom, age, numero_etudiant, moyenne, cours):
        super().__init__(nom, age)
        self.numero_etudiant = numero_etudiant
        self.moyenne = moyenne
        self.cours = cours


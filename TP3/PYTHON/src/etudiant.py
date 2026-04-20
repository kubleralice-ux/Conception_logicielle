from src.personne import Personne

class Etudiant(Personne):
    def __init__(self, nom, age, numero_etudiant, moyenne, cours):
        super().__init__(nom, age)
        self.numero_etudiant = numero_etudiant
        self.__moyenne = moyenne
        self.cours = cours
    
    def get_moyenne(self):
        return self.__moyenne
    
    def set_moyenne(self, moyenne):
        if moyenne < 0 or moyenne > 20:
            raise ValueError("Moyenne invalide")
        self.__moyenne = moyenne
    
    def afficher_details(self):
        return f"Etudiant: {self.get_nom()}, Age: {self.get_age()}, Moyenne: {self.get_moyenne()}"

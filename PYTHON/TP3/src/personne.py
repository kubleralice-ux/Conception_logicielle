class Personne:
    def __init__(self, nom, age):
        self.__nom = nom
        self.__age = age

    def get_nom(self):
        return self.__nom

    def get_age(self):
        return self.__age

    def set_age(self, age):
        if age < 0 or age > 100:
            raise ValueError("Âge invalide")
        self.__age = age
        
    def afficher_details(self):
        return f"Nom: {self.get_nom()}, Age: {self.get_age()}"
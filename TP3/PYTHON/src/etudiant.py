from src.personne import Personne

class Etudiant(Personne):
    def __init__(self, nom, age, numero_etudiant, cours):
        super().__init__(nom, age)
        self.numero_etudiant = numero_etudiant
        self.__moyenne = 0
        self.cours = cours
        self.notes = []
        self._observers = []
    
    def abonner(self, observateur):
        self._observers.append(observateur)

    def ajouter_note(self, note):
        if 0 <= note <= 20:
            self.notes.append(note)
            self.__moyenne = sum(self.notes) / len(self.notes)
            self.notifier()
        else:
            raise ValueError("La note doit être entre 0 et 20")

    def get_moyenne(self):
        return self.__moyenne
    
    def notifier(self):
        for obs in self._observers:
            obs.update(self)
    
    def afficher_details(self):
        return f"Etudiant: {self.get_nom()}, Age: {self.get_age()}, Moyenne: {self.get_moyenne()}"

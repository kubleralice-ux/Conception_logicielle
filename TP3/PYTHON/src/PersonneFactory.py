from src.etudiant import Etudiant
from src.enseignant import Enseignant

class PersonneFactory:
    @staticmethod
    def creer_personne(type_personne, nom, age, infos = None):
        #infos est une liste 
        if type_personne.lower() == "etudiant":
            numero_etudiant, cours = infos[0], infos[1]
            return Etudiant(nom, age, numero_etudiant, cours)
        
        elif type_personne.lower() == "enseignant":
            salaire = infos[0]
            return Enseignant(nom, age, salaire)
            
        else:
            raise ValueError("Type de personne inconnu")
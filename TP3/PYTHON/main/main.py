from src.personne import Personne
from src.etudiant import Etudiant
from src.cours import Cours
from src.enseignant import Enseignant

if __name__ == "__main__":  
    # commande pour lancer le code
    # se placer dans Python/TP3 et faire : python -m main.main
    personnes = []

    etudiant1 = Etudiant("Bob", 22, "E123", 15.5, [])
    enseignant1 = Enseignant("Dupont", 40, 3000)

    personnes.append(etudiant1)
    personnes.append(enseignant1)

    for p in personnes:
        print(p.afficher_details())
    


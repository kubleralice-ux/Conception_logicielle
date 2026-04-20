from src.personne import Personne
from src.etudiant import Etudiant
from src.cours import Cours

if __name__ == "__main__":  
    # commande pour lancer le code
    # se placer dans Python/TP1 et faire : python -m main.main

    personne1 = Personne("Alice", 20)
    print(f"Personne: {personne1.nom}, Age: {personne1.age}")
    cours1 = Cours("Mathématiques", "M.Dupond")
    cours2 = Cours("Français", "M.Leroy")
    cours = [cours1, cours2]
    etudiant1 = Etudiant("Bob", 22, "E12345", 15.5, cours)
    print(f"Etudiant: {etudiant1.nom}, Age: {etudiant1.age}, Numéro: {etudiant1.numero_etudiant}, Moyenne: {etudiant1.moyenne}")
    print("Cours suivis:")  
    for cours in etudiant1.cours:
        print(f"- {cours.nom} par {cours.professeur}")
    


from src.personne import Personne
from src.etudiant import Etudiant
from src.cours import Cours
from src.enseignant import Enseignant

#TP 3
from src.ScolariteManager import ScolariteManager
from src.PersonneFactory import PersonneFactory
from src.CoursAdapter import CoursAdapter
from src.EtudiantBoursier import EtudiantBoursier
from src.EtudiantDelegue import EtudiantDelegue
from src.EtudiantDecorator import EtudiantDecorator
from src.LegacyCours import LegacyCours
from src.PersonneFactory import PersonneFactory
from src.TriParMoyenne import TriParMoyenne
from src.TriParNom import TriParNom

def main():

    manager = ScolariteManager()

    vieux_systeme = LegacyCours()
    adaptateur = CoursAdapter(vieux_systeme)
    cours_python = adaptateur.recuperer_cours() 
    print(f"Cours chargé via Adapter : {cours_python.nom} ({cours_python.prof})")

    alice = PersonneFactory.creer_personne("etudiant", "Alice", 20, "E001")
    bob = PersonneFactory.creer_personne("etudiant", "Bob", 21, "E002")
    prof = PersonneFactory.creer_personne("professeur", "M. Durand", 45, "Informatique")

    manager.ajouter_etudiant(alice)
    manager.ajouter_etudiant(bob)

    print("Saisie de notes")
    alice.ajouter_note(18)
    bob.ajouter_note(12)
    alice.ajouter_note(14)

    print("Statuts spéciaux")
    alice_boursiere = EtudiantBoursier(alice)
    bob_delegue = EtudiantDelegue(bob)
    
    print(alice_boursiere.afficher_statut())
    print(bob_delegue.organiser_reunion())

    print("Tri des étudiants")
    
    print("Tri par Nom :")
    manager.set_strategie(TriParNom())
    manager.afficher_classement()

    print("Tri par Moyenne :")
    manager.set_strategie(TriParMoyenne())
    manager.afficher_classement()

if __name__ == "__main__":
    main()


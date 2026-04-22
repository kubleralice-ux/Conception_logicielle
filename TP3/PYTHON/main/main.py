from src.codes_initiaux.personne import Personne
from src.codes_initiaux.etudiant import Etudiant
from src.codes_initiaux.cours import Cours
from src.codes_initiaux.enseignant import Enseignant

#TP 3
from src.pattern.Singleton.ScolariteManager import ScolariteManager
from src.pattern.Factory.PersonneFactory import PersonneFactory
from src.pattern.Adapter.CoursAdapter import CoursAdapter
from src.pattern.Decorator.EtudiantBoursier import EtudiantBoursier
from src.pattern.Decorator.EtudiantDelegue import EtudiantDelegue
from src.pattern.Decorator.EtudiantDecorator import EtudiantDecorator
from src.pattern.Adapter.LegacyCours import LegacyCoursSystem
from src.pattern.Factory.PersonneFactory import PersonneFactory
from src.pattern.Strategy.TriParMoyenne import TriParMoyenne
from src.pattern.Strategy.TriParNom import TriParNom

def main():
    # 1. Singleton
    print("1. Pattern Singleton")
    print("Gestion de la scolarité avec Singleton")
    manager = ScolariteManager()

    # 2. Factory Method
    print("\n2. Pattern Factory Method")
    alice = PersonneFactory.creer_personne("etudiant", "Alice", 20, "E001")
    bob = PersonneFactory.creer_personne("etudiant", "Bob", 21, "E002")
    prof = PersonneFactory.creer_personne("enseignant", "M. Durand", 45, [4000])
    print(f"Étudiant créé : {alice.get_nom()}, ID: {alice.numero_etudiant}")
    print(f"Enseignant créé : {prof.get_nom()}, Salaire: {prof.salaire}€")
    
    # 3. Adapter
    print("\n3. Pattern Adapter")
    vieux_systeme = LegacyCoursSystem()
    adaptateur = CoursAdapter(vieux_systeme)
    cours_python = adaptateur.recuperer_cours() 
    print(f"Cours chargé via Adapter : {cours_python.nom} ({cours_python.professeur})")

    # 4. Décorateur
    print("\n4. Pattern Décorateur")
    print("Statuts spéciaux")
    alice_boursiere = EtudiantBoursier(alice)
    bob_delegue = EtudiantDelegue(bob)
    print(alice_boursiere.afficher_statut())
    print(bob_delegue.organiser_reunion())

    # Encore 1. Manager pour gérer les étudiants
    manager.ajouter_etudiant(alice)
    manager.ajouter_etudiant(bob)

    # 5. Strategy
    print("\n5. Pattern Strategy")
    print("Tri des étudiants")
    print("\nTri par Nom :")
    manager.set_strategie(TriParNom())
    manager.afficher_classement()

    print("\nTri par Moyenne :")
    manager.set_strategie(TriParMoyenne())
    manager.afficher_classement()

    # 6. Observer
    print("\n6. Pattern Observer")
    print("Saisie de notes")
    alice.ajouter_note(18)
    bob.ajouter_note(12)
    alice.ajouter_note(14) # Nouvelle moyenne : 16

    # Encore 5
    print("\nTri par Moyenne après saisie des notes :")
    manager.set_strategie(TriParMoyenne())
    manager.afficher_classement()


if __name__ == "__main__":
    main()


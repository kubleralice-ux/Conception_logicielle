from src.codes_initiaux.etudiant import Etudiant
from src.pattern.Decorator.EtudiantBoursier import EtudiantBoursier
from src.pattern.Decorator.EtudiantDelegue import EtudiantDelegue

def test_etudiant_boursier_decorator():
    alice = Etudiant("Alice", 20, "E001", "Python")
    boursiere = EtudiantBoursier(alice)
    assert boursiere.get_nom() == "Alice"
    status = boursiere.afficher_statut()
    assert "boursier" in status.lower()
    assert "exonéré" in status.lower()

def test_etudiant_delegue_decorator():
    bob = Etudiant("Bob", 21, "E002", "Python")
    delegue = EtudiantDelegue(bob)
    
    assert delegue.get_nom() == "Bob"
    action = delegue.organiser_reunion()
    assert "réunion" in action.lower()
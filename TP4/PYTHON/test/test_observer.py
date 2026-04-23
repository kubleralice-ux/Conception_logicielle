from src.codes_initiaux.etudiant import Etudiant
from src.pattern.Singleton.ScolariteManager import ScolariteManager

def test_observer_notification():
    manager = ScolariteManager()
    
    alice = Etudiant("Alice", 20, "E001", "Python")
    manager.ajouter_etudiant(alice)
    
    alice.ajouter_note(15)
    
    assert len(alice.notes) == 1
    assert alice.get_moyenne() == 15.0
    assert manager in alice._observers
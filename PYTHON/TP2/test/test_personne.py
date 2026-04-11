from src.personne import Personne

def test_creation_personne():
    personne = Personne("Alice", 20)
    assert personne.get_nom() == "Alice"
    assert personne.get_age() == 20
from src.personne import Personne

def test_creation_personne():
    personne = Personne("Alice", 20)
    assert personne.nom == "Alice"
from src.cours import Cours

def test_creation_cours():
    cours = Cours("Mathématiques", "M.Dupond")
    assert cours.nom == "Mathématiques"
    assert cours.professeur == "M.Dupond"
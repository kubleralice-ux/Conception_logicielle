from src.etudiant import Etudiant
from src.cours import Cours

def test_creation_etudiant():
    maths = Cours("Mathématiques", "M.Dupond")
    français = Cours("Français", "M.Leroy")
    cours = [maths, français]
    etudiant = Etudiant("Bob", 22, "E12345", 15.5, cours)
    assert etudiant.get_nom() == "Bob"
    assert etudiant.get_age() == 22
    assert etudiant.numero_etudiant == "E12345"
    assert etudiant.get_moyenne() == 15.5
    assert etudiant.cours == cours

def test_afficher_details_etudiant():
    e = Etudiant("Bob", 22, "E123", 15.5, [])
    result = e.afficher_details()
    assert "Bob" in result
    assert "15.5" in result
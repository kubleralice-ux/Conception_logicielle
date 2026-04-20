from src.enseignant import Enseignant

def test_afficher_details_enseignant():
    ens = Enseignant("Dupont", 40, 3000)
    result = ens.afficher_details()
    assert "Dupont" in result
    assert "3000" in result
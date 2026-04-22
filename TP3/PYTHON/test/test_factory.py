from src.codes_initiaux.enseignant import Enseignant
from src.pattern.Factory.PersonneFactory import PersonneFactory

def test_personne_factory():
    prof = PersonneFactory.creer_personne("enseignant", "Durand", 45, [4000])
    assert isinstance(prof, Enseignant)
    assert prof.get_nom() == "Durand"
    eleve = PersonneFactory.creer_personne("etudiant", "Alice", 20, ["E001", ["Python"]])
    assert eleve.get_nom() == "Alice"
    assert eleve.get_age() == 20
    assert eleve.numero_etudiant == "E001"
    assert eleve.cours == ["Python"]

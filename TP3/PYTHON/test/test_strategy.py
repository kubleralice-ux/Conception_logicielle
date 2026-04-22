from src.codes_initiaux.etudiant import Etudiant
from src.pattern.Strategy.TriParNom import TriParNom
from src.pattern.Strategy.TriParMoyenne import TriParMoyenne
from src.codes_initiaux.cours import Cours

def test_tri_par_nom():
    c1 = Cours("Mathématiques", "M.Dupond")
    e1 = Etudiant("Zoe", 20, "E001", [c1])
    e2 = Etudiant("Alice", 22, "E002", [c1])
    
    tri = TriParNom()
    resultat = tri.trier([e1, e2])
    
    assert resultat[0].get_nom() == "Alice"
    assert resultat[1].get_nom() == "Zoe"

def test_tri_par_moyenne():
    c1 = Cours("Mathématiques", "M.Dupond")
    e1 = Etudiant("Bob", 20, "E001", [c1])
    e2 = Etudiant("Alice", 22, "E002", [c1])
    e1.ajouter_note(10) # Moyenne 10
    e2.ajouter_note(20) # Moyenne 20
    
    tri = TriParMoyenne()
    resultat = tri.trier([e1, e2])
    
    assert resultat[0].get_moyenne() == 20.0
    assert resultat[0].get_nom() == "Alice"
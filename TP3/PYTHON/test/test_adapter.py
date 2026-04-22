from src.pattern.Adapter.CoursAdapter import CoursAdapter
from src.pattern.Adapter.LegacyCours import LegacyCoursSystem

def test_adapter():
    # LegacyCours renvoie "Mathematiques;M. Durand"
    legacy = LegacyCoursSystem()
    adapter = CoursAdapter(legacy)
    cours = adapter.recuperer_cours()
    
    assert cours.nom == "Mathematiques"
    assert cours.professeur == "M. Durand"

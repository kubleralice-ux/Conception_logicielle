from src.pattern.Singleton.ScolariteManager import ScolariteManager

def test_singleton_instance():
    """Vérifie que le manager est bien un Singleton."""
    s1 = ScolariteManager()
    s2 = ScolariteManager()
    assert s1 is s2, "ScolariteManager devrait être une instance unique"
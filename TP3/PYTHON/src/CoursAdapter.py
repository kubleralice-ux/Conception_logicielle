from src.LegacyCours import LegacyCoursSystem
from src.ICoursProvider import ICoursProvider
from src.cours import Cours

class CoursAdapter(ICoursProvider):
    def __init__(self, legacy_system):
        self._legacy = legacy_system

    def recuperer_cours(self):
        donnees_brutes = self._legacy.obtenir_donnees_brutes()
        nom_cours, nom_prof = donnees_brutes.split(";")

        return Cours(nom_cours, nom_prof)
from abc import ABC, abstractmethod

class ITriStrategy(ABC):
    @abstractmethod
    def trier(self, liste_etudiants):
        pass
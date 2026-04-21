from abc import ABC, abstractmethod

class ICoursProvider(ABC):
    @abstractmethod
    def recuperer_cours(self):
        pass
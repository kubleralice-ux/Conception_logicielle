from src.codes_initiaux.etudiant import Etudiant


class ScolariteManager:
    _instance = None

    def __new__(cls):
        if cls._instance is None :
            cls._instance = super().__new__(cls)
            cls._instance.liste_etudiants = []
        return cls._instance
    
    def ajouter_etudiant(self, etudiant):
        self.liste_etudiants.append(etudiant)
        etudiant.abonner(self)

    def update(self, etudiant):
        print(f"[NOTIFICATION MANAGER] Note reçue pour {etudiant.get_nom()}. "
              f"Calcul de la nouvelle moyenne globale : {etudiant.get_moyenne()}")
        
    def set_strategie(self, strategie):
        self._strategie = strategie

    def afficher_classement(self):
        if self._strategie is None:
            print("Aucune stratégie de tri sélectionnée")
            return
        
        liste_triee = self._strategie.trier(self.liste_etudiants)
        
        print("Tri des étudiants :")
        for e in liste_triee:
            print(e.afficher_details())
from TP3.PYTHON.src import etudiant


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
        print(f"[NOTIF MANAGER] Note reçue pour {etudiant.get_nom()}. "
              f"Nouvelle moyenne globale : {etudiant.get_moyenne()}")
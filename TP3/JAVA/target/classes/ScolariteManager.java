package main.resources;

import java.util.Arrays;
import java.util.List;

import src.Etudiant;

public class ScolariteManager {
    private List<Etudiant> liste_Etudiants = new List<Etudiant>() {};

    private ConfigScolariteManager() {}

    private ITriStrategy strategie;

    public static ConfigScolariteManager getInstance() {
        if (instance == null) {
            instance = new ConfigScolariteManager();
        }
        return instance;
    }

    public double getListeEtudiants() {
        return liste_Etudiants; 
    }

    public void ajouterEtudiant(Etudiant nouvel_etudiant) {
        this.liste_Etudiants.add(nouvel_etudiant);
        nouvel_etudiant.abonner(this);
    }
    
    public void setStrategy(ITriStrategy nouvelle_strategie) {
        this.strategie = nouvelle_strategie;
    }

    public void afficherClassement() {
        if(this.strategie instanceof None){
            System.out.println("Aucune stratégie de tri sélectionnée !");
        }

        List<Etudiant> listeTriee = this.strategie.trier(this.liste_Etudiants);

        System.out.println(Arrays.toString(list.toArray()));
    }

    public void update(Etudiant etudiant) {
        System.out.print("[NOTIF MANAGER] Note reçue pour : ");
        System.out.println(etudiant.get_nom());
        System.out.print("Nouvelle moyenne globale : ");
        System.out.println(etudiant.get_moyenne());
    }
}


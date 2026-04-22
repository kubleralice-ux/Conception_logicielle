package main.resources;

import java.util.List;

import src.Cours;
import src.Etudiant;

public class EtudiantBoursier extends Etudiant {
    
    public EtudiantBoursier(String nom, int age, String numeroEtudiant, double moyenne, List<Cours> cours) {
        super(nom, age, numeroEtudiant, moyenne, cours);
    }

    @Override
    public void afficherDetails() {
        System.out.println("Etudiant: " + getNom()
                + ", Age: " + getAge()
                + ", Moyenne: " + this.getMoyenne()
                + ", Cet etudiant est boursier.");
    }
}

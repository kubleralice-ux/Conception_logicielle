package src;
import src.Personne;
import src.Cours;

import java.util.List;

public class Etudiant extends Personne {

    private String numeroEtudiant;
    private double moyenne;
    private List<Cours> cours;

    public Etudiant(String nom, int age, String numeroEtudiant, double moyenne, List<Cours> cours) {
        super(nom, age);
        this.numeroEtudiant = numeroEtudiant;
        this.moyenne = moyenne;
        this.cours = cours;
    }

    public String getNumeroEtudiant() {
        return numeroEtudiant;
    }

    public double getMoyenne() {
        return moyenne;
    }

    public List<Cours> getCours() {
        return cours;
    }

    @Override
    public void afficherDetails() {
        System.out.println("Etudiant: " + getNom()
                + ", Age: " + getAge()
                + ", Moyenne: " + moyenne);
    }
}
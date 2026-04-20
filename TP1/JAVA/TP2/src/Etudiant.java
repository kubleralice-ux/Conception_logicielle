package src;

import java.util.ArrayList;
import java.util.List;

public class Etudiant extends Personne {

    private int numeroEtudiant;
    private double moyenne;
    private List<Cours> cours;

    public Etudiant(String nom, int age, int numeroEtudiant, double moyenne) {
        super(nom, age);
        this.numeroEtudiant = numeroEtudiant;
        setMoyenne(moyenne);
        this.cours = new ArrayList<>();
    }

    public int getNumeroEtudiant() {
        return numeroEtudiant;
    }

    public double getMoyenne() {
        return moyenne;
    }

    public void setMoyenne(double moyenne) {
        if (moyenne < 0 || moyenne > 20) {
            throw new IllegalArgumentException("Moyenne invalide");
        }
        this.moyenne = moyenne;
    }

    public List<Cours> getCours() {
        return cours;
    }

    public void ajouterCours(Cours c) {
        cours.add(c);
    }
}
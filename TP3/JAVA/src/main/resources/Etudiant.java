package src;
import src.Personne;
import src.Cours;

import java.util.List;

import main.resources.ScolariteManager;

public class Etudiant extends Personne {

    private String numeroEtudiant;
    private List<Float> notes;
    private double moyenne = 0;
    private List<Cours> cours;
    private ScolariteManager observateur;

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

    public void ajouterNote(Float note) {
        int sup = Float.compare(note, 0.0f);
        int sub = Float.compare(20.0f, note);
        if(sup > 0 && sub > 0) {
            this.notes.add(note);
            this.moyenne = (this.moyenne + note)/2;
        } else {
            System.out.println("La note doit être entre 0 et 20");
        }
    }

    public void abonner(ScolariteManager nouvel_observateur) {
        this.observateur = nouvel_observateur;
    }

    public void notifier() {
        this.observateur.update(this);
    }
}
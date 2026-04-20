package src;
import java.util.ArrayList;
import java.util.List;

public class Etudiant extends Personne {
    public String numeroEtudiant;
    public double moyenne;
    public List<Cours> listeCours;

    public Etudiant(String nom, int age, String numeroEtudiant, double moyenne) {
        super(nom, age);
        this.numeroEtudiant = numeroEtudiant;
        this.moyenne = moyenne;
        this.listeCours = new ArrayList<>();
    }

    public void ajouterCours(Cours cours) {
        this.listeCours.add(cours);
    }
}
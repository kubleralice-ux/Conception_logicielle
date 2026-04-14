package src;

public class Cours {
    public String nomCours;
    public String professeur;

    public Cours(String nomCours, String professeur) {
        this.nomCours = nomCours;
        this.professeur = professeur;
    }

    public String getNom() { return nomCours; }
}
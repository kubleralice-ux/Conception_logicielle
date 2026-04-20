package main;
import src.Cours;
import src.Etudiant;
import src.Personne;

public class Main {

    public static void main(String[] args) {

        Personne personne1 = new Personne("Alice", 20);
        System.out.println("Personne: " + personne1.getNom() + ", Age: " + personne1.getAge());

        Cours cours1 = new Cours("Mathématiques", "M.Dupond");
        Cours cours2 = new Cours("Français", "M.Leroy");

        Etudiant etudiant1 = new Etudiant("Bob", 22, 12345, 15.5);

        etudiant1.ajouterCours(cours1);
        etudiant1.ajouterCours(cours2);

        System.out.println("Etudiant: " + etudiant1.getNom()
                + ", Age: " + etudiant1.getAge()
                + ", Numéro: " + etudiant1.getNumeroEtudiant()
                + ", Moyenne: " + etudiant1.getMoyenne());

        System.out.println("Cours suivis:");
        for (Cours c : etudiant1.getCours()) {
            System.out.println("- " + c.getNomCours() + " par " + c.getProfesseur());
        }

        System.out.println("Moyenne actuelle : " + etudiant1.getMoyenne());

        try {
            etudiant1.setMoyenne(25);
        } catch (IllegalArgumentException erreur) {
            System.out.println("Erreur détectée : " + erreur.getMessage());
        }

        System.out.println("Moyenne après tentative : " + etudiant1.getMoyenne());
    }
}
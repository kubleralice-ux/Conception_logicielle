package main;
import src.*;

import java.util.ArrayList;
import java.util.List;

public class Main {

    public static void main(String[] args) {

        List<Personne> personnes = new ArrayList<>();

        Etudiant etudiant1 = new Etudiant("Bob", 22, "E123", 15.5, new ArrayList<>());
        Enseignant enseignant1 = new Enseignant("Dupont", 40, 3000);

        personnes.add(etudiant1);
        personnes.add(enseignant1);

        for (Personne p : personnes) {
            p.afficherDetails();
        }
    }
}
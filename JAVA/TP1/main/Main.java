package main;
import src.*;
// Pour lancer le code : javac -d . src/*.java main/*.java
// puis : java main.Main

public class Main {
    public static void main(String[] args) {
        Etudiant etu = new Etudiant("Jean Dupont", 22, "E2026-001", 14.5);
        
        Cours java = new Cours("Programmation Java", "M. Martin");
        etu.ajouterCours(java);

        System.out.println("Étudiant: " + etu.nom + " (ID: " + etu.numeroEtudiant + ")");
        System.out.println("Âge: " + etu.age + " ans");
        System.out.println("Moyenne: " + etu.moyenne);
        System.out.println("Cours suivis:");
        for (Cours c : etu.listeCours) {
            System.out.println("- " + c.nomCours + " (Prof: " + c.professeur + ")");
        }
    }
}
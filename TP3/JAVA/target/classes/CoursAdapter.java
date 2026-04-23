package main.resources;

import java.util.List;

import src.Cours;

public class CoursAdapter{
    private Cours legacy = new Cours();

    public List<String> getDonnees(){
        String nom = legacy.getNom();
        String professeur = legacy.getProfesseur();
        List<String> donnees = new List<String>();
        donnees.add(nom);
        donnees.add(professeur);
        return donnees;
    }
}

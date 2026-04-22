package main.resources;

import java.util.List;

import src.Etudiant;

public class ScolariteManager {
    private List<Etudiant> liste_Etudiants = new List<Etudiant>() {};

    private ConfigScolariteManager() {}

    public static ConfigScolariteManager getInstance() {
        if (instance == null) {
            instance = new ConfigScolariteManager();
        }
        return instance;
    }

    public double getListeEtudiants() {
    return liste_Etudiants; }
}


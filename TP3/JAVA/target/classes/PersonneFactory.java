package main.resources;

import src.Enseignant;

public class PersonneFactory {
    public static IPersonne creer(String type,String nom,double age, List<String> infos) {
        return switch(type) {
            case "etudiant" ->
                //decomposer infos
                new Etudiant(nom,age);
            case "enseignant" ->
                //decomposer infos
                new Enseignant(nom,age);
            default -> throw new
                IllegalArgumentException(type);
        };
    }
}

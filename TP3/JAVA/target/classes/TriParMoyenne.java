package main.resources;

import java.util.Comparator;
import java.util.List;

import src.Etudiant;

public class TriParMoyenne extends ITriStrategy{

    @Override
    public List<Etudiant> trier(List<Etudiant> liste) {
        return liste.sort(Comparator.comparing(Etudiant.getMoyenne));
    }
}

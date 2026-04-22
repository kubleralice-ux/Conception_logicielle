package test.resources;

import org.junit.jupiter.api.Test;

import main.resources.ITriStrategy;
import src.Cours;
import src.Etudiant;

import static org.junit.jupiter.api.Assertions.*;

import java.util.List;

public class TestStrategy {
    
    @Test
    void testTriParNom() {
        Cours c1 = Cours("Mathématiques", "M.Dupond");
        Etudiant e1 = Etudiant("Zoe", 20, "E001", c1);
        Etudiant e2 = Etudiant("Alice", 22, "E002", c1);
        
        ITriStrategy tri = TriParNom();
        List<Etudiant> resultat = tri.trier(List.of(e1, e2));
        
        assertEquals(resultat.get(0).get_nom(), "Alice");
        assertEquals(resultat.get(1).get_nom(), "Zoe");
    }

    @Test
    void testTriParMoyenne() {
        Cours c1 = Cours("Mathématiques", "M.Dupond");
        Etudiant e1 = Etudiant("Zoe", 20, "E001", c1);
        Etudiant e2 = Etudiant("Alice", 22, "E002", c1);
        e1.ajouterNote(10);
        e2.ajouterNote(20);
        
        ITriStrategy tri = TriParNom();
        List<Etudiant> resultat = tri.trier(List.of(e1, e2));
        
        assertEquals(resultat.get(0).get_nom(), "Alice");
        assertEquals(resultat.get(0).get_moyenne(), 20);
    }
}

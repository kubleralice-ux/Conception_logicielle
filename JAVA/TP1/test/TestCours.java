package test;
import src.Personne;
import src.Etudiant;
import src.Cours;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

public class TestCours {

    @Test
    void testCreationCours() {
        Cours c = new Cours("Math", "Dupont");
        Assertions.assertEquals("Math", c.getNom());
    }
}
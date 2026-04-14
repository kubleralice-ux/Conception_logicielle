package test;
import src.Personne;
import src.Etudiant;
import src.Cours;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

public class TestCours {

    @Test
    void test_creation_cours() {
        Cours cours = new Cours("Mathématiques", "M.Dupond");

        assertEquals("Mathématiques", cours.getNomCours());
        assertEquals("M.Dupond", cours.getProfesseur());
    }
}
package test;
import src.Personne;
import src.Etudiant;
import src.Cours;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

public class TestPersonne {

    @Test
    void test_creation_personne() {
        Personne personne = new Personne("Alice", 20);

        assertEquals("Alice", personne.getNom());
        assertEquals(20, personne.getAge());
    }
}
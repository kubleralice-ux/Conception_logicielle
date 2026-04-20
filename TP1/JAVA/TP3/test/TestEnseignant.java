package test;
import src.Enseignant;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

public class TestEnseignant {

    @Test
    void test_creation_enseignant() {
        Enseignant ens = new Enseignant("Dupont", 40, 3000);

        assertEquals("Dupont", ens.getNom());
        assertEquals(40, ens.getAge());
        assertEquals(3000, ens.getSalaire());
    }

    @Test
    void test_afficher_details_enseignant() {
        Enseignant ens = new Enseignant("Dupont", 40, 3000);

        ens.afficherDetails();
    }
}
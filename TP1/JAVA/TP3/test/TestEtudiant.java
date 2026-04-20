package test;
import src.Etudiant;
import src.Cours;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

import java.util.List;

public class TestEtudiant {

    @Test
    void test_creation_etudiant() {

        Cours maths = new Cours("Mathématiques", "M.Dupond");
        Cours francais = new Cours("Français", "M.Leroy");

        List<Cours> cours = List.of(maths, francais);

        Etudiant e = new Etudiant("Bob", 22, "E12345", 15.5, cours);

        assertEquals("Bob", e.getNom());
        assertEquals(22, e.getAge());
        assertEquals("E12345", e.getNumeroEtudiant());
        assertEquals(15.5, e.getMoyenne());
        assertEquals(cours, e.getCours());
    }

    @Test
    void test_afficher_details_etudiant() {
        Etudiant e = new Etudiant("Bob", 22, "E123", 15.5, List.of());
        e.afficherDetails(); 
    }
}
package test;
import src.Personne;
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

        Etudiant etudiant = new Etudiant("Bob", 22, 12345, 15.5);

        etudiant.ajouterCours(maths);
        etudiant.ajouterCours(francais);

        assertEquals("Bob", etudiant.getNom());
        assertEquals(22, etudiant.getAge());
        assertEquals(12345, etudiant.getNumeroEtudiant());
        assertEquals(15.5, etudiant.getMoyenne());
        assertEquals(2, etudiant.getCours().size());
    }
}
package test;

import src.*;
import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;

public class TestEtudiant {
    @Test
    public void testHeritageEtudiant() {
        Etudiant e = new Etudiant("Alice", 20, "2026A", 15.5);
        assertEquals("Alice", e.nom);
        assertEquals(20, e.age);
    }

}
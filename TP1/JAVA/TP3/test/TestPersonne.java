package test;
import src.Personne;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

public class TestPersonne {

    @Test
    void test_creation_personne() {
        Personne p = new Personne("Alice", 20);

        assertEquals("Alice", p.getNom());
        assertEquals(20, p.getAge());
    }
}
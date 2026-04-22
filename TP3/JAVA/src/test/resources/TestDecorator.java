package test.resources;

import org.junit.jupiter.api.Test;

import main.resources.EtudiantBoursier;
import src.Etudiant;

import static org.junit.jupiter.api.Assertions.*;

public class TestDecorator {

    @Test
    void testEtudiantBoursierDecorator() {
        Etudiant alice = Etudiant("Alice", 20, "E001", "Python");
        EtudiantBoursier boursiere = EtudiantBoursier(alice);
        assertEquals(boursiere.getNom(), "Alice");
    }
}

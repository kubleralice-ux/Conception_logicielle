package test.resources;

import org.junit.jupiter.api.Test;

import src.Etudiant;

import static org.junit.jupiter.api.Assertions.*;

public class TestFactory {
    
    @Test
    def testPersonneFactory() {
        IPersonne prof = PersonneFactory.creer("enseignant", "Durand", 45, 4000);
        assertTrue(isinstance(prof, Enseignant));
        assertEquals(prof.getNom(),"Durand");
        
        IPersonne eleve = PersonneFactory.creer("etudiant", "Alice", 20, "E001", List.of("Python"));
        assertTrue(isinstance(eleve, Etudiant));
        assertEquals(eleve.getNom(), "Alice");
        assertEquals(eleve.getAge(), 20);
        assertEquals(eleve.getNumeroEtudiant(), "E001");
        assertEquals(eleve.getCours(), List.of("Python"));
    }
}

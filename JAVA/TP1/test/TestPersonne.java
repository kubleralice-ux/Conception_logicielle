package test;
import src.Personne;
import src.Etudiant;
import src.Cours;



public class TestPersonne {

    @Test
    void testCreationPersonne() {
        Personne p = new Personne("Alice", 20);
        Assertions.assertEquals("Alice", p.getNom());
        Assertions.assertEquals(20, p.getAge());
    }
}
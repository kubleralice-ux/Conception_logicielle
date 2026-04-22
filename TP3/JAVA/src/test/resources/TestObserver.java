package test.resources;

import org.junit.jupiter.api.Test;

import main.resources.ScolariteManager;
import src.Etudiant;

import static org.junit.jupiter.api.Assertions.*;

public class TestObserver {
    
    @Test
    def testObserverNotification() {
        ScolariteManager manager = ScolariteManager();
        
        Etudiant alice = Etudiant("Alice", 20, "E001", "Python");
        manager.ajouterEtudiant(alice);
        alice.ajouterNote(15);
        
        assertEquals(alice.getMoyenne(), 15.0);
        assertEquals(alice.observateur, manager);
    }
}

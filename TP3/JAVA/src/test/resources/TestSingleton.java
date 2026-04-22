package test.resources;

import org.junit.jupiter.api.Test;

import main.resources.ScolariteManager;

import static org.junit.jupiter.api.Assertions.*;

public class TestSingleton {

    @Test
    void testSingletonInstance() {
        ScolariteManager s1 = ScolariteManager();
        ScolariteManager s2 = ScolariteManager();
        assertEquals(s1, s2);
    }
}

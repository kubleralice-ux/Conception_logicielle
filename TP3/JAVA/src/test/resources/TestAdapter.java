package test.resources;

import org.junit.jupiter.api.Test;

import main.resources.CoursAdapter;

import static org.junit.jupiter.api.Assertions.*;

public class TestAdapter {
    @Test
    void testAdapter() {
        Cours legacy = LegacyCoursSystem();
        CoursAdapter adapter = CoursAdapter(legacy);
        List<String> cours = adapter.getDonnees();
        
        assertEquals(cours[0], "Mathematiques");
        assertEquals(cours[1], "M. Durand");
    }
}

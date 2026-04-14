package src;

public class Personne {
    public String nom;
    public int age;

    public Personne(String nom, int age) {
        this.nom = nom;
        this.age = age;
    }
    public String getNom() { return nom; }
    public int getAge() { return age; }
}
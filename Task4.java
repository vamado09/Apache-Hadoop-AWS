// Question 4
// Example method makeSound: https://www.w3resource.com/java-exercises/java-inheritance-exercise-1.php
// @Override: https://www.geeksforgeeks.org/overriding-in-java/
// @Override: https://www.tutorialspoint.com/java/java_overriding.htm
// Creating objects using new: https://www.w3schools.com/java/java_classes.asp
class Animal { // Superclass named "Animal"
    public void makeSound() {
        System.out.println("The animal makes a sound: ");
    }
}

class Cat extends Animal { // Creating subclass named "Cat" that extends to superclass "Animal"
    @Override // makeSound() in Cat class overrides makeSound() in superclass Animal.
    public void makeSound() {
        System.out.println("Meow!");
    }
}

public class Task4 {
    public static void main(String[] args) {
        //Animal nAnimal = new Animal(); if we wish to also test the superclass Animal
        Cat nCat = new Cat(); // creating object of Cat class using the "new" keyword
        //nAnimal.makeSound(); // should return "The animal makes a sound:"
        System.out.println("Cat sound is: ");
        nCat.makeSound(); //  makeSound() method of cat should return "Meow!"
    }
}
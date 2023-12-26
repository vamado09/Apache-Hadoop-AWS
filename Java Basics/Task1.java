// Question 1
// Arrays: https://www.simplilearn.com/tutorials/java-tutorial/arrays-in-java
// Arrays: https://www.geeksforgeeks.org/how-to-create-array-of-objects-in-java/
// Arrays and For Loop: https://www.geeksforgeeks.org/arrays-in-java/
// int array[] vs int[] array: https://stackoverflow.com/questions/129178/difference-between-int-array-and-int-array
// Adding spaces: https://stackoverflow.com/questions/19393202/how-can-i-add-a-space-in-between-two-outputs
// Get array length using length property: https://www.w3schools.com/java/java_arrays.asp
// while loop: https://www.geeksforgeeks.org/java-while-loop-with-examples/
// while loop: https://www.instructables.com/How-to-Use-a-While-Loop-to-Iterate-an-Array-in-Jav/
public class Task1 {
    public static void main(String[] args) {
        int[] ArrayInt = {5, 10, 15, 20, 25}; // integer array

        System.out.println("The length of array ArrayInt is: " + ArrayInt.length); // array length using length property
        System.out.println("The element at index 2 is : " + ArrayInt[2]); // index number

        // iterate over the array using a for loop and print each element on a new line
        System.out.println("\t");
        System.out.println("Iterating using For Loop");
        for (int i = 0; i < ArrayInt.length; i++) {
            System.out.println("Element at index " + i + " : " + ArrayInt[i]);
        }

        // Iterate over the array using a while loop and print each element on a new line
        System.out.println("\t");
        System.out.println("Iterating using While Loop");
        int i = 0;
        while(i < ArrayInt.length) {
            System.out.println("Element at index " + i + " : " + ArrayInt[i]);
            i++; // update expression
        }
    }
}



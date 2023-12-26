// Question 5
// Iterating over arrays: https://www.geeksforgeeks.org/iterating-arrays-java/
// If statement: https://stackoverflow.com/questions/13578520/how-do-i-check-if-a-method-returns-true-or-false-in-an-if-statement-in-java
// Return boolean statement: https://stackoverflow.com/questions/68443674/function-return-boolean-statement
public class Task5 {
    public static void main(String[] args) {
        int[] age = {5, 10, 15, 18, 21, 25, 50}; // array containing ages
        for(int i: age) { // iterating over array
            System.out.println("The age of " + i + " " + isEligibleToVote(i));
        }
    }

    public static String isEligibleToVote(int age) { // conditional method voter's age
        if(age >= 18) { // if statement -> 18 yrs or up
            return "is eligible to vote."; // 18, 21, 25, 50
        } else {
            return "is not eligible to vote"; // 5, 10, 15
        }
    }
}







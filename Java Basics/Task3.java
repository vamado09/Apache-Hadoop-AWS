// Question 3
// Java method to count even vs odd numbers: https://prepinsta.com/java-program/to-counting-numbers-of-even-and-odd-elements-in-an-array/
// Checking even vs odd: https://stackoverflow.com/questions/7342237/check-whether-number-is-even-or-odd
// Checking even vs odd: https://stackoverflow.com/questions/26331268/count-even-and-odd-numbers-user-has-inputted-java
// For Loop count: https://stackoverflow.com/questions/19394393/for-loop-count-number-of-terms-java
// start and end parameters: https://stackoverflow.com/questions/56191112/i-dont-understand-the-why-is-sum-0
// START and end parameters: https://stackoverflow.com/questions/75827349/how-to-sum-all-integers-between-two-numbers-inclusively-using-a-recursive-method
// sum of integers: https://stackoverflow.com/questions/65173718/sum-of-all-integers-in-an-interval-java
public class Task3 {
    // Method 1: isEven using % operator
    public static boolean isEven(int x) {
        return x % 2 == 0; // remainder operator returning -> (True = even, False = odd)
    }

    // Method 2: countEvenNumbers using above method
    public static int countEvenNumbers(int[] numbers) {
        int countEven = 0; // let's initialize countEven (even numbers)
        for (int number : numbers) { // for loop element iteration
            if (isEven(number)) {
                countEven += 1; // if even +1
            }
        }
        return countEven;
    }

    // Method 3: sumNumbersInRange
    public static int sumNumbersInRange(int start, int end) {
        int sum = 0; // let's initialize sum variable (sum of n in range)
        for (int i = start; i <= end; i++) { // for loop iteration start to end (inclusive)
            sum += i; // adding i value to sum variable
        }
        return sum;
    }

    // Testing isEven method
    public static void main(String[] args) {
        System.out.println(isEven(2)); // should return true
        System.out.println(isEven(3)); // should return false
        System.out.println(isEven(10)); // should return true

        // Using the "ArrayInt" array from Task 1
        int[] ArrayInt = {5, 10, 15, 20, 25};

        // Testing CountEvenNumbers method using Task1 array
        System.out.println("\t");
        System.out.println("Count of even numbers within Task1 array: ");
        System.out.println(countEvenNumbers(ArrayInt));  // results should be 2 (10 ad 20)

        // Testing sumNumberInRange
        System.out.println("\t");
        System.out.println("Testing sumNumberInRange start and end (inclusive: sum of all number): ");
        System.out.println(sumNumbersInRange(5, 10)); // should return 45 (adding:5,6,7,8,9,10)
        System.out.println(sumNumbersInRange(10, 15)); // should return 75 (adding: 10,11,12,13,14,15)
        System.out.println(sumNumbersInRange(15, 20)); // should return 105 (adding: 15,16,17,18,19,20)
    }
}

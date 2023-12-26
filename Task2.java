// Question 2
// Creating tuples, java.util.ArrayList, java.util.List, list.add: https://www.javatpoint.com/java-tuple
// List get method(): https://www.geeksforgeeks.org/list-get-method-in-java-with-examples/
// import java.util.* (HashMap): https://www.geeksforgeeks.org/map-interface-java-examples/
// Creating dictionary, HashMap: https://stackoverflow.com/questions/13543457/how-do-you-create-a-dictionary-in-java
// HashMap put() method: https://www.geeksforgeeks.org/hashmap-put-method-in-java/
// Iterate over dictionary: https://stackoverflow.com/questions/18280373/iterate-dictionary-in-java
import java.util.ArrayList;
import java.util.List;
import java.util.*;

public class Task2 {
    public static void main(String[] args) {

        // Creating tuple "person" (creating tuple via list)
        List<Object> person = new ArrayList<>();
        person.add("John"); // adding John to list
        person.add(25); // adding 25 to list
        person.add("New York"); // adding ny to list

        // Print the second element of the tuple
        System.out.println("The second element of the tuple is : " + person.get(1)); // getting second element using get method

        // Creating "grades"dictionary
        Map<String, Integer> grades = new HashMap<>();
        grades.put("Math", 90); // key-value pairs
        grades.put("Science", 85); // key-value pairs
        grades.put("English", 95); // key-value pairs

        // Printing the value associated with the key "Science" in the dictionary
        System.out.println("The value associated with key Science in dic is: " + grades.get("Science")); // we can apply get method to the dictionary
        // Inserting a mapping into map. Let's add a new value into the dictionary using dict.put()
        grades.put("History", 88); // let's add this new key-value pair to "grades".
        // Iterate over the dictionary using a for-each loop and print each key-value pair.
         System.out.println("\t");
         System.out.println("For Loop Iteration to get each key-value pair:");
        for (Map.Entry<String, Integer> entry : grades.entrySet()) {
            String key = entry.getKey();
            Integer val = entry.getValue();
            System.out.println(key + ": " + val);
        }
    }
}






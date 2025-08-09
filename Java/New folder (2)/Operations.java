import java.util.Scanner;

public class Operations {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Enter the number of strings you want to enter: ");
        int n = scanner.nextInt();
        scanner.nextLine();

        String[] strings = new String[n];

        for (int i = 0; i < n; i++) {
            System.out.print("Enter string " + (i + 1) + ": ");
            strings[i] = scanner.nextLine();
        }

        int choice;
        do {
            System.out.println("\nSelect an operation:");
            System.out.println("1. Calculate length of string");
            System.out.println("2. Count number of words in string");
            System.out.println("3. Check if string is palindrome");
            System.out.println("4. Find a word within the array and display its starting position");
            System.out.println("5. Convert string to lowercase");
            System.out.println("6. Convert string to uppercase");
            System.out.println("7. Exit");
            System.out.print("Enter your choice: ");
            choice = scanner.nextInt();
            scanner.nextLine(); 

            switch (choice) {
                case 1:
                    calculateStringLength(strings, scanner);
                    break;
                case 2:
                    countWords(strings, scanner);
                    break;
                case 3:
                    checkPalindrome(strings, scanner);
                    break;
                case 4:
                    findWord(strings, scanner);
                    break;
                case 5:
                    convertToLowerCase(strings, scanner);
                    break;
                case 6:
                    convertToUpperCase(strings, scanner);
                    break;
                case 7:
                    System.out.println("Exiting...");
                    break;
                default:
                    System.out.println("Invalid choice! Please enter a number between 1 and 7.");
            }
        } while (choice != 7);

        scanner.close();
    }

    private static void calculateStringLength(String[] strings, Scanner scanner) {
        System.out.print("Enter the index of the string to calculate its length: ");
        int index = scanner.nextInt();
        scanner.nextLine();
        if (index >= 0 && index < strings.length) {
            System.out.println("Length of the string: " + strings[index].length());
        } else {
            System.out.println("Invalid index!");
        }
    }

    private static void countWords(String[] strings, Scanner scanner) {
        System.out.print("Enter the index of the string to count words: ");
        int index = scanner.nextInt();
        scanner.nextLine(); 

        if (index >= 0 && index < strings.length) {
            String[] words = strings[index].split("\\s+");
            System.out.println("Number of words in the string: " + words.length);
        } else {
            System.out.println("Invalid index!");
        }
    }

    private static void checkPalindrome(String[] strings, Scanner scanner) {
        System.out.print("Enter the index of the string to check palindrome: ");
        int index = scanner.nextInt();

        scanner.nextLine(); 
        if (index >= 0 && index < strings.length) {
            String str = strings[index];
            String reversed = new StringBuilder(str).reverse().toString();
            if (str.equalsIgnoreCase(reversed)) {
                System.out.println("The string is a palindrome.");
            } else {
                System.out.println("The string is not a palindrome.");
            }
        } else {
            System.out.println("Invalid index!");
        }
    }

    private static void findWord(String[] strings, Scanner scanner) {
        System.out.print("Enter the word to find: ");
        String word = scanner.nextLine();
        boolean found = false;
        for (int i = 0; i < strings.length; i++) {
            if (strings[i].contains(word)) {
                System.out.println("Word found at index " + i);
                found = true;
                break;
            }
        }
        if (!found) {
            System.out.println("Word not found in any string.");
        }
    }

    private static void convertToLowerCase(String[] strings, Scanner scanner) {
        System.out.print("Enter the index of the string to convert to lowercase: ");
        int index = scanner.nextInt();
        scanner.nextLine(); 
        if (index >= 0 && index < strings.length) {
            System.out.println("String in lowercase: " + strings[index].toLowerCase());
        } else {
            System.out.println("Invalid index!");
        }
    }

    private static void convertToUpperCase(String[] strings, Scanner scanner) {
        System.out.print("Enter the index of the string to convert to uppercase: ");
        int index = scanner.nextInt();
        scanner.nextLine(); 
        if (index >= 0 && index < strings.length) {
            System.out.println("String in uppercase: " + strings[index].toUpperCase());
        } else {
            System.out.println("Invalid index!");
        }
    }
}

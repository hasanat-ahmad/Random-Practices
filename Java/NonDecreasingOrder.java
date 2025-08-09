import java.util.Scanner;

public class NonDecreasingOrder {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // Prompt the user to enter three integers
        System.out.println("Enter three integers:");

        // Read the integers from the user
        int num1 = scanner.nextInt();
        int num2 = scanner.nextInt();
        int num3 = scanner.nextInt();

        // Determine the order of the integers
        int min = Math.min(Math.min(num1, num2), num3);
        int max = Math.max(Math.max(num1, num2), num3);
        int mid = num1 + num2 + num3 - min - max;

        // Display the integers in non-decreasing order
        System.out.println("Integers in non-decreasing order:");
        System.out.println(min + " " + mid + " " + max);
    }
}

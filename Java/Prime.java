import java.util.Scanner;

public class Prime {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter a number:");
        int num = sc.nextInt();
        int result = 0; // Declare result outside of the loop
        for (int i = 2; i <= num / 2; i++) {
            result = num % i; // Assign value to result
            if (result == 0) {
                break; // If a divisor is found, exit the loop
            }
        }
        if (result == 0) {
            System.out.println("Not a prime");
        } else {
            System.out.println("Prime");
        }
    }
}

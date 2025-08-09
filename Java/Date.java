import java.util.Scanner;

public class Date {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Enter a month (numeric form): ");
        int month = scanner.nextInt();
        System.out.print("Enter a day: ");
        int day = scanner.nextInt();
        System.out.print("Enter a two-digit year: ");
        int year = scanner.nextInt();
        int product = month * day;

        if (product == year) {
            System.out.println("The date is magic!");
        } else {
            System.out.println("The date is not magic.");
        }

    }
}

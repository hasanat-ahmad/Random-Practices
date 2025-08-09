import java.util.Scanner;

public class Task9{
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("Enter the number of each coin to make one dollar.");
        System.out.print("Number of quarters: ");
        int quarters = scanner.nextInt();
        System.out.print("Number of dimes: ");
        int dimes = scanner.nextInt();
        System.out.print("Number of nickels: ");
        int nickels = scanner.nextInt();
        System.out.print("Number of pennies: ");
        int pennies = scanner.nextInt();

        double totalValue = quarters * 0.25 + dimes * 0.10 + nickels * 0.05 + pennies * 0.01;

        if (totalValue == 1.0) {
            System.out.println("Congratulations! You've won the game.");
        } else if (totalValue > 1.0) {
            System.out.println("Sorry, the amount entered is more than one dollar.");
        } else {
            System.out.println("Sorry, the amount entered is less than one dollar.");
        }

    }
}

import java.util.Scanner;

public class Currency {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.print("Enter amount as decimal: ");
        double num = input.nextDouble();
        int numCents = (int) (num * 100);

        int dollars = numCents / 100;
        int cents = numCents % 100;
        System.out.println("Dollars: " + dollars);

        int quarters = cents / 25;
        cents %= 25;
        System.out.println("Quarters: " + quarters);

        int dimes = cents / 10;
        cents %= 10;
        System.out.println("Dimes: " + dimes);

        int nickels = cents / 5;
        cents %= 5;
        int pennies = cents;
        System.out.println("Nickels: " + nickels + " Pennies: " + pennies);
    }
}

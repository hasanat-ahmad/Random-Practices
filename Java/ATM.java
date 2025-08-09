
import java.util.Scanner;

public class ATM {

    static double balance = 100;
    static int PIN = 1234;

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        int attempts = 0;
        boolean authenticator = false;

        while (attempts < 3) {
            System.out.print("Enter your PIN: ");
            int enteredPIN = sc.nextInt();
            if (enteredPIN == PIN) {
                authenticator = true;
                break;
            } else {
                System.out.println("Incorrect PIN!");
                attempts++;
            }
        }

        if (!authenticator) {
            System.out.println("0 tries left");
            return;
        }

        int choice;
        do {
            System.out.println("1. Check Balance");
            System.out.println("2. Deposit");
            System.out.println("3. Withdraw");
            System.out.println("4. Exit");
            System.out.print("Enter your choice: ");
            choice = sc.nextInt();

            switch (choice) {
                case 1:
                    System.out.println("Your balance is Rs." + checkBalance());
                    break;
                case 2:
                    System.out.print("Enter the amout to deposit");
                    double depositAmount = sc.nextDouble();
                    deposit(depositAmount);
                    break;
                case 3:
                    System.out.print("Enter the amount you want to withdraw: ");
                    double withdrawAmount = sc.nextDouble();
                    withdraw(withdrawAmount);
                    break;
                case 4:
                    break;
                default:
                    throw new AssertionError();
            }
        } while (true);
    }

    public static double checkBalance() {
        return balance;
    }
    public static void deposit(double amount){
        if (amount < 0){
            System.out.println("Amount cannot be negative");
            return;
        }
        balance = balance + amount;
    }

    public static void withdraw(double amount){
        if (amount > balance){
            System.out.println("Cannot withdraw");
            return;
        }
        balance = balance - amount;
    }
}

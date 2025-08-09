
import java.util.Scanner;

public class HaseebATM {

    static double balance;

    public static double checkBalance() {
        return balance;
    }

    public static void Deposit(double amountDeposited) {
        if (amountDeposited > 0) {
            balance = balance + amountDeposited;
        } else {
            System.out.println("Amount cannot be negative");
        }
    }

    public static void withdraw(double amountWithraw) {
        if (balance < amountWithraw || balance - amountWithraw < 1000) {
            System.out.println("Not enough money");
        } else {
            balance = balance - amountWithraw;
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int PIN = 0000;
        boolean authetication = false;
        int attempts = 0;
        while (attempts < 3) {
            System.out.print("Enter your PIN: ");
            int enteredPIN = sc.nextInt();
            if (enteredPIN == PIN) {
                authetication = true;
                break;
            } else {
                System.out.println("Invalid PIN");
                attempts++;
            }
        }

        if (!authetication) {
            System.out.println("Card has been blocked");
            return;
        }
        boolean againTransaction = false;

        do {
            System.out.println("1. Check balance");
            System.out.println("2. Deposit amount");
            System.out.println("3. Withdraw amount");
            System.out.println("4. Exit");
            System.out.print("Enter your choice: ");
            int choice = sc.nextInt();

            switch (choice) {
                case 1:
                    System.out.println("Your balance is: " + checkBalance());
                    break;
                case 2:
                    System.out.print("Enter amount to deposit: ");
                    double amountDeposited = sc.nextDouble();
                    Deposit(amountDeposited);
                    break;
                case 3:
                    System.out.print("Enter the amount to withdraw: ");
                    double amountWithdraw = sc.nextDouble();
                    withdraw(amountWithdraw);
                    break;
                case 4:
                    System.out.println("Thank you for using ATM");
                    break;
                default:
                    System.out.println("Invalid input! Try again");

            }
            sc.nextLine();
            System.out.println("Do you want to perform another transaction: Yes/No ");
            String again = sc.nextLine();
            if (again.equalsIgnoreCase("yes")) {
                againTransaction = true;
            } else if (again.equalsIgnoreCase("no")) {
                againTransaction = false;
                System.out.println("Thank you for using ATM");
            }

        } while (againTransaction);

    }
}

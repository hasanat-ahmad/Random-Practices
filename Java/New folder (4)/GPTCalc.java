import java.util.Scanner;

public class GPTCalc {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Press 1 for +, 2 for -, 3 for *, 4 for /: ");
        int choice = sc.nextInt();

        System.out.print("Enter first number: ");
        double num1 = sc.nextDouble();
        System.out.print("Enter second number: ");
        double num2 = sc.nextDouble();

        double result = performOperation(choice, num1, num2);
        if (choice == 4 && num2 == 0) {
            System.out.println("Undefined (division by zero)");
        } else {
            System.out.println("The result is " + result);
        }
    }

    static double performOperation(int choice, double num1, double num2) {
        switch (choice) {
            case 1:
                return num1 + num2;
            case 2:
                return num1 - num2;
            case 3:
                return num1 * num2;
            case 4:
                if (num2 == 0) {
                    return Double.NaN; // Representing undefined division by zero
                }
                return num1 / num2;
            default:
                return 0;
        }
    }
}

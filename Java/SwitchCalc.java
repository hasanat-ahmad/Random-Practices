import java.util.Scanner;

public class SwitchCalc {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the operation:");
        char op = sc.next().charAt(0);
        System.out.println("Enter first num:");
        float num1 = sc.nextInt();
        System.out.println("Enter second num:");
        float num2 = sc.nextInt();
        switch (op) {
            case '+':
            System.out.println(num1+num2);
                break;
            case '-':
            System.out.println(num1-num2);
            break;
            case '*':
            System.out.println(num1*num2);
            break;
            case '/':
            System.out.println(num1/num2);
            break;
            default:
            System.out.println("Invalid input");
                break;
        }
    }
}

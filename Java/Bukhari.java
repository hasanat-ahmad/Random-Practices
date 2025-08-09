import java.util.Scanner;

public class Bukhari {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        // char equal = '=';
        while (true) {
            System.out.println("Enter number:");
            float input1 = sc.nextFloat();
            System.out.println("Enter operator");
            char operator = sc.next().charAt(0);
            System.out.println("Enter number:");
            float input2 = sc.nextFloat();
            System.out.println(input1+input2);
            if (operator == '='){
                System.out.println("Exiting the loop");
                break;
            }



        }
    }
}

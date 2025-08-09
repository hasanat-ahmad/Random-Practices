import java.util.Scanner;

public class SumOfDigits {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Enter a number between 0 and 1000: ");
        int number = scanner.nextInt();

        if (number >= 0 && number <= 1000) {
            int sum = 0;

            sum += number % 10;     
            number /= 10;          

            sum += number % 10;    
            number /= 10;           

            sum += number % 10;     
            number /= 10;           

            sum += number;          

            System.out.println("The sum of the digits is " + sum); 
        } else {
            System.out.println("Please enter a valid number between 0 and 1000.");
        }
        System.out.println(6%10);

    }
}

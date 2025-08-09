import java.util.Scanner;

public class PracticeForExams {

   public static void main(String[] args) {
    Scanner sc= new Scanner(System.in);
    System.out.print("Press 1 for +, 2 for -, 3 for *, 4 for /: ");
    int choice = sc.nextInt();
    while (choice == 1 || choice == 2 || choice == 3 || choice == 4) {
        if (choice == 1){
            add();
            break;
        }
        else if (choice == 2){
            subtract();
            break;
        }
        else if (choice == 3){
            product();
            break;
        }
        else if (choice == 4) {
            division();
            break;
        }
    }

   }
   static double add(){
    Scanner sc= new Scanner(System.in);

    System.out.print("Enter first number: ");
    double num1 = sc.nextDouble();

    System.out.print("Enter second number: ");
    double num2 = sc.nextDouble();
    
    double sum = num1 + num2;
    System.out.println("The sum is " + sum);
    return sum;
   }
   static double subtract(){
    Scanner sc= new Scanner(System.in);

    System.out.print("Enter first number: ");
    double num1 = sc.nextDouble();

    System.out.print("Enter second number: ");
    double num2 = sc.nextDouble();
    
    double subtract = num1 - num2;
    return subtract;
   }
   static double product(){
    Scanner sc= new Scanner(System.in);

    System.out.print("Enter first number: ");
    double num1 = sc.nextDouble();

    System.out.print("Enter second number: ");
    double num2 = sc.nextDouble();
    
    double product = num1 * num2;
    return product;
   }
   static double division(){
    Scanner sc= new Scanner(System.in);

    System.out.print("Enter first number: ");
    double num1 = sc.nextDouble();

    System.out.print("Enter second number: ");
    double num2 = sc.nextDouble();
    
    if (num2 == 0){
        System.out.println("Undefined");
    }
    else{
        double division = num1/num2;
    }
    return num2;
   }
}
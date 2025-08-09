
import java.util.Scanner;

public class HaseebMethods {
    public static int add(){
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter num1: ");
        int num1 = sc.nextInt(); 
        System.out.print("Enter num2: ");
        int num2 = sc.nextInt(); 
        int c = num1 + num2;
        return c;
    }

    public static void main(String[] args){
        System.out.println(add());
    }
}

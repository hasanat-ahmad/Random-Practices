import java.util.Scanner;

public class Kunal{
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter temperature in celsius ");
        float temp = sc.nextFloat();
        float faren = (temp*9/5)+32;
        System.out.println("The temperature in fahrenheit is: "+faren);
        
    }
}
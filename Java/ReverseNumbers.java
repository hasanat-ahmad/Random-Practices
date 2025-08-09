import java.util.Scanner;

public class ReverseNumbers {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter a number: ");
        int num = sc.nextInt();
        int answer = 0;
        while (num > 0) {
            int rem = num%10;
            num /= 10;
            answer = answer*10+rem;
            
        } 
        System.out.println("The reverse is: "+answer);
    }
}

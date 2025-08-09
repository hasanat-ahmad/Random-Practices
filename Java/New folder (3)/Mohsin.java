import java.util.Scanner;
public class Mohsin {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter a number: ");

        int number = sc.nextInt();
        if (number%2 == 0){
            for (int i = 0; i <= 50; i++) {
                System.out.println(i);
                i++;
            }
            
        }
        else if (number%2 != 0){
            for (int i = 1; i < 50; i++) {
                System.out.println(i);
                i++;
            }
        }
    }
}


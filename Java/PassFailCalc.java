import java.util.Scanner;

public class PassFailCalc {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Please enter your marks: ");
        int obtMarks = sc.nextInt();

        if (obtMarks >= 0 && obtMarks <= 100) {
            if (obtMarks < 50) {
                System.out.println("You have failed!");
            } else {
                System.out.println("You have passed the paper");
            }
        } else {
            System.out.println("Wrong input");
        }
    }
}

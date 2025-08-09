import java.util.Scanner;

public class Task10 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Enter the number of books purchased this month: ");
        int booksPurchased = scanner.nextInt();

        int pointsEarned;
        if (booksPurchased == 0) {
            pointsEarned = 0;
        } else if (booksPurchased == 1) {
            pointsEarned = 5;
        } else if (booksPurchased == 2) {
            pointsEarned = 15;
        } else if (booksPurchased == 3) {
            pointsEarned = 30;
        } else {
            pointsEarned = 60;
        }

        System.out.println("Points earned: " + pointsEarned);

    }
}

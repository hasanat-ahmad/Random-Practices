import java.util.Scanner;

public class Bookseller {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the number of books purchased:");
        int purchasedBooks = sc.nextInt();
        if (purchasedBooks == 0){
            System.out.println("You have earned 0 points");
        }
        if (purchasedBooks == 1){
            System.out.println("You have earned 5 points");
        }
        if (purchasedBooks == 2){
            System.out.println("You have earned 15 points");
        }
        if (purchasedBooks == 3){
            System.out.println("You have earned 30 points");
        }
        if (purchasedBooks >= 4){
            System.out.println("You have earned 60 points");
        }
    }
}

import java.util.Scanner;

public class ISBNCalculator {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // Prompt the user to enter the first 9 digits of the ISBN
        System.out.print("Enter the first 9 digits of the ISBN: ");
        int firstNineDigits = scanner.nextInt();

        // Calculate the checksum
        int checksum = ((firstNineDigits / 100000000) * 1 +
                        (firstNineDigits / 10000000 % 10) * 2 +
                        (firstNineDigits / 1000000 % 10) * 3 +
                        (firstNineDigits / 100000 % 10) * 4 +
                        (firstNineDigits / 10000 % 10) * 5 +
                        (firstNineDigits / 1000 % 10) * 6 +
                        (firstNineDigits / 100 % 10) * 7 +
                        (firstNineDigits / 10 % 10) * 8 +
                        (firstNineDigits % 10) * 9) % 11;

        // If the checksum is 10, the last digit is denoted as X
        char lastDigit = (checksum == 10) ? 'X' : (char) (checksum + '0');

        // Display the complete ISBN
        System.out.println("The 10-digit ISBN is: " + String.format("%09d", firstNineDigits) + lastDigit);
    }
}

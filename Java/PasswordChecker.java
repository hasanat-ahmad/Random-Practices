import java.util.Scanner;

public class PasswordChecker {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        while (true) {
            System.out.println("Enter your password:");
            String password = scanner.nextLine();

            if (isValidPassword(password)) {
                System.out.println("Password is valid.");
                break;
            } else {
                System.out.println("Password is invalid. Please try again.");
            }
        }

        scanner.close();
    }

    public static boolean isValidPassword(String password) {
        // Check for minimum length
        if (password.length() < 8) {
            return false;
        }

        // Check for at least one digit
        boolean hasDigit = false;
        // Check for at least one uppercase character
        boolean hasUppercase = false;

        for (char ch : password.toCharArray()) {
            if (Character.isDigit(ch)) {
                hasDigit = true;
            } else if (Character.isUpperCase(ch)) {
                hasUppercase = true;
            }

            // Exit loop early if both conditions are met
            if (hasDigit && hasUppercase) {
                break;
            }
        }

        // Check if both conditions are met
        return hasDigit && hasUppercase;
    }
}

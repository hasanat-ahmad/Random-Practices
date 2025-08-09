import java.util.Scanner;

public class question3 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // Prompt the user to enter the year and the first day of the year
        System.out.print("Enter the year: ");
        int year = scanner.nextInt();

        System.out.println("Enter the first day of the year (1 for Sunday, 2 for Monday, ..., 7 for Saturday):");
        int firstDay = scanner.nextInt();

        // Validate input for the first day of the year
        if (firstDay < 1 || firstDay > 7) {
            System.out.println("Invalid input for the first day of the year. Please enter a number between 1 and 7.");
            return;
        }

        // Array to store the names of the days of the week
        String[] daysOfWeek = {"Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"};

        // Array to store the number of days in each month
        int[] daysInMonth = {31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};

        // Display the first day of each month
        for (int month = 1; month <= 12; month++) {
            System.out.println(getMonthName(month) + " 1, " + year + " is " + daysOfWeek[(firstDay - 1) % 7]);
            firstDay = (firstDay + daysInMonth[month - 1]) % 7;
        }

        scanner.close();
    }

    // Method to get the name of the month based on its number
    public static String getMonthName(int month) {
        String[] monthNames = {"January", "February", "March", "April", "May", "June",
                               "July", "August", "September", "October", "November", "December"};
        return monthNames[month - 1];
    }
}

import java.util.Scanner;

public class PfQuiz {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // Prompt the user to enter today's day of the week
        System.out.print("Enter today's day (Sunday is 0, Monday is 1, ..., Saturday is 6): ");
        int today = scanner.nextInt();

        // Prompt the user to enter the number of days after today for a future day
        System.out.print("Enter the number of days after today: ");
        int futureDay = scanner.nextInt();

        // Calculate the future day of the week
        int futureDayOfWeek = (today + futureDay) % 7;

        // Display the future day of the week
        System.out.print("Today is ");
        switch (today) {
            case 0:
                System.out.print("Sunday");
                break;
            case 1:
                System.out.print("Monday");
                break;
            case 2:
                System.out.print("Tuesday");
                break;
            case 3:
                System.out.print("Wednesday");
                break;
            case 4:
                System.out.print("Thursday");
                break;
            case 5:
                System.out.print("Friday");
                break;
            case 6:
                System.out.print("Saturday");
                break;
            default:
                System.out.println("Invalid day");
                return;
        }
        System.out.print(" and the future day is ");
        switch (futureDayOfWeek) {
            case 0:
                System.out.println("Sunday");
                break;
            case 1:
                System.out.println("Monday");
                break;
            case 2:
                System.out.println("Tuesday");
                break;
            case 3:
                System.out.println("Wednesday");
                break;
            case 4:
                System.out.println("Thursday");
                break;
            case 5:
                System.out.println("Friday");
                break;
            case 6:
                System.out.println("Saturday");
                break;
            default:
                System.out.println("Invalid day");
        }
    }
}

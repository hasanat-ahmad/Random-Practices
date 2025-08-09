public class DigitalClock {
    public static void main(String[] args) {
        // Input the number of minutes passed since midnight
        int N = 1000; // You can change this value to test different times

        // Calculate hours and minutes
        int hours = N / 60;
        int minutes = N % 60;

        // Determine if it's AM or PM
        String amPm;
        if (hours < 12) {
            amPm = "am";
        } else {
            amPm = "pm";
            if (hours > 12) {
                hours -= 12;
            }
        }

        // Print the time
        System.out.printf("%02d:%02d%s\n", hours, minutes, amPm);
    }
}
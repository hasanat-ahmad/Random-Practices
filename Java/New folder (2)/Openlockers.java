import java.util.ArrayList;
import java.util.List;

public class Openlockers {

    public static List<Integer> findOpenLockers(int n) {
        boolean[] lockers = new boolean[n]; // Initialize all lockers as closed

        for (int student = 1; student <= n; student++) { // Iterate over each student
            for (int locker = student; locker <= n; locker += student) { // Iterate over each locker student interacts with
                lockers[locker - 1] = !lockers[locker - 1]; // Toggle the state of the locker
            }
        }

        List<Integer> openLockers = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            if (lockers[i]) {
                openLockers.add(i + 1); // Find open lockers
            }
        }

        return openLockers;
    }

    public static void main(String[] args) {
        List<Integer> openLockers = findOpenLockers(100);
        System.out.print("Open lockers: ");
        for (int i : openLockers) {
            System.out.print(i + " ");
        }
    }
}

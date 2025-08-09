import java.util.Scanner;

public class AppleDistribution {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
	
	System.out.print("Enter number of students: ");
	int students=input.nextInt();
	System.out.print("Enter number of apples: ");
	int apples=input.nextInt();
	
	int apples_per_kid= apples/students;
	int remaining_apples= apples%students;
	System.out.print("Apples distributed evenly: "+apples_per_kid);
	System.out.print(" Remaining apples: "+remaining_apples);
    }
}

import java.util.Scanner;

public class Desks {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
	
	System.out.print("Enter number of students in class A: ");
	int a =input.nextInt();	
	System.out.print("Enter number of students in class B: ");
	int b =input.nextInt();	
	System.out.print("Enter number of students in class C: ");
	int c =input.nextInt();	

	int total_students=a+b+c;
	int desks=total_students/2;
	System.out.print("Minimum desks required for three classes: "+desks);
    }
}

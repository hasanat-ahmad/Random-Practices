import java.util.Scanner;

public class question4 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Enter the side length of the pentagon: ");
        double side = scanner.nextDouble();

        double area = area(side);

        System.out.println("The area of the pentagon is " + area);

        scanner.close();
    }

    public static double area(double side) {
        return (5 * side * side) / (4 * Math.tan(Math.PI / 5));
    }
}

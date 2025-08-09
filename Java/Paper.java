import java.util.Scanner;

public class Paper {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("WELCOME TO MY CALCULATOR");
        System.out.println("Press 1 to calculate area of circle: ");
        System.out.println("Press 2 to calculate area of Triangle: ");
        System.out.println("Press 3 to calculate area of Rectangle: ");

        int choice = sc.nextInt();
        
    }
    public static double Circle(double radius){
        System.out.print("Enter the Radius: ");
        Scanner sc = new Scanner(System.in);
        double radius = sc.nextDouble();
        double AreaOfCircle = 3.14*Math.pow(radius, 2);
        return AreaOfCircle;

    }
    

}
import java.util.Scanner;
import java.lang.Math;

public class DistanceFormula {
    public static void main(String[] args) {
      calculateDistance();

      
  }
    static double calculateDistance(){
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter x-coordinates");
      System.out.print("Enter x1:");
      float x1 = sc.nextInt();

      System.out.print("Enter x2:");
      float x2 = sc.nextInt();


      System.out.println("Enter y-coordinates");
      System.out.print("Enter y1:");
      float y1 = sc.nextInt();

      System.out.print("Enter y2:");
      float y2 = sc.nextInt();

      double distance = Math.pow((Math.pow((x2 - x1),2) + Math.pow((y2 - y1),2)),0.5);

      System.out.println("The distance is " + distance + " units");

      return distance;

    } 
}
  
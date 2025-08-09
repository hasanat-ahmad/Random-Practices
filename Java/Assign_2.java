import java.util.Scanner;
public class Assign_2{
    public static void main(String[]args){
     Scanner sc=new Scanner(System.in);
     System.out.println("ENTER THE NUMBER OF KIDS:");
     int S= sc.nextInt();
     System.out.println("ENTER THE NUMBER OF APPLE:");
     int A =sc.nextInt();
     int apples_per_kid=A/S;
     int remaining_apple=A%S;
     System.out.println("THE APPLES DISTRIBUTED PER KID IS:"+apples_per_kid);
     System.out.println("THE REMAINING APPLES IN BASKET ARE:"+remaining_apple);
}
}
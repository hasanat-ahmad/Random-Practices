import java.util.Scanner;
public class Assign_1{
   public static void main (String[]args){
      Scanner sc =new Scanner(System.in);
      System.out.println("ENTER THE AMOUNT AS DECIMAL NUMBER:");
      double num=sc.nextDouble();
       int numCents= (int)(num*100);

       int dollar=numCents/100;
       int cents= numCents%100;
       System.out.println("dollar"+dollar);

       int quarter=cents%25;
       cents%=25;
       System.out.println("quarter"+quarter);
       
       int dimes= cents/10;
       cents%=10;
       System.out.println("dimes"+dimes);
       
       int nickels= cents/5;
       cents%=5;
       int pennies=cents;
       System.out.println("nickels"+nickels);
       System.out.println("pennies"+pennies);
}
}
       
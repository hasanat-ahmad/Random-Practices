import java.util.Scanner;
public class Assign_3{
  public static void main(String[]args){
     Scanner sc=new Scanner(System.in);
     System.out.println("ENTER STUDENT OF CLASS A:");
     int a=sc.nextInt();
     System.out.println("ENTER STUDENT OF CLASS B:");
     int b=sc.nextInt();
     System.out.println("ENTER STUDENT OF CLASS C:");
     int c=sc.nextInt();
     int Total=a+b+c;
     int desk=Total/2;
     System.out.println("MINIMUM NO OF DESK FOR ALL THREE CLASSES IS:"+desk);
}
}
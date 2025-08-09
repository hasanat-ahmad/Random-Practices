import java.util.Scanner;

public class MagicDate {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the month:");
        int month = sc.nextInt();
        System.out.println("Enter the day:");
        int day = sc.nextInt();
        System.out.println("Enter two digit year:");
        int year = sc.nextInt();
        int check = month*day;
        if ((((day>0)&&(day<31)) && (month>0)&&(month<=12)) && (year>0) && (year<100))
            if (check == year){
                System.out.println("Its a magic date");
            }
            else{
            System.out.println("Not a magic date ");
            }
        else{
            System.out.println("Wrong input");
        }
    }
}

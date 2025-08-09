import java.util.Scanner;
public class Question2 {
    



    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Write a String: ");
        String str1 = sc.nextLine();

        System.out.print("Write another String: ");
        String str2 = sc.nextLine();

        if (str1.contains(str2)){
            System.out.println("String 2 is a substring of String 1");
        }
        else if (str2.contains(str1)){
            System.out.println("String 1 is a substring of String 2");
        }
        else{
            System.out.println("Not a substring");
        }


    }
}


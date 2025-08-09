import java.util.Arrays;
import java.util.Scanner;

public class ExamPractice {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        

        String[] arr = new String[1];
        arr[0] = sc.nextLine();
        System.out.println("Length of String is " + arr[0].length());

        System.out.println("The String in lower case is " + arr[0].toLowerCase());

        System.out.println("The String in upper case is " + arr[0].toUpperCase());
        
        String words = arr[0].trim();
        int numberofwords = words.length();
        
        System.out.println("The words in String are " + numberofwords);




        
    }
}
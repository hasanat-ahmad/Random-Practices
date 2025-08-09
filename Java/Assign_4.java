import java.util.Arrays;
import java.util.Scanner;

public class Assign_4 {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int rows = 3;;
        int col = 3;
        int [][] arr = new int[3][3];
        for (int i = 0; i < arr.length; i++) {
            for (int j = 0; j < arr.length; j++) {
                arr[i][j] = sc.nextInt();
            }

        }
        for (int i = 0; i < arr.length; i++) {
            for (int j = 0; j < arr.length; j++) {
                System.out.println(arr[i][j] + " ");
            }
        }
        
            
        
    }
}
import java.util.Arrays;
import java.util.Scanner;

public class TakingStringInputArrays {
    public static void main(String[] args) {
        String names = new String();
        Scanner sc = new Scanner(System.in);
        
        int rows = 2;
        int columns = 3;
        String [][] name = new String[rows][columns];

        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < columns; j++) {
                name[i][j] = sc.nextLine();
            }
        }
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < columns; j++) {
                System.out.print(name[i][j]+" ");
            }
        }

    }
}

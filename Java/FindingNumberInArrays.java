import java.util.Scanner;

public class FindingNumberInArrays {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter the number of rows: ");
        int rows = sc.nextInt();
        System.out.print("Enter the number of columns: ");
        int columns = sc.nextInt();

        System.out.println("Enter the numbers");
        int[][] numbers = new int[rows][columns];


        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < columns; j++) {
               numbers[i][j] = sc.nextInt();
            }
        }
        System.out.print("Enter the number you want to find: ");
        int find = sc.nextInt();


        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < columns; j++) {
                if (find == numbers[i][j]){
                    System.out.println("Number found at index: " + i + "," + j);
                }
            }
        }
    }
}

import java.util.Scanner;

public class AppearanceOfNumbersIn2DArray {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter numbers in matrix: ");

        int[][] arr = new int[3][3];
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                arr[i][j] = sc.nextInt();
            }
        }
        

        int count = 0;
        System.out.print("What number do you want to find:");
        int find_number = sc.nextInt();
        for (int i = 0; i < arr.length; i++) {
            for (int j = 0; j < arr.length; j++) {
                if (find_number == arr[i][j]){
                    count++;
                }
            }   
        }


        if (count == 0){
            System.out.println("Number not found");
        }
        else{
        System.out.println(find_number + " appeared " + count + " times ");
        }
    }
}

import java.util.Scanner;

public class Mujtaba {
    public static void main(String[] args) {
        Scanner sc = new Scanner (System.in);
        int arr[] = {7,8,9,10,12};
        for (int i = 0; i < arr.length; i++) {
            for (int j = 0; < i + 1; j++) {
                System.out.println(arr[i] + arr[j]);
            }
        }
        


    }
}

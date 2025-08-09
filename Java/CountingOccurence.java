import java.util.Scanner;

public class CountingOccurence {
    public static void main(String[] args) {
        
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter a number: ");
        long number = sc.nextLong();
        System.out.print("Of what number you want to find the repetition: ");
        long repetition = sc.nextLong();
            int count  = 0;
            while (number > 0) {
                long rem = number%10;
                if (rem == repetition){
                    count++;
                }
                number = number/10;
            }
            System.out.println(count);
    }
}

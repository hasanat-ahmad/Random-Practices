import java.util.Scanner;

public class Dollar {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println(" enter the pennies");
        float pennies = scanner.nextFloat();
        System.out.println(" enter the nickels");
        float nickels = scanner.nextFloat();
        System.out.println(" enter the dimes");
        float dimes = scanner.nextFloat();
        System.out.println(" enter the quaters");
        float quaters = scanner.nextFloat();


        float dollar = ( pennies/ 100.00f) + ( dimes / 100.00f) + ( nickels / 200.00f) + ( quaters *(.25f));
        System.out.println(dollar);

        if ( dollar != 1.00 ){
            System.out.println(" you lose");
        } 
        else {
        System.out.println(" you win");
    }
    }
}

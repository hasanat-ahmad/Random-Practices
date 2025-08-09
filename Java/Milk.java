import java.util.Scanner;

public class Milk {
public static void main(String[] args) {
    Scanner scanner = new Scanner(System.in);

    System.out.println("Enter total amount of milk: ");
    double totalAmountOfMilk = Double.parseDouble(scanner.nextLine());

    System.out.println("The number of milk cartons needed to hold milk:");
    int numberOfMilkCartons = (int) (totalAmountOfMilk / 3.78);
    System.out.println(numberOfMilkCartons);

    System.out.println("The cost of producing one liter of milk:");
    double costOfProducingOneLiterOfMilk = totalAmountOfMilk * 0.38;
    System.out.println(costOfProducingOneLiterOfMilk);

    System.out.println("The output of the profit for producing milk:");
    double profitForProducingMilk = numberOfMilkCartons * 0.27;
    System.out.println(profitForProducingMilk);
}
}
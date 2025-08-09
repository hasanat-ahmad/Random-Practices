import java.util.Scanner;

public class SummerJob {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Enter the pay rate per hour: $");
        double payRate = scanner.nextDouble();
        System.out.print("Enter the number of hours worked per week: ");
        int hoursPerWeek = scanner.nextInt();

        double incomeBeforeTaxes = payRate * hoursPerWeek * 5;
        double taxRate = 0.14;
        double incomeAfterTaxes = incomeBeforeTaxes * (1 - taxRate);
        double clothesAndAccessories = 0.10 * incomeAfterTaxes;
        double schoolSupplies = 0.01 * incomeAfterTaxes;
        double savingsBonds = 0.25 * (incomeAfterTaxes - clothesAndAccessories - schoolSupplies);
        double parentsSavingsBonds = 0.50 * savingsBonds;

        System.out.println("Income before taxes: $" + incomeBeforeTaxes);
        System.out.println("Income after taxes: $" + incomeAfterTaxes);
        System.out.println("Money spent on clothes and accessories: $" + clothesAndAccessories);
        System.out.println("Money spent on school supplies: $" + schoolSupplies);
        System.out.println("Money spent to buy savings bonds: $" + savingsBonds);
        System.out.println("Money parents spend on additional savings bonds: $" + parentsSavingsBonds);

    }
}

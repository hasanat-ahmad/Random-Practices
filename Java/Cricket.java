import java.util.Scanner;

public class Cricket {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        double classAPrice = 20.0;
        double classBPrice = 15.0;
        double classCPrice = 10.0;
        double classDPrice = 5.0;

        System.out.print("Enter the number of Class A tickets sold: ");
        int classATickets = scanner.nextInt();
        System.out.print("Enter the number of Class B tickets sold: ");
        int classBTickets = scanner.nextInt();
        System.out.print("Enter the number of Class C tickets sold: ");
        int classCTickets = scanner.nextInt();
        System.out.print("Enter the number of Class D tickets sold: ");
        int classDTickets = scanner.nextInt();
        double totalIncome = (classAPrice * classATickets) + (classBPrice * classBTickets) +
                            (classCPrice * classCTickets) + (classDPrice * classDTickets);

        System.out.println("Total income generated: $" + totalIncome);
        System.out.println("Income corresponding to ticket sales:");
        System.out.println("Class A: $" + (classAPrice * classATickets));
        System.out.println("Class B: $" + (classBPrice * classBTickets));
        System.out.println("Class C: $" + (classCPrice * classCTickets));
        System.out.println("Class D: $" + (classDPrice * classDTickets));

    }
}

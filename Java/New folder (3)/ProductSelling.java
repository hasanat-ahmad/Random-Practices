// import java.util.Scanner;
// public class ProductSelling {
//     public static void main(String[] args) {

//         // Entering entities
//         double Product_1 = 2.98;
//         double Product_2 = 4.50;
//         double Product_3 = 9.98;
//         double Product_4 = 4.49;
//         double Product_5 = 6.87;
//         // Input
//         Scanner sc = new Scanner(System.in);
//         System.out.print("Enter the ID of Product: ");
//         double Product_ID = sc.nextDouble();
//         System.out.print("Enter the number of Product sold: ");
//         double NumberSold = sc.nextDouble();

//         // Calculation
//         if (Product_ID == 1){
//             double Sold = Product_1*NumberSold;
//             System.out.println("The total profit is: " + "$"+ Sold);
//         }
//         else if (Product_ID == 2){
//             double Sold = Product_2*NumberSold;
//             System.out.println("The total profit is: " + "$"+Sold);
//         }
//         else if (Product_ID == 3){
//             double Sold = Product_3*NumberSold;
//             System.out.println("The total profit is: " +"$"+ Sold);
//         }
//         else if (Product_ID == 4){
//             double Sold = Product_4*NumberSold;
//             System.out.println("The total profit is: " + "$" +Sold);
//         }
//         else if (Product_ID == 5){
//             double Sold = Product_5*NumberSold;
//             System.out.println("The total profit is: " + "$" +Sold);
//         }
//         else if (Product_ID == -99){
//             System.out.println("Exiting the loop");
            
//         }
//     }
// }


import java.util.Scanner;

public class ProductSelling {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        double[] prices = {2.98, 4.50, 9.98, 4.49, 6.87};
        double totalRetailValue = 0;
        int productNumber;
        int quantitySold;

        System.out.println("Enter product number (1-5) and quantity sold (or -99 to finish):");

        while (true) {
            System.out.print("Product number: ");
            productNumber = input.nextInt();
            if (productNumber == -99) {
                break;
            }

            if (productNumber >= 1 && productNumber <= 5) {
                System.out.print("Quantity sold: ");
                quantitySold = input.nextInt();
                
                if (quantitySold < 0) {
                    System.out.println("Invalid quantity. Please enter a non-negative value.");
                    continue;
                }
                
                totalRetailValue += prices[productNumber - 1] * quantitySold;
            } else {
                System.out.println("Invalid product number. Please try again.");
            }
        }

        System.out.printf("Total retail value of all products sold: $%.2f%n", totalRetailValue);
        input.close();
    }
}


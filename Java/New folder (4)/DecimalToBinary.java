// import java.util.Scanner;

// public class DecimalToBinary {

//     public static void main(String[] args) {
//         Scanner sc = new Scanner(System.in);
//         int decimalNumber = sc.nextInt();
        
//         String a = "";
//         while (decimalNumber != 0){
//             int remainder = decimalNumber % 2;
//             decimalNumber = decimalNumber / 2;
//             a += Integer.toString(remainder);
            
//         }

import java.util.Scanner;

public class DecimalToBinary {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int decimalNumber = sc.nextInt();
        
        if (decimalNumber == 0) {
            System.out.println("0");
            return;
        }
        
        String binary = "";
        while (decimalNumber != 0) {
            int remainder = decimalNumber % 2;
            decimalNumber = decimalNumber / 2;
            binary =  binary+remainder ;  // Prepend remainder
        }

        System.out.println(binary);
    }
}

        

//         System.out.println(a);
//     }
// }
import java.util.Scanner;

public class Calculator {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        
        
        while (true) {
            System.out.println("Enter 2 numbers: ");
            float num1 = sc.nextFloat();
            float num2 = sc.nextFloat();
            System.out.println("Enter the operator[+,-,*,/,%] or X to quit: ");
            char operator = sc.next().trim().charAt(0);
            if (operator == '+'){
                System.out.println(num1+num2);
                
            }
            else if (operator == '-'){
                System.out.println(num1-num2);
                
            }
            else if (operator == '*'){
                System.out.println(num1*num2);
                
            }
            else if (operator == '/'){
                if (num2 != 0){
                System.out.println(num1/num2);
                
                }
                else{System.out.println("Undefined");}
                
            } 
            else if (operator == '%'){
                System.out.println(num1%num2);
                
            }
            else if(operator == 'X' || operator == 'x'){
                System.out.println("Exiting the loop");
                break;   
            }
            else{
                System.out.println("Wrong operator!");
            }
        }
    }
}

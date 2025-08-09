public class TASK_4_D {
    public static void main(String[] args) {
        int num1 = 5;
        int num2 = 3;
        int num3 = 7;
        
        int min = Math.min(Math.min(num1, num2), num3);
        
        System.out.println("Minimum: " + min);
    }
}
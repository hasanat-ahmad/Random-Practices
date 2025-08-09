public class TASK_4_C {
    public static void main(String[] args) {
        int X = -5;
        int sign;
        
        if (X > 0) {
            sign = 1;
        } else if (X < 0) {
            sign = -1;
        } else {
            sign = 0;
        }
        
        System.out.println("Sign: " + sign);
    }
}
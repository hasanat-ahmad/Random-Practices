public class Recursion {
    public static void recursion(int a){
        if (a == 0){
            return;
            
        }
        
        recursion(a - 1);
        System.out.println(a);
    }
    public static void main(String[] args) {
        recursion(10);
    }
}

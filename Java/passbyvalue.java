public class passbyvalue {
    public static void increment(int number){
        number++;
        System.out.println(number);
    }
    public static void main(String[] args) {
        int number = 10;
        increment(number);
        System.out.println(number);
    }
}

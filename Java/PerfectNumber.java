public class PerfectNumber {
    public static void main(String[] args) {
        int sum = 0;
        for ( int i = 1 ; i <= 10000 ; i++){
            for (int j = 1 ; j <= i ; j++){
                if ( i % j == 0){
                    sum = sum + j ;
                }
            }
            // if ( i == sum ){
            //     System.out.println("This " + i + " is a perfect number. ");
            }
        System.out.println(sum);
        }
    }


public class Question1 {
    
        public static void main(String[] args) {
            
                    int limit = 10000; 
                    
                    System.out.println("Perfect numbers up to " + limit + ":");
                    for (int i = 1; i <= limit; i++) {
                        if (isPerfectNumber(i)) {
                            System.out.println(i);
                        }
                    }
                }
            
                public static boolean isPerfectNumber(int num) {
                    int sum = 0;
                    for (int i = 1; i <= num / 2; i++) {
                        if (num % i == 0) {
                            sum += i;
                        }
                    }
                    return sum == num;
        }
    }

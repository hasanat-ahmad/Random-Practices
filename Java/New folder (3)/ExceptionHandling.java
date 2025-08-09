public class ExceptionHandling {
    public static void main(String[] args) {
        try{
            int a = 5;
            int b = 5;
            int answer = a/b;
            System.out.println(answer);
        }
        catch(Exception e){
            System.out.println("Can't divide a number by 0");
        }

        int[] arr = new int[3];
        arr[0] = 1;
        arr[1] = 5;
        arr[2] = 9;
        try {
            System.out.println(arr[9]);
        } catch (Exception e) {
            System.out.println("Index not found");
        }
    }
}

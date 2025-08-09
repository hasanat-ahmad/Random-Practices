import java.util.Arrays;

public class PassByRef {
    static void changeValue(int[] x){
        x[4] = 10;
    } 
    public static void main(String[] args) {
        int[] arr = {1,2,3,4,5};
        changeValue(arr);
        System.out.println(Arrays.toString(arr));
    }
}

import java.util.Arrays;

public class ForEach {
    public static void main(String[] args) {
        String[][] arr = {{"Ahmad", "Hasnat", "Mohsin"}, {"Ahmad", "Hasnat", "Mohsin"}, {"Ahmad", "Hasnat", "Mohsin"}};
        for (String[] name : arr) {
            for (String element : name){
            System.out.println(element);
        }
        }

        String[] arr2 = new String[]{"Ahmad" + "-" + "052", "Hasnat-88"};
        System.out.println(Arrays.toString(arr2));
    }
}

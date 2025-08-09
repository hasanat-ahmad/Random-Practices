public class FindingMax {

    public static void main(String[] args) {
        int a = 100;
        int b = 70;
        int c = 30;
        int max = a < b ? a : b;
        int finalmax = c < max ? c : max;
        System.out.println(finalmax);
    }
}
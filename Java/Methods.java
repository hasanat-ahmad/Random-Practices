public class Methods {
    public static void middle(String a1) {
        int length = a1.length();
        int middleIndex = length / 2;

        // Check if the length is odd
        if (length % 2 == 1) {
            // Print the middle character
            System.out.println(a1.charAt(middleIndex));
        } else {
            // Print the two middle characters
            System.out.print(a1.charAt(middleIndex - 1));
            System.out.println(a1.charAt(middleIndex));
        }
    }

    public static void main(String[] args) {
        middle("ABC");
        middle("ABCD");
    }
}

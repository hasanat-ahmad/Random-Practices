public class question2 {
    public static void main(String[] args) {
        String input = "this is a test sentence";
        System.out.println(capitalizeWords(input));
    }

    public static String capitalize(String lowerCaseWord) {
        if (lowerCaseWord == null || lowerCaseWord.isEmpty()) {
            return lowerCaseWord;
        }
        return Character.toUpperCase(lowerCaseWord.charAt(0)) + lowerCaseWord.substring(1);
    }

    public static String capitalizeWords(String sentence) {
        if (sentence == null || sentence.isEmpty()) {
            return sentence;
        }

        String[] words = sentence.split(" ");
        StringBuilder result = new StringBuilder();

        for (String word : words) {
            result.append(capitalize(word)).append(" ");
        }

        return result.toString().trim(); // remove trailing space
    }
}

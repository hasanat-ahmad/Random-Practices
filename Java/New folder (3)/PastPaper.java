import java.io.FileWriter;
import java.io.IOException;
import java.util.Scanner;

public class PastPaper {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        System.out.print("Enter your first name: ");
        String firstName = scanner.nextLine();

        System.out.print("Enter your registration number: ");
        String regNumber = scanner.nextLine();
        
        String[][] raggedArray = new String[1][];
        raggedArray[0] = new String[]{firstName + "-" + regNumber};

        
        writeToFile(raggedArray);                                                               

        
        scanner.close();
    }

    
    public static void writeToFile(String[][] raggedArray) {
        FileWriter writer = null;
        try {
            writer = new FileWriter("output.txt");
            for (String[] row : raggedArray) {
                for (String element : row) {
                    writer.write(element);
                    writer.write(System.lineSeparator());
                    writer.close();
                }
            }
            System.out.println("Data successfully written to output.txt");
        } catch (IOException e) {
            System.err.println("Error writing to file: " + e.getMessage());
        // } finally {
        //     if (writer != null) {
        //         try {
        //             writer.close();
        //         } catch (IOException e) {
        //             System.err.println("Error closing the writer: " + e.getMessage());
        //         }
        //     }
        }
    }
}

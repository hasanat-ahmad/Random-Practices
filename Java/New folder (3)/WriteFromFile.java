import java.io.FileWriter;
import java.io.IOException;

public class WriteFromFile {
    public static void main(String[] args) {
        try {
            FileWriter WriteFile = new FileWriter("D:\\CUI\\File.txt");
            WriteFile.write("Hi BCS-2B. File handling in Java implies reading from and writing data to a file. The File class from the java.io package, allows us to work with different formats of files. In order to use the File class, you need to create an object of the class and specify the filename or directory name.");
            WriteFile.close();
            System.out.println("Successfully wrote to the file");
        } catch (IOException e) {
            System.out.println("An error occured");
        }
        
    }
}

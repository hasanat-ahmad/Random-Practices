import java.io.File;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.util.Scanner;

public class ReadFromFile {
    public static void main(String[] args) throws IOException {
        File ReadFile = new File("D:\\CUI\\File.txt");
        
            try {
                Scanner sc = new Scanner(ReadFile);
                String data = sc.nextLine();
                System.out.println(data);
            
            } catch (FileNotFoundException e) {
                e.printStackTrace();
            }
            

    }
}

import java.io.File;
import java.io.FileWriter;

public class FileHandling {
    public static void main(String[] args) {
        try {
            File file = new File("C:\\merged_partition_content\\Code\\Java\\haseeb.txt");
            if (file.createNewFile()){
                System.out.println("File created");
                System.out.println(file.getAbsolutePath());
                System.out.println(file.getName());
                System.out.println(file.length());
                System.out.println(file.canRead());
                System.out.println(file.canWrite());
            }
        } catch (Exception e) {
            System.out.println("Could not make file");
        }
        try {
            FileWriter fileWriter = new FileWriter("C:\\merged_partition_content\\Code\\Java\\haseeb.txt");
            fileWriter.write("I am a Haseeb. I am a first semester software engineering student");
            fileWriter.close();
        } catch (Exception e) {
            System.out.println("ABC");
        }
    }
}

import java.io.File;
import java.io.IOException;

public class CreateFileAndGetInformation {

    public static void main(String[] args) throws IOException {
        File My_File = new File("D:\\CUI\\File.txt");
        My_File.createNewFile();
        if (My_File.exists()){
            System.out.println("Name: " + My_File.getName());
            System.out.println("Path: " + My_File.getAbsolutePath());
            System.out.println("Is readable: " + My_File.canRead());
            System.out.println("Is Writable: " + My_File.canWrite());
            System.out.println("Size: " + My_File.length());
        }
        throw new IndexOutOfBoundsException("Run nahi hwa");

    }
}
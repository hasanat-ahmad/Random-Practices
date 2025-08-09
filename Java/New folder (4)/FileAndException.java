import java.io.*;
import java.util.ArrayList;
import java.util.Scanner;

public class FileAndException {

    public static void main(String[] args) {
        // Prompt user for file name
        Scanner input = new Scanner(System.in);
        System.out.print("Enter the filename: ");
        String filename = input.nextLine();

        ArrayList<Double> scores = new ArrayList<>();
        int totalStudents = 0;
        double totalScore = 0.0;

        // Read from file
        try (BufferedReader br = new BufferedReader(new FileReader(filename))) {
            String line;
            while ((line = br.readLine()) != null) {
                // Split the line by space to get ID and score
                String[] parts = line.split("\\s+");
                if (parts.length == 2) {
                    double score = Double.parseDouble(parts[1]);
                    scores.add(score);
                    totalScore += score;
                    totalStudents++;
                }
            }
        } catch (FileNotFoundException e) {
            System.out.println("File not found: " + e.getMessage());
            return;
        } catch (IOException e) {
            System.out.println("Error reading file: " + e.getMessage());
            return;
        } catch (NumberFormatException e) {
            System.out.println("Error parsing score: " + e.getMessage());
            return;
        }

        // Calculate average
        double averageScore = totalScore / totalStudents;

        // Count students with score above average
        int aboveAverageCount = 0;
        for (double score : scores) {
            if (score > averageScore) {
                aboveAverageCount++;
            }
        }

        // Print results to console
        System.out.println("Total number of students: " + totalStudents);
        System.out.println("Average score: " + averageScore);
        System.out.println("Number of students above average: " + aboveAverageCount);

        // Write results to AvgScore.txt
        try (PrintWriter writer = new PrintWriter(new FileWriter("AvgScore.txt"))) {
            writer.println("Total number of students: " + totalStudents);
            writer.println("Average score: " + averageScore);
            writer.println("Number of students above average: " + aboveAverageCount);
        } catch (IOException e) {
            System.out.println("Error writing to file: " + e.getMessage());
        }
    }
}

import java.util.Scanner;

public class StudentMarks {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int[][] marks = new int[3][3];
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                marks[i][j] = sc.nextInt();
            }
        }
        int marksOfStudent_1 = 0;
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                if (i == 0) {
                    marksOfStudent_1 = marksOfStudent_1 + marks[0][j];
                    
                    }
            
            }

        }
        
        int marksOfStudent_2 = 0;
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                if (i == 1) {
                    marksOfStudent_2 = marksOfStudent_2 + marks[1][j];
                    
                    }
            
            }

        }
        
        int marksOfStudent_3 = 0;
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                if (i == 2) {
                    marksOfStudent_3 = marksOfStudent_3 + marks[2][j];
                    
                    }
            
            }

        }
        System.out.println("Total marks of student 1 are " + marksOfStudent_1);
        System.out.println("Total marks of student 2 are " + marksOfStudent_2);
        System.out.println("Total marks of student 3 are " + marksOfStudent_3);
    }
}

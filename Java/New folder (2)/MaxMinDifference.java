import java.util.Scanner;

public class MaxMinDifference {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // Prompting the user to enter the number of elements in the array
        System.out.print("Enter the number of elements in the array: ");
        int n = scanner.nextInt();

        // Creating an array of size n
        int[] arr = new int[n];

        // Prompting the user to enter the elements of the array
        System.out.println("Enter the elements of the array:");
        for (int i = 0; i < n; i++) {
            arr[i] = scanner.nextInt();
        }

        // Finding the pairs with maximum and minimum difference
        int maxDiff = Integer.MIN_VALUE;
        int minDiff = Integer.MAX_VALUE;
        int maxDiffPair1 = 0, maxDiffPair2 = 0;
        int minDiffPair1 = 0, minDiffPair2 = 0;

        for (int i = 0; i < n - 1; i++) {
            for (int j = i + 1; j < n; j++) {
                int diff = Math.abs(arr[i] - arr[j]);
                if (diff > maxDiff) {
                    maxDiff = diff;
                    maxDiffPair1 = arr[i];
                    maxDiffPair2 = arr[j];
                }
                if (diff < minDiff) {
                    minDiff = diff;
                    minDiffPair1 = arr[i];
                    minDiffPair2 = arr[j];
                }
            }
        }

        // Displaying the pairs with maximum and minimum difference
        System.out.println("Pair with maximum difference: (" + maxDiffPair1 + ", " + maxDiffPair2 + ")");
        System.out.println("Maximum Difference: " + maxDiff);
        System.out.println("Pair with minimum difference: (" + minDiffPair1 + ", " + minDiffPair2 + ")");
        System.out.println("Minimum Difference: " + minDiff);
    }
}

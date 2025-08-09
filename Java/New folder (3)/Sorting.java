public class Sorting {

    public static void main(String[] args) {
        int[] arr = {3,5,6,8,2};
        BubbleSorting(arr);
        PrintArray(arr);
    }
    public static void BubbleSorting(int arr[]){
        for (int i = 0; i < arr.length-1; i++) {
            for (int j = 0; j < arr.length-i-1; j++) {
                if (arr[j] > arr[j+1]){
                    int temp = arr[j];
                    arr[j] = arr[j+1];
                    arr[j+1] = temp;
                }
            }
        }
    }
    public static void PrintArray(int arr[]){
        System.out.print("The sorted array is ");
        for (int i = 0; i < arr.length; i++) {
            System.out.print(arr[i] + " ");
        }
    }
}



    

import java.util.Random;
import java.util.Scanner;

public class LabMid {
    public static void main(String[] args) {

        String[] ranks = {"Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"};
        String[] suits = {"Clubs", "Diamonds", "Hearts", "Spades"};

        Random random = new Random();

        String pickedRank = ranks[random.nextInt(ranks.length)];
        String pickedSuit = suits[random.nextInt(suits.length)];

        System.out.println("The card you picked is " + pickedRank + " of " + pickedSuit + ".");
    }
}

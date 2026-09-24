// Задача #2: тот же конвертер + структура выбора для окончаний валюты (юань/юаня/юаней)
import java.util.Scanner;

public class Converter {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        final double ROUBLES_PER_YUAN = 11.91;

        System.out.println("Сколько юаней у вас осталось после путешествия?");
        int yuan = input.nextInt();

        double roubles = ROUBLES_PER_YUAN * yuan;

        int last2 = yuan % 100;  
        int digit = yuan % 10;   

        String ending;
        if (last2 >= 11 && last2 <= 14) {   // 11..14 — исключение, проверяем первым
            ending = "юаней";
        } else if (digit == 1) {
            ending = "юань";
        } else if (digit >= 2 && digit <= 4) {
            ending = "юаня";
        } else {
            ending = "юаней";
        }

        System.out.println("У вас " + yuan + " " + ending + " = " + roubles + " рублей");
    }
}

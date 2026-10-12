// Задача #1: конвертация суммы из китайских юаней в рубли по курсу 11.91
import java.util.Scanner;

public class ConverterYuan {
    public static void main(String[] args) {
    	Scanner input = new Scanner(System.in);
        double k = 11.91;
        System.out.println("Сколько юаней у вас осталось после путешествия?");
        double rub = input.nextDouble();

        System.out.print("У вас " + k*rub + " рублей");
    }
}

// Задание 1 (исключения): два массива, ввод числа 1..12, перехват ArrayIndexOutOfBoundsException
import java.util.InputMismatchException;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        String[] months = {"январь", "февраль", "март", "апрель", "май",
                "июнь", "июль", "август", "сентябрь", "октябрь", "ноябрь", "декабрь"};
        int[] dom = {31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};

        Scanner input = new Scanner(System.in);

        while (true) {                     // повторяем, пока не введут корректное число
            System.out.print("Введите номер месяца (1-12): ");
            try {
                int n = input.nextInt();
                System.out.println(months[n - 1] + " — " + dom[n - 1] + " дней");
                break;                     // получилось — выходим из цикла
            } catch (ArrayIndexOutOfBoundsException e) {
                System.out.println("Недопустимое число");
            } catch (InputMismatchException e) {
                System.out.println("Нужно ввести целое число");
                input.next();              // убираем неверный ввод из потока
            }
        }
    }
}

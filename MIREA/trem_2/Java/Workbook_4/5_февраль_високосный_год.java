// Задание 2 (исключения): ввод года для февраля, метод проверки високосного года
import java.util.InputMismatchException;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        String[] months = {"январь", "февраль", "март", "апрель", "май",
                "июнь", "июль", "август", "сентябрь", "октябрь", "ноябрь", "декабрь"};
        int[] dom = {31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};

        Scanner input = new Scanner(System.in);

        while (true) {
            System.out.print("Введите номер месяца (1-12): ");
            try {
                int n = input.nextInt();
                int days = dom[n - 1];
                String name = months[n - 1];

                if (n == 2) {                       // февраль — спрашиваем год
                    System.out.print("Введите год: ");
                    int year = input.nextInt();
                    if (isLeapYear(year)) {
                        days = 29;
                    }
                    System.out.println(name + " " + year + " года — " + days + " дней");
                } else {
                    System.out.println(name + " — " + days + " дней");
                }
                break;
            } catch (ArrayIndexOutOfBoundsException e) {
                System.out.println("Недопустимое число");
            } catch (InputMismatchException e) {
                System.out.println("Нужно ввести целое число");
                input.next();
            }
        }
    }

    /** Високосный: делится на 4, но не на 100; либо делится на 400 */
    public static boolean isLeapYear(int year) {
        return (year % 4 == 0 && year % 100 != 0) || year % 400 == 0;
    }
}

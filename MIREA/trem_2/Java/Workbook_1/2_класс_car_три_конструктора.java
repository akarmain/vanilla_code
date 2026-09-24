// Задача #1 (ООП): класс Car с полями model, license, color, year и тремя конструкторами
public class Car {
 public static void main(String[] args) {
        Car a = new Car();
        Car b = new Car("Lada Vesta", "А123ВС777", "белый", 2021);
        Car c = new Car("Kia Rio", 2018);

        System.out.println("b: " + b.model + " " + b.license + " " + b.color + " " + b.year);
        System.out.println("C: " + c.model + " " + c.year);
        System.out.println("A: "+a.model + " " + a.year); 
    }
    String model;    // модель
    String license;  // номер
    String color;    // цвет
    int year;        // год выпуска

    public Car() {                  
    }

    public Car(String model, String license, String color, int year) { 
        this.model = model;          
        this.license = license;
        this.color = color;
        this.year = year;
    }

    public Car(String model, int year) {
        this.model = model;
        this.year = year;
    }
}

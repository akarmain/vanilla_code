// Задача #2 (ООП): класс Main, объекты через разные конструкторы, To_String(), геттеры/сеттеры, возраст авто
public class Main {
    public static void main(String[] args) {
        Car a = new Car();
        Car b = new Car("Lada Vesta", "А123ВС777", "белый", 2021);
        Car c = new Car("Kia Rio", 2018);

        System.out.println("b: " + b.To_String());
        System.out.println("C: " + c.To_String());

        a.setModel("Renault Logan");
        a.setLicense("В456ЕК99");
        a.setColor("синий");
        a.setYear(2015);
        System.out.println("a: " + a.To_String());

        System.out.println("A (Возраст " + a.getModel() + ": " + a.getAge() + " лет)");
    }
}

class Car {
    private static final int CURRENT_YEAR = 2026; 

    private String model;
    private String license;
    private String color;
    private int year;

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

    public String getModel() { return model; }
    public void setModel(String model) { this.model = model; }

    public String getLicense() { return license; }
    public void setLicense(String license) { this.license = license; }

    public String getColor() { return color; }
    public void setColor(String color) { this.color = color; }

    public int getYear() { return year; }
    public void setYear(int year) { this.year = year; }

    public int getAge() {
        return CURRENT_YEAR - year;
    }

    public String To_String() {
        return "Car {модель=" + model + ", номер=" + license
             + ", цвет=" + color + ", год=" + year + "}";
    }
}

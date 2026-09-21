// Часть 1. Задача #1: пакеты vehicles и app, private ownerName/insuranceNumber, protected engineType
// Пакеты vehicles/app здесь показаны комментариями: всё решение лежит в одном файле.
public class Main {  // это app.Main
    public static void main(String[] args) {
        Car car = new Car("Lada Vesta", "А123ВС777", "белый", 2021);

        car.setOwnerName("Иванов И.И.");        // к private-полям — только через сеттеры
        car.setInsuranceNumber("ОСАГО-778899");
        car.setEngineType("Combustion");

        System.out.println("Владелец: " + car.getOwnerName());
        System.out.println("Страховка: " + car.getInsuranceNumber());
        System.out.println("Двигатель: " + car.getEngineType());
        // car.ownerName — так нельзя: поле private
    }
}

class Car {  // это vehicles.Car
    String model;
    String license;
    String color;
    int year;

    private String ownerName;        // виден только внутри класса Car
    private String insuranceNumber;
    protected String engineType;     // виден ещё и наследникам

    public Car() {
    }

    public Car(String model, String license, String color, int year) {
        this.model = model;
        this.license = license;
        this.color = color;
        this.year = year;
    }

    public String getOwnerName() { return ownerName; }
    public void setOwnerName(String ownerName) { this.ownerName = ownerName; }

    public String getInsuranceNumber() { return insuranceNumber; }
    public void setInsuranceNumber(String insuranceNumber) { this.insuranceNumber = insuranceNumber; }

    public String getEngineType() { return engineType; }
    public void setEngineType(String engineType) { this.engineType = engineType; }
}

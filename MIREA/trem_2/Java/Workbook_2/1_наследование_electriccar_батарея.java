// Часть 1. Задача #2: ElectricCar наследует Car, поле batteryCapacity, engineType = Electric
public class Main {
    public static void main(String[] args) {
        Car car = new Car("Lada Vesta", "А123ВС777", "белый", 2021);
        car.setOwnerName("Иванов И.И.");
        car.setEngineType("Combustion");

        ElectricCar tesla = new ElectricCar("Tesla Model 3", "Е777ЛК77", "красный", 2023, 75.0);
        tesla.setOwnerName("Петров П.П.");

        System.out.println(car.getOwnerName() + ", двигатель " + car.getEngineType());
        System.out.println(tesla.getOwnerName() + ", двигатель " + tesla.getEngineType()
                         + ", батарея " + tesla.getBatteryCapacity() + " кВт*ч");
    }
}

class Car {
    String model;
    String license;
    String color;
    int year;

    private String ownerName;
    private String insuranceNumber;
    protected String engineType;

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

class ElectricCar extends Car {  
    private double batteryCapacity;

    public ElectricCar(String model, String license, String color, int year, double batteryCapacity) {
        super(model, license, color, year);  // вызов конструктора родителя
        this.batteryCapacity = batteryCapacity;
        this.engineType = "Electric";        // protected-поле доступно наследнику напрямую
    }

    public double getBatteryCapacity() { return batteryCapacity; }
    public void setBatteryCapacity(double batteryCapacity) { this.batteryCapacity = batteryCapacity; }
}

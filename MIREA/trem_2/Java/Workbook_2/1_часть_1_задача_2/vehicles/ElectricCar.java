package vehicles;

public class ElectricCar extends Car {
    private double batteryCapacity;

    public ElectricCar(String model, String license, String color, int year, double batteryCapacity) {
        super(model, license, color, year);  // вызов конструктора родителя
        this.batteryCapacity = batteryCapacity;
        this.engineType = "Electric";        // protected-поле доступно наследнику напрямую
    }

    public double getBatteryCapacity() { return batteryCapacity; }
    public void setBatteryCapacity(double batteryCapacity) { this.batteryCapacity = batteryCapacity; }
}

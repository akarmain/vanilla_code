package vehicles;

public class ElectricCar extends Car implements ElectricVehicle {  // наследует класс + реализует интерфейс
    private double batteryCapacity;

    public ElectricCar(String model, String license, String color, int year, double batteryCapacity) {
        super(model, license, color, year);
        this.batteryCapacity = batteryCapacity;
        setEngineType("Electric");
    }

    @Override
    public double getBatteryCapacity() { return batteryCapacity; }

    @Override
    public void setBatteryCapacity(double batteryCapacity) { this.batteryCapacity = batteryCapacity; }

    @Override
    public String vehicleType() { return "Electric Car"; }

    @Override
    public String toString() {
        return super.toString() + ", батарея " + batteryCapacity + " кВт*ч";
    }
}

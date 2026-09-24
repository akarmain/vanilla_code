// Часть 1. Задача #2: ElectricCar наследует Car, поле batteryCapacity, engineType = Electric
package app;

import vehicles.Car;
import vehicles.ElectricCar;

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

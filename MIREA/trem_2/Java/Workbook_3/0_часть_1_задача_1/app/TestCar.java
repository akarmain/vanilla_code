package app;

import vehicles.Car;
import vehicles.ElectricCar;

public class TestCar {
    public static void main(String[] args) {
        Car car = new Car("Lada Vesta", "А123ВС777", "белый", 2021);
        ElectricCar tesla = new ElectricCar("Tesla Model 3", "Е777ЛК77", "красный", 2023, 75.0);

        car.setYear(2022);                          // изменение года выпуска
        car.setOwnerName("Иванов И.И.");            // изменение владельца
        car.setInsuranceNumber("ОСАГО-445566");
        tesla.setOwnerName("Петров П.П.");
        tesla.setInsuranceNumber("ОСАГО-112233");   // изменение страхового номера

        System.out.println("Ёмкость батареи: " + tesla.getBatteryCapacity() + " кВт*ч");

        System.out.println(car);
        System.out.println(tesla);
    }
}

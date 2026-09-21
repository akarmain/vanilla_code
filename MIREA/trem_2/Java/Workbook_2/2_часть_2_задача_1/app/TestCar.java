// Часть 2. Задача #1: полиморфизм в тестовом классе
package app;

import vehicles.Car;
import vehicles.ElectricCar;
import vehicles.Vehicle;

public class TestCar {
    public static void main(String[] args) {
        Vehicle[] garage = {                                   // полиморфизм: в массиве родителя
            new Car("Lada Vesta", "А123ВС777", "белый", 2021),  // лежат объекты наследников
            new ElectricCar("Tesla Model 3", "Е777ЛК77", "красный", 2023, 75.0)
        };

        garage[0].setOwnerName("Иванов И.И.");
        garage[0].setYear(2022);
        garage[1].setOwnerName("Петров П.П.");
        garage[1].setInsuranceNumber("ОСАГО-112233");

        for (Vehicle v : garage) {
            System.out.println(v.vehicleType() + " -> " + v);  
        }
    }
}

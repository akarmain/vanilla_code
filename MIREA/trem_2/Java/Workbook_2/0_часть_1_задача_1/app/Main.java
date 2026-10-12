// Часть 1. Задача #1: пакеты vehicles и app, private ownerName/insuranceNumber, protected engineType
package app;

import vehicles.Car;

public class Main {
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

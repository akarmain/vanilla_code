// Задание №1: класс Triangle от GeometricObject, getArea(), getPerimeter(), toString()
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        System.out.print("Введите три стороны треугольника: ");
        double s1 = input.nextDouble();
        double s2 = input.nextDouble();
        double s3 = input.nextDouble();

        System.out.print("Введите цвет: ");
        String color = input.next();

        System.out.print("Треугольник закрашен (true/false)? ");
        boolean filled = input.nextBoolean();

        Triangle t = new Triangle(s1, s2, s3);
        t.setColor(color);
        t.setFilled(filled);

        System.out.println(t);
        System.out.println("Площадь: " + t.getArea());
        System.out.println("Периметр: " + t.getPerimeter());
        System.out.println("Цвет: " + t.getColor());
        System.out.println("Закрашен: " + t.isFilled());
    }
}

class GeometricObject {
    private String color = "белый";
    private boolean filled;

    public GeometricObject() {
    }

    public String getColor() { return color; }
    public void setColor(String color) { this.color = color; }

    public boolean isFilled() { return filled; }
    public void setFilled(boolean filled) { this.filled = filled; }
}

class Triangle extends GeometricObject {
    private double side1 = 1.0;
    private double side2 = 1.0;
    private double side3 = 1.0;

    public Triangle() {                 // безаргументный: стороны по умолчанию 1.0
    }

    public Triangle(double side1, double side2, double side3) {
        this.side1 = side1;
        this.side2 = side2;
        this.side3 = side3;
    }

    public double getSide1() { return side1; }
    public double getSide2() { return side2; }
    public double getSide3() { return side3; }

    public double getPerimeter() {
        return side1 + side2 + side3;
    }

    public double getArea() {                       // формула Герона
        double s = getPerimeter() / 2;              // полупериметр
        return Math.sqrt(s * (s - side1) * (s - side2) * (s - side3));
    }

    @Override
    public String toString() {
        return "Треугольник: сторона1 = " + side1 + " сторона2 = " + side2 + " сторона3 = " + side3;
    }
}

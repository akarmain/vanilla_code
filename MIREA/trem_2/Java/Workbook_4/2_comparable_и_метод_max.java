// Задание №3: GeometricObject реализует Comparable, статический max(), ComparableCircle
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        System.out.print("Введите три стороны треугольника: ");
        Triangle t = new Triangle(input.nextDouble(), input.nextDouble(), input.nextDouble());
        System.out.print("Введите цвет: ");
        t.setColor(input.next());
        System.out.print("Закрашен (true/false)? ");
        t.setFilled(input.nextBoolean());

        System.out.println(t);
        System.out.println("Площадь " + t.getArea() + ", периметр " + t.getPerimeter()
                         + ", цвет " + t.getColor() + ", закрашен " + t.isFilled());

        Circle c1 = new Circle(2), c2 = new Circle(5);
        Rectangle r1 = new Rectangle(2, 3), r2 = new Rectangle(4, 4);

        System.out.println("Больший круг: " + GeometricObject.max(c1, c2));
        System.out.println("Больший прямоугольник: " + GeometricObject.max(r1, r2));

        ComparableCircle cc1 = new ComparableCircle(1), cc2 = new ComparableCircle(7);
        System.out.println("Больший ComparableCircle: "
            + (cc1.compareTo(cc2) > 0 ? cc1 : cc2));
        System.out.println("Круг против прямоугольника: "
            + (cc2.compareTo(r2) > 0 ? cc2 : r2));
    }
}

abstract class GeometricObject implements Comparable<GeometricObject> {
    private String color = "белый";
    private boolean filled;

    public String getColor() { return color; }
    public void setColor(String color) { this.color = color; }

    public boolean isFilled() { return filled; }
    public void setFilled(boolean filled) { this.filled = filled; }

    public abstract double getArea();

    @Override
    public int compareTo(GeometricObject other) {          // сравнение по площади
        return Double.compare(this.getArea(), other.getArea());
    }

    public static GeometricObject max(GeometricObject a, GeometricObject b) {
        return a.compareTo(b) >= 0 ? a : b;
    }
}

class Circle extends GeometricObject {
    private double radius;

    public Circle(double radius) { this.radius = radius; }

    public double getRadius() { return radius; }

    @Override
    public double getArea() { return Math.PI * radius * radius; }

    @Override
    public String toString() { return "Круг r=" + radius + " (площадь " + getArea() + ")"; }
}

class ComparableCircle extends Circle {
    public ComparableCircle(double radius) { super(radius); }

    @Override
    public String toString() { return "ComparableCircle r=" + getRadius() + " (площадь " + getArea() + ")"; }
}

class Rectangle extends GeometricObject {
    private double width;
    private double height;

    public Rectangle(double width, double height) {
        this.width = width;
        this.height = height;
    }

    @Override
    public double getArea() { return width * height; }

    @Override
    public String toString() { return "Прямоугольник " + width + "x" + height + " (площадь " + getArea() + ")"; }
}

class Triangle extends GeometricObject {
    private double side1 = 1.0, side2 = 1.0, side3 = 1.0;

    public Triangle() { }

    public Triangle(double side1, double side2, double side3) {
        this.side1 = side1;
        this.side2 = side2;
        this.side3 = side3;
    }

    public double getPerimeter() { return side1 + side2 + side3; }

    @Override
    public double getArea() {
        double s = getPerimeter() / 2;
        return Math.sqrt(s * (s - side1) * (s - side2) * (s - side3));
    }

    @Override
    public String toString() {
        return "Треугольник: сторона1 = " + side1 + " сторона2 = " + side2 + " сторона3 = " + side3;
    }
}

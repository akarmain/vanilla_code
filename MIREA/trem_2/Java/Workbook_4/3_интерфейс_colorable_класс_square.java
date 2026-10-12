// Задание №4: интерфейс Colorable с howToColor(), класс Square, массив из пяти GeometricObject
public class Main {
    public static void main(String[] args) {
        GeometricObject[] objects = {
            new Square(3),
            new Circle(2),
            new Square(1.5),
            new Rectangle(2, 5),
            new Circle(4)
        };

        for (GeometricObject o : objects) {
            System.out.println(o + ", площадь " + o.getArea());
            if (o instanceof Colorable) {              // если объект можно раскрасить
                ((Colorable) o).howToColor();
            }
        }
    }
}

interface Colorable {
    void howToColor();
}

abstract class GeometricObject {
    private String color = "белый";
    private boolean filled;

    public String getColor() { return color; }
    public void setColor(String color) { this.color = color; }

    public boolean isFilled() { return filled; }
    public void setFilled(boolean filled) { this.filled = filled; }

    public abstract double getArea();
}

class Square extends GeometricObject implements Colorable {
    private double side;

    public Square() { this.side = 0; }
    public Square(double side) { this.side = side; }

    public double getSide() { return side; }
    public void setSide(double side) { this.side = side; }

    @Override
    public double getArea() { return side * side; }

    @Override
    public void howToColor() {
        System.out.println("Раскрасьте все четыре стороны.");
    }

    @Override
    public String toString() { return "Квадрат со стороной " + side; }
}

class Circle extends GeometricObject {
    private double radius;

    public Circle(double radius) { this.radius = radius; }

    @Override
    public double getArea() { return Math.PI * radius * radius; }

    @Override
    public String toString() { return "Круг r=" + radius; }
}

class Rectangle extends GeometricObject {
    private double width, height;

    public Rectangle(double width, double height) {
        this.width = width;
        this.height = height;
    }

    @Override
    public double getArea() { return width * height; }

    @Override
    public String toString() { return "Прямоугольник " + width + "x" + height; }
}

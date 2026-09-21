// Задание №2: класс IllegalTriangleException, проверка неравенства треугольника в конструкторе
public class Main {
    public static void main(String[] args) {
        try {
            Triangle ok = new Triangle(3, 4, 5);
            System.out.println(ok + ", площадь " + ok.getArea());

            Triangle bad = new Triangle(1, 2, 10);   // 1 + 2 < 10 — треугольника не существует
            System.out.println(bad);
        } catch (IllegalTriangleException e) {
            System.out.println("Ошибка: " + e.getMessage());
        }
    }
}

class IllegalTriangleException extends Exception {   // своё проверяемое исключение
    public IllegalTriangleException(String message) {
        super(message);
    }
}

class GeometricObject {
    private String color = "белый";
    private boolean filled;

    public String getColor() { return color; }
    public void setColor(String color) { this.color = color; }

    public boolean isFilled() { return filled; }
    public void setFilled(boolean filled) { this.filled = filled; }
}

class Triangle extends GeometricObject {
    private double side1 = 1.0;
    private double side2 = 1.0;
    private double side3 = 1.0;

    public Triangle() {
    }

    /** Создает треугольник с указанными сторонами */
    public Triangle(double side1, double side2, double side3) throws IllegalTriangleException {
        if (side1 + side2 <= side3 || side1 + side3 <= side2 || side2 + side3 <= side1) {
            throw new IllegalTriangleException(
                "сумма двух сторон должна быть больше третьей: " + side1 + ", " + side2 + ", " + side3);
        }
        this.side1 = side1;
        this.side2 = side2;
        this.side3 = side3;
    }

    public double getSide1() { return side1; }
    public double getSide2() { return side2; }
    public double getSide3() { return side3; }

    public double getPerimeter() { return side1 + side2 + side3; }

    public double getArea() {
        double s = getPerimeter() / 2;
        return Math.sqrt(s * (s - side1) * (s - side2) * (s - side3));
    }

    @Override
    public String toString() {
        return "Треугольник: сторона1 = " + side1 + " сторона2 = " + side2 + " сторона3 = " + side3;
    }
}

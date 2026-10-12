package vehicles;

public class Car {
    String model;
    String license;
    String color;
    int year;

    private String ownerName;        // виден только внутри класса Car
    private String insuranceNumber;
    protected String engineType;     // виден ещё и наследникам

    public Car() {
    }

    public Car(String model, String license, String color, int year) {
        this.model = model;
        this.license = license;
        this.color = color;
        this.year = year;
    }

    public String getOwnerName() { return ownerName; }
    public void setOwnerName(String ownerName) { this.ownerName = ownerName; }

    public String getInsuranceNumber() { return insuranceNumber; }
    public void setInsuranceNumber(String insuranceNumber) { this.insuranceNumber = insuranceNumber; }

    public String getEngineType() { return engineType; }
    public void setEngineType(String engineType) { this.engineType = engineType; }
}

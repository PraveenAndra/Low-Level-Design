// Shape interface with getArea method
interface Shape {
    int getArea();
}

// Rectangle class
class Rectangle implements Shape {
    protected int width;
    protected int height;

    public void setWidth(int width) {
        this.width = width;
    }

    public void setHeight(int height) {
        this.height = height;
    }

    public int getArea() {
        return width * height;
    }
}

// Square class
class Square implements Shape {
    protected int side;

    public void setSide(int side) {
        this.side = side;
    }

    public int getArea() {
        return side * side;
    }
}
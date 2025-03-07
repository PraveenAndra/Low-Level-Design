// Rectangle class with width and height
class Rectangle {
    protected int width;
    protected int height;

    // Set width and height
    public void setWidth(int width) {
        this.width = width;
    }

    public void setHeight(int height) {
        this.height = height;
    }
}

// Square inherits from Rectangle, but this breaks LSP
class Square extends Rectangle {

    @Override
    public void setWidth(int width) {
        this.width = width;
        this.height = width;  // Inconsistent behavior
    }

    @Override
    public void setHeight(int height) {
        this.height = height;
        this.width = height;  // Inconsistent behavior
    }
}
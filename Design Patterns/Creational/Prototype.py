from abc import ABC, abstractmethod
class Prototype(ABC):
    @abstractmethod
    def clone(self):
        pass

class Shape(Prototype):
    def __init__(self, height, width, color):
        self.height = height
        self.width = width
        self.color = color
    def clone(self):
        return Shape(self.height, self.width, self.color)

square = Shape(100, 100, "Blue")
square2 = square.clone()
print(square2.color)
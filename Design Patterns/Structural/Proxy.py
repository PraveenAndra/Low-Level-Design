# When we want to validate before calling original method or org obj we use proxy

from abc import ABC, abstractmethod

class Image(ABC):
    @abstractmethod
    def display(self):
        pass

class RealImage(Image):
    def __init__(self, filename):
        self.filename = filename
        self.loadImage(filename)
    def loadImage(self, filename):
        print("Loading image")
    def display(self):
        print("Displaying image")

class ProxyImage(Image):
    def __init__(self, filename):
        self.filename = filename
        self.realImage = None

    def display(self):
        if self.realImage is None:
            self.realImage = RealImage(self.filename)
        # print("Displaying image")
        self.realImage.display()


image1 = ProxyImage("image1.jpg")
image2 = ProxyImage("image2.jpg")
image1.display()
image2.display()
image1.display()
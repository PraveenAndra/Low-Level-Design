## Builder pattern is mainly used to construct an object step by step
from abc import ABC,abstractmethod
class Computer:
    def __init__(self,):
        self.ram = None
        self.cpu = None
        self.storage = None
        self.gpu = None
    def __str__(self):
        return f"Computer(cpu={self.cpu}, ram={self.ram}, storage={self.storage}, gpu={self.gpu})"
class Builder(ABC):
    @abstractmethod
    def ram(self,ram):
        pass
    @abstractmethod
    def cpu(self,cpu):
        pass
    @abstractmethod
    def gpu(self,gpu):
        pass
    @abstractmethod
    def storage(self,storage):
        pass
    @abstractmethod
    def build(self):
        pass

class GamingComputerBuilder(Builder):
    def __init__(self):
        self.computer = Computer()
    def ram(self,ram):
        self.computer.ram = ram
        return self
    def cpu(self,cpu):
        self.computer.cpu = cpu
        return self
    def gpu(self,gpu):
        self.computer.gpu = gpu
        return self
    def storage(self,storage):
        self.computer.storage = storage
        return self
    def build(self):
        return self.computer
builder = GamingComputerBuilder()
gamingComputer = (builder.ram("1GB").cpu("Intel").gpu("Nvidia").storage("3GB").build())
print(gamingComputer)


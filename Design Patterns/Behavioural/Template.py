from abc import ABC, abstractmethod

class Beverage(ABC):
    def prepare(self):
        self.boil_water()
        self.brew()
        self.pour()
        self.add_condiments()
    def boil_water(self):
        print("Boil Water")
    @abstractmethod
    def brew(self):
        pass
    def pour(self):
        print("Pour in Cup")
    @abstractmethod
    def add_condiments(self):
        pass

class Tea(Beverage):
    def brew(self):
        print("Tea")
    def add_condiments(self):
        print("Adding Lemon,Ginger")

class Coffee(Beverage):
    def brew(self):
        print("Coffee")
    def add_condiments(self):
        print("Adding Sugar and milk")

def main():
    coffee = Coffee()
    coffee.prepare()
    tea = Tea()
    tea.prepare()
if __name__ == "__main__":
    main()


from abc import ABC,abstractmethod
class BasePizza(ABC):
    @abstractmethod
    def cost(self):
        pass
    @abstractmethod
    def description(self):
        pass

class ThinCrustPizza(BasePizza):
    def cost(self):
        return 8
    def description(self):
        return "Thin Crust"+" , "
class RegularPizza(BasePizza):
    def cost(self):
        return 5
    def description(self):
        return "Regular"+" , "

class ToppingDecorator(BasePizza):
    def __init__(self, pizza: BasePizza):
        self._pizza = pizza

class OlivesTopping(ToppingDecorator):
    def cost(self):
        return self._pizza.cost() + 1
    def description(self):
        return self._pizza.description()+"Olives"+" , "

class CheeseTopping(ToppingDecorator):
    def cost(self):
        return self._pizza.cost() + 2
    def description(self):
        return self._pizza.description()+"Cheese"+" , "


pizza = ThinCrustPizza()
pizza = OlivesTopping(pizza)
pizza = CheeseTopping(pizza)
print(pizza.cost())
print(pizza.description())





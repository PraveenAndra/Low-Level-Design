from abc import ABC, abstractmethod
from enum import Enum

class ItemType(Enum):
    REGULAR = 1
    FRAGILE = 2
    JEWELL = 3

class Item:
    def __init__(self, type: ItemType, weight):
        self.type = type
        self.weight = weight

class Order:
    def __init__(self, item: Item, distance: float):
        self.item = item
        self.distance = distance

    def get_distance(self):
        return self.distance

    def get_item(self):
        return self.item

class ShippingStrategy(ABC):
    @abstractmethod
    def cost(self, order: Order) -> float:
        pass

class FlatRateShippingStrategy(ShippingStrategy):
    def __init__(self, rate: float):
        self.rate = rate

    def cost(self, order: Order) -> float:
        print(f"Flat Rate Shipping: {self.rate}")
        return self.rate

class WeightBasedShippingStrategy(ShippingStrategy):
    def __init__(self, rate: float):
        self.rate = rate

    def cost(self, order: Order) -> float:
        cost = self.rate * order.get_item().weight
        print(f"Weight Based Shipping: {cost}")
        return cost

class DistanceBasedShippingStrategy(ShippingStrategy):
    def __init__(self, rate: float):
        self.rate = rate

    def cost(self, order: Order) -> float:
        cost = self.rate * order.get_distance()
        print(f"Distance Based Shipping: {cost}")
        return cost

class ShippingSystem:
    def __init__(self, shipping_strategy: ShippingStrategy):
        self.shipping_strategy = shipping_strategy

    def set_shipping_strategy(self, shipping_strategy: ShippingStrategy):
        self.shipping_strategy = shipping_strategy

    def calculate_order_cost(self, order: Order) -> float:
        return self.shipping_strategy.cost(order)

def main():
    item = Item(ItemType.REGULAR, weight=10)
    order = Order(item, distance=50)

    shipping_system = ShippingSystem(FlatRateShippingStrategy(5))
    shipping_system.calculate_order_cost(order)

    shipping_system.set_shipping_strategy(WeightBasedShippingStrategy(2))
    shipping_system.calculate_order_cost(order)

    shipping_system.set_shipping_strategy(DistanceBasedShippingStrategy(1.5))
    shipping_system.calculate_order_cost(order)

if __name__ == "__main__":
    main()
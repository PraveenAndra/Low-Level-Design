from abc import ABC,abstractmethod
import time

class VendingMachine:
    def __init__(self, inventory: 'Inventory'):
        self.state = IdleState()
        self.selectedItem = None
        self.insertedAmount = 0
        self.inventory = inventory

    def setState(self, state):
        self.state = state

    def select_item(self, item):
        if self.inventory.is_in_stock(item):
            self.selectedItem = item
            self.state.select_item(self, item)
        else:
            self.setState(OutOfStockState())  # Item is out of stock
            self.state.select_item(self, item)

    def insertCoin(self, amount):
        self.insertedAmount += amount
        self.state.insertCoin(self, amount)

    def dispense(self):
        self.state.dispense(self)

    def reset_state(self):
        self.setState(IdleState())
        self.selectedItem = None
        self.insertedAmount = 0


class Inventory:
    def __init__(self):
        self.items = {
            "Soda": {"price": 5, "stock": 5},
            "Chips": {"price": 2, "stock": 3},
            "Candy": {"price": 3, "stock": 2}
        }

    def is_in_stock(self, item):
        return self.items.get(item, {}).get("stock", 0) > 0

    def reduce_stock(self, item):
        if self.is_in_stock(item):
            self.items[item]["stock"] -= 1
            print(f"{item} stock reduced to {self.items[item]['stock']}")
        else:
            print(f"{item} is out of stock!")

    def refill(self, item, quantity):
        if item in self.items:
            self.items[item]["stock"] += quantity
            print(f"Refilled {item}, new stock: {self.items[item]['stock']}")
        else:
            print(f"{item} not found in inventory!")

    def get_price(self, item):
        return self.items.get(item, {}).get("price", 0)

class VendingMachineState(ABC):
    @abstractmethod
    def select_item(self,context: VendingMachine,item):
        pass
    @abstractmethod
    def insertCoin(self,context: VendingMachine, amount):
        pass
    @abstractmethod
    def dispense(self,context: VendingMachine):
        pass

class IdleState(VendingMachineState):
    def select_item(self,context: VendingMachine,item):
        print(f"Selected Item{item}")
        context.setState(PaymentState())

    def insertCoin(self,context: VendingMachine, amount):
        print("Item has to be selected first before insertion")

    def dispense(self,context: VendingMachine):
        print("Item has to be selected first to dispense")

class PaymentState(VendingMachineState):
    def select_item(self,context: VendingMachine,item):
        print("Item has already been selected")
    def insertCoin(self,context: VendingMachine, amount):
        print(f"Inserting amount {amount}")
        context.setState(ReadyDispense())
    def dispense(self,context: VendingMachine):
        print("Payment has to be done before dispense")


class ReadyDispense(VendingMachineState):
    def select_item(self, context: VendingMachine, item):
        print("Item has already been selected")

    def insertCoin(self, context: VendingMachine, amount):
        print("Payment is already done")

    def dispense(self, context: VendingMachine):
        item_price = context.inventory.get_price(context.selectedItem)
        change = context.insertedAmount - item_price
        if change > 0:
            print(f"Dispensing {context.selectedItem} with change: {change}")
        else:
            print(f"Dispensing {context.selectedItem}")

        # Reduce stock and reset state
        context.inventory.reduce_stock(context.selectedItem)
        print("Dispensing complete.")
        context.reset_state()


class DispensingState(VendingMachineState):
    def select_item(self, context: VendingMachine, item):
        print("Dispensing in progress. Cannot select item.")

    def insertCoin(self, context: VendingMachine, amount):
        print("Dispensing in progress. Cannot insert coins.")

    def dispense(self, context: VendingMachine):
        print("Dispensing in progress. Wait for completion.")


class OutOfStockState(VendingMachineState):
    def select_item(self, context: VendingMachine, item):
        print(f"Item {item} is out of stock.")

    def insertCoin(self, context: VendingMachine, amount):
        print("Cannot proceed, item is out of stock.")

    def dispense(self, context: VendingMachine):
        print("Cannot dispense, item is out of stock.")

def main():
    inventory = Inventory()
    machine = VendingMachine(inventory)

    machine.select_item("Soda")  # Select Soda
    machine.insertCoin(3)  # Insert 3 coins
    machine.insertCoin(2)  # Insert 2 more coins, total = 5 (matches Soda's price)
    machine.dispense()  # Dispense Soda and return change

    # Refill and try to dispense again
    inventory.refill("Soda", 3)
    machine.select_item("Soda")
    machine.insertCoin(5)  # Exact price for Soda
    machine.dispense()  # Dispense Soda without change

    # Try with out of stock item
    machine.select_item("Chips")  # Out of stock
    machine.insertCoin(2)
    machine.dispense()

if __name__ == "__main__":
    main()

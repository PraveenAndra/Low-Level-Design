from abc import ABC,abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def create(self):
        pass
class Car(Vehicle):
    def create(self):
        return "Car"
class Bike(Vehicle):
    def create(self):
        return "Bike"
class VehicleFactory(ABC):
    @abstractmethod
    def createVehicle(self):
        pass

class CarFactory(VehicleFactory):
    def createVehicle(self):
        return Car()
class BikeFactory(VehicleFactory):
    def createVehicle(self):
        return Bike()


def vehicle_production(factory: VehicleFactory):
    vehicle = factory.createVehicle()
    print(vehicle.create())
vehicle_production(CarFactory())
vehicle_production(BikeFactory())

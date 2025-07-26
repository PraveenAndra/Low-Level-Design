# Our goal is to generate a ticket when a vehicle enters a lot and use that ticket to retrieve
# the vehicle if there is no parking spot left we need to reject the entry

# Vehicle --> Compact, SUV, Truck
# parking spot --> Compact, SUV, Truck

# We can assign a smaller vehicle to a large parking spot

# Entities
## Vehicle, ParkingSpot, Ticket
# create ticket, park vehicle, un-park vehicle
import uuid
from abc import ABC, abstractmethod
from enum import Enum

class VehicleType(Enum):
    COMPACT = 1
    SUV = 2
    TRUCK = 3
class Ticket:
    def __init__(self,id,vehicle,spot):
        self.id = id
        self.vehicle = vehicle
        self.spot = spot
class Vehicle(ABC):
    def __init__(self, numberPlate,type):
        self.numberPlate = numberPlate
        self.type = type

class ParkingSpot:
    def __init__(self, id, type):
        self.id = id
        self.type = type
        self.available = True
        self.vehicle = None
    def can_park(self,vehicle):
        if self.available and vehicle.type.value <= self.type.value:
            return True
        return False
    def park(self,vehicle):
        if self.can_park(vehicle):
            self.available = False
            self.vehicle = vehicle
            return True
        return None

    def unpark_vehicle(self):
        if not self.available and self.vehicle:
            self.available = True
            curr = self.vehicle
            self.vehicle = None
            return curr
        return None
class CompactParkingSpot(ParkingSpot):
    def __init__(self,id):
        super().__init__(id,VehicleType.COMPACT)
class SUVParkingSpot(ParkingSpot):
    def __init__(self,id):
        super().__init__(id,VehicleType.SUV)
class TruckParkingSpot(ParkingSpot):
    def __init__(self,id):
        super().__init__(id,VehicleType.TRUCK)

class ParkingLot:
    def __init__(self):
        self.availableSpots = 0
        self.ticketMapping = {}
        self.parkingSpots = []

    def add_parking_spots(self,spots):
        self.parkingSpots.extend(spots)
        self.availableSpots += len(spots)

    def create_ticket(self,vehicle,parking_spot):
        ticket_id = uuid.uuid4()
        self.ticketMapping[ticket_id] = parking_spot
        return Ticket(ticket_id,vehicle,parking_spot)

    def park_vehicle(self,vehicle):
        if self.availableSpots == 0:
            print("No Available Parking Spot")
            return None
        for spot in self.parkingSpots:
            if spot.can_park(vehicle):
                ticket = self.create_ticket(vehicle,spot)
                spot.park(vehicle)
                print("Parked vehicle",ticket.id)
                self.availableSpots = self.availableSpots - 1
                return ticket
        print("No Available Parking Spot")
        return None
    def retrieve_vehicle(self,ticket):
        if ticket.id in self.ticketMapping:
            spot = self.ticketMapping[ticket.id]
            vehicle = spot.unpark_vehicle()
            del self.ticketMapping[ticket.id]
            print("vehicle is retrieved")
            self.availableSpots = self.availableSpots + 1
            return vehicle
        print("Invalid Ticket")
        return None

class CompactCar(Vehicle):
    def __init__(self, number_plate):
        super().__init__(number_plate, VehicleType.COMPACT)


def main():
    lot = ParkingLot()
    lot.add_parking_spots([
        CompactParkingSpot(1),
        SUVParkingSpot(2),
        TruckParkingSpot(3),
    ])

    car = CompactCar("ABC123")
    ticket = lot.park_vehicle(car)

    if ticket:
        lot.retrieve_vehicle(ticket)


if __name__ == "__main__":
    main()














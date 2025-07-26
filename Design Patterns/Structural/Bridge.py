# It is mainly used to separate abstraction and implementation of class
from abc import ABC, abstractmethod

#Implementor
class Device(ABC):
    @abstractmethod
    def turn_on(self):
        pass
    @abstractmethod
    def turn_off(self):
        pass
#Concrete
class TV(Device):
    def turn_on(self):
        print("TV is ON")
    def turn_off(self):
        print("TV is OFF")

class Fan(Device):
    def turn_off(self):
        print("Fan is OFF")
    def turn_on(self):
        print("Fan is ON")

#Abstraction
class RemoteControl:
    def __init__(self,device):
        self.device = device
    def turn_off(self):
        self.device.turn_off()
    def turn_on(self):
        self.device.turn_on()

class AdvancedRemoteControl(RemoteControl):
    def mute(self):
        print("Muting the device")
        self.device.turn_off()
tv = TV()
fan = Fan()
tvRemote = RemoteControl(tv)
fanRemote = AdvancedRemoteControl(fan)
tvRemote.turn_off()
fanRemote.mute()


from abc import ABC, abstractmethod

class WeatherStationSubject(ABC):
    @abstractmethod
    def add_observer(self, observer):
        pass
    @abstractmethod
    def remove_observer(self, observer):
        pass
    @abstractmethod
    def update_observer(self):
        pass
class WeatherStation(WeatherStationSubject):
    def __init__(self):
        self.observers = []
        self.temperature = 0
        self.humidity = 0


    def add_observer(self, observer):
        self.observers.append(observer)
    def remove_observer(self, observer):
        self.observers.remove(observer)
    def update_observer(self):
        for observer in self.observers:
            observer.update(self)
    def get_temperature(self):
        return self.temperature
    def get_humidity(self):
        return self.humidity
    def set_weather(self, temperature, humidity):
        self.temperature = temperature
        self.humidity = humidity
        self.update_observer()


class WeatherObserver(ABC):
    @abstractmethod
    def update(self, weather: WeatherStation):
        pass

class TemperatureDisplay(WeatherObserver):
    def update(self,weather: WeatherStation):
        print(f"Temperature display : {weather.get_temperature()} F")

class HumidityDisplay(WeatherObserver):
    def update(self,weather: WeatherStation):
        print(f"Humidity display : {weather.get_humidity()} %")


def main():
    temperatureDisplay = TemperatureDisplay()
    humidityDisplay = HumidityDisplay()
    weatherStation = WeatherStation()
    weatherStation.add_observer(temperatureDisplay)
    weatherStation.add_observer(humidityDisplay)
    weatherStation.set_weather(25,65)
    weatherStation.set_weather(30,70)
    weatherStation.remove_observer(temperatureDisplay)
    weatherStation.set_weather(35,90)

if __name__ == "__main__":
    main()

from abc import ABC, abstractmethod
class Button(ABC):
    @abstractmethod
    def click(self):
        pass
class Toggle(ABC):
    @abstractmethod
    def toggle(self):
        pass

class WindowsButton(Button):
    def click(self):
        print("WindowsButton")
class MacButton(Button):
    def click(self):
        print("MacButton")
class WindowsToggle(Toggle):
    def toggle(self):
        print("WindowsToggle")
class MacToggle(Toggle):
    def toggle(self):
        print("MacToggle")

class GUIFactory(ABC):
    @abstractmethod
    def createButton(self):
        pass
    @abstractmethod
    def createToggle(self):
        pass

class WindowsGUI(GUIFactory):
    def createButton(self):
        return WindowsButton()
    def createToggle(self):
        return WindowsToggle()
class MacGUI(GUIFactory):
    def createButton(self):
        return MacButton()
    def createToggle(self):
        return MacToggle()

def render_UI(factory: GUIFactory):
    button = factory.createButton()
    toggle = factory.createToggle()
    button.click()
    toggle.toggle()
render_UI(WindowsGUI())
render_UI(MacGUI())

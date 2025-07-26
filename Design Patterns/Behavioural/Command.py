from abc import ABC, abstractmethod

# === Command Interface ===
class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

    @abstractmethod
    def undo(self):
        pass


# === Receiver ===
class Light:
    def on(self):
        print("💡 Light is ON")

    def off(self):
        print("💡 Light is OFF")


# === Concrete Commands ===
class LightOnCommand(Command):
    def __init__(self, light: Light):
        self.light = light

    def execute(self):
        self.light.on()

    def undo(self):
        self.light.off()


class LightOffCommand(Command):
    def __init__(self, light: Light):
        self.light = light

    def execute(self):
        self.light.off()

    def undo(self):
        self.light.on()


# === Invoker ===
class RemoteControl:
    def __init__(self):
        self._history = []

    def submit(self, command: Command):
        command.execute()
        self._history.append(command)

    def undo_last(self):
        if self._history:
            last = self._history.pop()
            print("↩️ Undoing last command:")
            last.undo()
        else:
            print("❌ No commands to undo.")


# === Client Code ===
def main():
    # Receiver
    light = Light()

    # Commands
    on_command = LightOnCommand(light)
    off_command = LightOffCommand(light)

    # Invoker
    remote = RemoteControl()

    # Use remote
    remote.submit(on_command)    # Light ON
    remote.submit(off_command)   # Light OFF

    # Undo operations
    remote.undo_last()           # Undo OFF → Light ON
    remote.undo_last()           # Undo ON → Light OFF
    remote.undo_last()           # Nothing to undo

if __name__ == "__main__":
    main()
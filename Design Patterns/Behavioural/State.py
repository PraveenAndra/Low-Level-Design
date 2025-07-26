# Allows an object to change its behaviour when its internal state changes
from abc import ABC, abstractmethod

class MusicPlayerState(ABC):
    @abstractmethod
    def play(self,context):
        pass
    @abstractmethod
    def pause(self,context):
        pass
class IdleState(MusicPlayerState):
    def play(self,context):
        print("Playing Music")
        context.state = RunningState()
    def pause(self,context):
        print("No Music is playing")
class RunningState(MusicPlayerState):
    def play(self,context):
        print("Already Playing")
    def pause(self,context):
        print("Pausing Music")
        context.state = IdleState()

class MusicPlayer:
    def __init__(self):
        self.state = IdleState()
    def play(self):
        self.state.play(self)
    def pause(self):
        self.state.pause(self)
    def reset(self):
        self.state = IdleState()
        print("Reset to Idle State")

def main():
    musicPlayer = MusicPlayer()
    musicPlayer.pause()
    musicPlayer.play()
    musicPlayer.pause()
    musicPlayer.reset()

if __name__ == "__main__":
    main()

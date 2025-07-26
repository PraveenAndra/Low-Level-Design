# Simplifying provides a simplified interface of a complex system which is easier to use by clients

class DVDPlayer:
    def on(self):
        print("Player on")
    def off(self):
        print("Player off")
    def play(self,movie):
        print(f"Player play{movie}")

class Projector:
    def on(self):
        print("Projector on")
    def off(self):
        print("Projector off")
    def set_resolution(self,resolution):
        print("Projector set resolution")

class Speaker:
    def on(self):
        print("Speaker on")
    def off(self):
        print("Speaker off")
    def set_volume(self,volume):
        print(f"Speaker set volume {volume}")

class HomeTheaterFacade:
    def __init__(self,dvdPlayer, projector, speaker):
        self.dvdPlayer = dvdPlayer
        self.projector = projector
        self.speaker = speaker
    def watch_movie(self,movie):
        self.dvdPlayer.on()
        self.projector.on()
        self.speaker.on()
        self.speaker.set_volume(10)
        self.dvdPlayer.play(movie)
    def end_movie(self):
        self.speaker.off()
        self.dvdPlayer.off()
        self.projector.off()

def main():
    dvd_player = DVDPlayer()
    projector = Projector()
    speaker = Speaker()
    home_theatre = HomeTheaterFacade(dvd_player, projector, speaker)
    home_theatre.watch_movie("RRR")
    home_theatre.end_movie()

if __name__ == "__main__":
    main()
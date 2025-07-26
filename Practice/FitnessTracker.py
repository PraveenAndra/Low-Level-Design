from abc import ABC, abstractmethod
from typing import List


# === Observer Interface ===
class FitnessObserver(ABC):
    @abstractmethod
    def update(self, tracker: 'FitnessTracker'):
        pass


# === Subject Interface ===
class FitnessTrackerSubject(ABC):
    @abstractmethod
    def add_observer(self, observer: FitnessObserver):
        pass

    @abstractmethod
    def remove_observer(self, observer: FitnessObserver):
        pass

    @abstractmethod
    def notify_observers(self):
        pass


# === Concrete Subject ===
class FitnessTracker(FitnessTrackerSubject):
    def __init__(self):
        self.steps = 0
        self.calories = 0
        self.heartrate = 0
        self._observers: List[FitnessObserver] = []

    def add_observer(self, observer: FitnessObserver):
        if observer not in self._observers:
            self._observers.append(observer)

    def remove_observer(self, observer: FitnessObserver):
        if observer in self._observers:
            self._observers.remove(observer)

    def notify_observers(self):
        for observer in self._observers:
            observer.update(self)

    def add_data(self, steps: int, calories: int, heartrate: int):
        self.steps += steps
        self.calories = calories
        self.heartrate = heartrate
        print(f"\n[Tracker] New data - Steps: {self.steps}, Calories: {self.calories}, Heart Rate: {self.heartrate}")
        self.notify_observers()

    def reset(self):
        self.steps = 0
        self.calories = 0
        self.heartrate = 0
        print("[Tracker] Data has been reset.")


# === Concrete Observer 1 ===
class FitnessDataDisplay(FitnessObserver):
    def update(self, tracker: FitnessTracker):
        print(f"[Display] Steps: {tracker.steps}, Calories: {tracker.calories}, Heart Rate: {tracker.heartrate}")


# === Concrete Observer 2 ===
class GoalNotifier(FitnessObserver):
    def __init__(self, step_goal: int = 1000):
        self.goal_steps = step_goal
        self.goal_reached = False

    def update(self, tracker: FitnessTracker):
        if not self.goal_reached and tracker.steps >= self.goal_steps:
            print(f"[Goal] 🎉 Goal reached! You have taken {tracker.steps} steps.")
            self.goal_reached = True

    def reset_goal(self):
        self.goal_reached = False
        print("[Goal] Goal progress reset.")


# === Test / Client Code ===
def main():
    # Create observers
    display = FitnessDataDisplay()
    goal_notifier = GoalNotifier(step_goal=200)

    # Create subject
    tracker = FitnessTracker()

    # Attach observers
    tracker.add_observer(display)
    tracker.add_observer(goal_notifier)

    # Simulate data updates
    tracker.add_data(80, 100, 89)   # No goal yet
    tracker.add_data(120, 150, 92)  # Goal reached

    # Reset goal and test again
    goal_notifier.reset_goal()
    tracker.add_data(100, 80, 85)   # Already over goal, but flag is reset

    # Remove display and show update without it
    tracker.remove_observer(display)
    tracker.add_data(50, 40, 80)


if __name__ == "__main__":
    main()
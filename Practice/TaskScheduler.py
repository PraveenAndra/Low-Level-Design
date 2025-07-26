from abc import ABC,abstractmethod
from enum import Enum
import heapq
class Priority(Enum):
    HIGH = 1
    MEDIUM = 2
    LOW = 3
class TaskState(Enum):
    CREATED = 1
    FINISHED = 2
    RUNNING = 3
class Task:
    def __init__(self,id,priority):
        self.id = id
        self.dependencies = []
        self.priority = priority
        self.state = TaskState.CREATED
    def addDependency(self,dep):
        self.dependencies.append(dep)
    def execute(self):
        if self.state == TaskState.RUNNING:
            print("Circular Dependencies")
            return
        for dep in self.dependencies:
            if dep.state == TaskState.CREATED:
                dep.execute()
        if self.state == TaskState.CREATED:
            self.state = TaskState.FINISHED
            print(f"Task {self.id}")

    def __lt__(self, other):
        return self.priority.value < other.priority.value or (
                    self.priority.value == other.priority.value and self.id < other.id)


class TaskScheduler:
    def __init__(self):
        self.tasks = []
    def addTask(self,task):
        print(task.priority)
        heapq.heappush(self.tasks,task)
    def run(self):
        while self.tasks:
            task = heapq.heappop(self.tasks)
            if task.state == TaskState.CREATED:
                task.execute()
    # def getOrder(self):
    #
    # def execute(self,task):



task1 = Task(1,Priority.MEDIUM)
task2 = Task(2,Priority.HIGH)
task3 = Task(3,Priority.MEDIUM)
task4 = Task(4,Priority.LOW)
task1.addDependency(task2)
task2.addDependency(task3)
scheduler = TaskScheduler()
scheduler.addTask(task1)
scheduler.addTask(task2)
scheduler.addTask(task3)
scheduler.addTask(task4)
scheduler.run()

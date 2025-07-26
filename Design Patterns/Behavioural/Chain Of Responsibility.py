from abc import ABC, abstractmethod

class SupportHandler(ABC):
    def __init__(self):
        self.next = None

    def set_next(self, next):
        self.next = next
        return next

    def forward(self, issue, priority):
        if self.next:
            self.next.handle(issue, priority)
        else:
            print(f"No handler available for issue: {issue} (Priority: {priority})")

    @abstractmethod
    def handle(self, issue, priority):
        pass

class L1SupportHandler(SupportHandler):
    def handle(self, issue, priority):
        if priority > 1:
            print(f"L1 Escalated Issue to next Level: {issue}")
            self.forward(issue, priority)
        else:
            print(f"L1 Resolved the issue: {issue}")

class L2SupportHandler(SupportHandler):
    def handle(self, issue, priority):
        if priority > 2:
            print(f"L2 Escalated Issue to next Level: {issue}")
            self.forward(issue, priority)
        else:
            print(f"L2 Resolved the issue: {issue}")

class ManagerHandler(SupportHandler):
    def handle(self, issue, priority):
        print(f"Manager Resolved the issue: {issue}")

def main():
    l1 = L1SupportHandler()
    l2 = L2SupportHandler()
    manager = ManagerHandler()

    l1.set_next(l2).set_next(manager)

    # Test different priorities
    l1.handle("Forgot password", 1)
    print("---")
    l1.handle("Minor bug", 2)
    print("---")
    l1.handle("Outage", 3)
    print("---")
    l1.handle("Security breach", 4)

if __name__ == "__main__":
    main()
from collections import deque

class EventSystem:
    def __init__(self):
        self.queue = deque()

    def add_event(self, event):
        self.queue.append(event)

    def process_next_event(self):
        if self.queue:
            event = self.queue.popleft()
            print("Processed:", event)
        else:
            print("No events to process")

    def display_pending_events(self):
        if self.queue:
            print("Pending Events:", list(self.queue))
        else:
            print("No pending events")

    def cancel_event(self, event):
        if event in self.queue:
            self.queue.remove(event)
            print("Canceled:", event)
        else:
            print("Event not found")

system = EventSystem()
while True:
    print("\n1. Add Event\n2. Process Next Event\n3. Display Pending Events\n4. Cancel Event\n5. Exit")
    ch = input("Enter choice: ")
    if ch == '1':
        e = input("Enter event: ")
        system.add_event(e)
    elif ch == '2':
        system.process_next_event()
    elif ch == '3':
        system.display_pending_events()
    elif ch == '4':
        e = input("Enter event to cancel: ")
        system.cancel_event(e)
    elif ch == '5':
        break
    else:
        print("Invalid choice")

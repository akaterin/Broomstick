from enum import Enum
from Queue import PriorityQueue

class EventType(Enum):
    beggining = 1
    end = 2
    intersection = 3

class Event(object):

    def __init__(self, type, axis):
        self.type = type
        self.axis = axis

    def __cmp__(self, other):
        if self.axis < other.axis:
            return 1
        elif self.axis == other.axis:
            return 0
        else:
            return -1


class EventsCollection(object):

    def __init__(self):
        self.events = PriorityQueue()

    def add_event(self, event):
        self.events.put(event)

    def pop(self):
        self.events.get()

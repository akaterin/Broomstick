from enum import Enum

class EventType(Enum):
    beggining = 1
    end = 2
    intersection = 3

class Event(object):

    def __init__(self, type, axis):
        self.type = type
        self.axis = axis


class EventsCollection(object):

    def __init__(self):
        self.events = []

from helpers import *
import generator
from bintrees import FastRBTree

class Segment(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end


class SegmentCollection(object):

    def __init__(self):
        self.segments = []
        #self.segments_struct = FastRBTree()

    def __init__(self, list):
        self.segments = list

    def add_segment(self, segment):
        self.segments.append(segment)

    def add_segment(self, start, end):
        segment = Segment(start, end)
        self.add_segment(segment)

    def del_segment(self, segment):
        self.segments.remove(segment)

    def del_segment(self, start, end):
        segment = Segment(start, end)
        self.del_segment(segment)

    def get(self, index):
        return self.segments[index]

    def index(self, segment):
        return self.segments.index(segment)

    def move_up(self, segment):
        index = self.index(segment)
        self.segments[index] = self.get(index -1)
        self.segments[index -1] = segment

    def move_down(self, segment):
        index = self.index(segment)
        self.segments[index] = self.get(index +1)
        self.segments[index + 1] = segment



def generate_segments(nr, plane_range):
    segments = SegmentCollection()
    while nr > 0:
        first = generator.create_random_point(plane_range)
        second = generator.create_random_point(plane_range)
        if first != second and first.y != second.y:
            nr -= 1
            segment = Segment(min(first, second, key=lambda x: x.x), max(first, second, key=lambda x: x.x))
            segments.add_segment(segment)
    return segments











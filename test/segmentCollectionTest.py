import unittest
from SegmentCollection import *
from helpers import *

class generatorTest(unittest.TestCase):

    def test_up(self):
        seg1 = Segment(Point(0,0), Point(1,0))
        seg2 = Segment(Point(1,0), Point(1,1))
        segments = SegmentCollection([seg1, seg2])
        segments.move_up(seg2)
        self.assertTrue(seg1 == segments.get(1))
        self.assertTrue(seg2 == segments.get(0))

    def test_down(self):
        seg1 = Segment(Point(0,0), Point(1,0))
        seg2 = Segment(Point(1,0), Point(1,1))
        segments = SegmentCollection([seg1, seg2])
        segments.move_down(seg1)
        self.assertTrue(seg1 == segments.get(1))
        self.assertTrue(seg2 == segments.get(0))



    if __name__ == '__main__':
        unittest.main()
class Point(object):
    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)

    def __str__(self):
        return '{0} {1}'.format(self.x, self.y)

    def get_dict(self):
        return {'x': self.x, 'y': self.y}


class RangeXY(object):
    def __init__(self, low_x, high_x, low_y, high_y):
        self.low_x = low_x
        self.high_x = high_x
        self.low_y = low_y
        self.high_y = high_y


class Range(object):
    def __init__(self, low_axis, high_axis):
        self.low = low_axis
        self.high = high_axis




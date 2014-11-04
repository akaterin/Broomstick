import math
import random
from helpers import *


def print_points(points):
    print(len(points))
    for point in points:
        print(point)


def generate_d_set():
    points_x_range = (-1000.0, 1000.0)
    points_number = 1000
    vector_a = Point(-1.0, 0.0)
    vector_b = Point(1.0, 0.1)

    f = create_line_func_from_two_points(vector_a, vector_b)
    points = [create_random_point_on_line(f, points_x_range) for i in range(points_number)]
    return points


def generate_circle_set(points_number, r):
    points = [create_random_point_on_circle(r) for i in range(points_number)]
    print_points(points)
    return points

def generate_range_set(points_number, rangeX, rangeY):
    plane_range = RangeXY(rangeX.low, rangeX.high, rangeY.low, rangeY.high)

    points = [create_random_point(plane_range) for i in range(points_number)]
    return points

def generate_border_rectangle_set(points_number, rangeX, rangeY):
    rectangle = RangeXY(rangeX.low, rangeX.high, rangeY.low, rangeY.high)

    points = [create_random_point_on_rectangle(rectangle) for i in range(points_number)]
    print_points(points)
    return points

def generate_square_samples(points_on_sides_number, points_on_diagonals_number, v1, v2, v3, v4):
    points = [v1, v2, v3, v4]
    f1 = create_line_func_from_two_points(v1, v3)
    f2 = create_line_func_from_two_points(v2, v4)
    x_range = Range(min(v1.x, v2.x, v3.x, v4.x), max(v1.x, v2.x, v3.x, v4.x))
    points_on_diagonal = [create_random_point_on_diagonals(f1, f2, x_range) for i in range(points_on_diagonals_number)]
    points_on_sides = [create_random_point_on_axis_sides(v3.y) for i in range(points_on_sides_number)]
    points.extend(points_on_diagonal)
    points.extend(points_on_sides)
    return points

import getopt, sys


def main():
    try:
        opts, args = getopt.getopt(sys.argv[1:], "rcps", [])
    except getopt.GetoptError as err:
        print(str(err))
        sys.exit(2)

    for o, a in opts:
        if o == "-r":
            rangeX = Range(float(args[1]), float(args[2]))
            rangeY = Range(float(args[3]), float(args[4]))
            generate_range_set(int(args[0]), rangeX, rangeY)
            break
        elif o == "-c":
            generate_circle_set(int(args[0]), float(args[1]))
            break
        elif o == "-p":
            rangeX = Range(float(args[1]), float(args[2]))
            rangeY = Range(float(args[3]), float(args[4]))
            generate_border_rectangle_set(int(args[0]), rangeX, rangeY)
            break
        elif o == "-s":
            v1 = Point(float(args[2]), float(args[3]))
            v2 = Point(float(args[4]), float(args[5]))
            v3 = Point(float(args[6]), float(args[7]))
            v4 = Point(float(args[8]), float(args[9]))
            generate_square_samples(int(args[0]), int(args[1]), v1, v2, v3, v4)
            break
    else:
        print('No option selected')


def create_line_func_from_two_points(a, b):
    direction_coeficient = (b.y - a.y) / (b.x - a.x)
    translation_coeficient = b.y - direction_coeficient * b.x
    return lambda x: direction_coeficient * x + translation_coeficient


def create_random_point_on_line(f, x_range):
    low_x, high_x = x_range
    x = random.uniform(low_x, high_x)
    return Point(x, f(x))

def create_random_point_on_diagonals(f1, f2, x_range):
    point = create_random_point_on_line(f1, (x_range.low, x_range.high*2))
    if point.x < x_range.high:
        return point
    x = point.x - x_range.high
    return Point(x, f2(x))

def create_random_point_on_axis_sides(y_max):
    line = RangeXY(0, 0, 0, y_max*2)
    point = create_random_point(line)
    if point.y < y_max:
        return point
    return Point(point.y - y_max, 0)

def create_random_point(plane_range):
    x = random.uniform(plane_range.low_x, plane_range.high_x)
    y = random.uniform(plane_range.low_y, plane_range.high_y)
    return Point(x, y)

def create_random_point_on_rectangle(plane_range):
    xWidth = plane_range.high_x - plane_range.low_x
    yWidth = plane_range.high_y - plane_range.low_y
    lineWidth = 2*xWidth + 2*yWidth
    place = random.uniform(0.0, lineWidth)
    if 0 < place < xWidth:
        return Point(plane_range.low_x + place, plane_range.high_y)
    if xWidth < place < xWidth+yWidth:
        return Point(plane_range.high_x, plane_range.high_y - (place - xWidth))
    if xWidth+yWidth < place < 2*xWidth + yWidth:
        return Point(plane_range.high_x - (place - xWidth - yWidth), plane_range.low_y)
    if 2*xWidth + yWidth < place < 2*xWidth + 2*yWidth:
        return Point(plane_range.low_x, plane_range.low_y + (place - 2*xWidth- yWidth))

def create_random_point_on_circle(r):
    angle = random.uniform(0.0, 2 * math.pi)
    x = r * math.cos(angle)
    y = r * math.sin(angle)

    return Point(x, y)


if __name__ == '__main__':
    main()


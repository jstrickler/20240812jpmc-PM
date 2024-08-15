"""
General geometry-related functions

Syntax:

area = circle_area(diameter)
area = rectangle_area(length, width)
area = square_area(side)
"""
import math   # load math.py

PI = math.pi

def __main__():
    print("Hello from the geometry module!")

def circle_area(diameter):
    """
    Compute the area of a circle from a given diameter

    :param diameter: Diameter of circle
    :return: Area of circle
    """
    radius = diameter / 2
    return PI * (radius ** 2)

def rectangle_area(length, width):
    """
    Compute the area of a rectangle.

    :param length:  length of longer side
    :param width:   length of shorter side
    :return: Area of rectangle
    """
    return length * width

def square_area(side):
    """
    Compute area of a square.

    :param side: Length of one side
    :return: Area of square
    """
    return side ** 2

print(f"{__name__ = }")


# if NOT imported
if __name__ == "__main__":  # {name} -> __name__    {main} ->  __main__
    raw_diameter = input("Please enter diameter of circle: ")
    diameter = float(raw_diameter)
    area = circle_area(diameter)
    print(f"{area = }")

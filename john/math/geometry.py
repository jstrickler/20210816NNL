"""
Provide geometric functions
"""
from math import pi

ANIMAL = "wombat"

def main():
    print("HI MOM!")
    print(ANIMAL)
    print(cylinder_volume(10, 5))

def circle_area(diameter):
    """
    Calculate area of circle

    :param diameter: Diameter of circle
    :return: area of circle
    """
    radius = diameter / 2
    area = pi * radius ** 2
    return area

def rectangle_area(length, width):
    """
    Calculate area of rectangle

    :param length: Length of rectangle as int or float
    :param width: With of rectangle
    :return: Area of rectangle
    """
    return length * width

def cylinder_volume(diameter, height):
    return circle_area(diameter) * height

# print("My name is", __name__)

if __name__ == '__main__':  # if executed, not imported
    main()


from math import pi

def get_message():
    return "Hello NNL world"

message = get_message()
print(message)

def spam():
    print("Hi from spam()")

x = spam()
print(x)

#        parameter
def greet(whom):
    print(f"Hello, {whom}")

#    argument
greet("world")
greet("Mom")
greet("New York")
person = "Dr. Livingston"
greet(person)

def circle_area(diameter):
    radius = diameter / 2
    area = pi * radius ** 2
    return area

print(f"{circle_area(7):.2f}")
d = 100
print(circle_area(d))

def rectangle_area(length, width):
    return length * width

print(rectangle_area(5, 10))

def cylinder_volume(diameter, height):
    return circle_area(diameter) * height

print(cylinder_volume(3, 10))

# print(cylinder_volume(3))


def greet(whom="world"):
    print(f"Hello, {whom}")

greet("Dad")
greet("Gretchen")
greet()

# positional-only       can't use name
# required positional   normal, everyday
# optional positional   optional
# required named        must use specified name
# optional named        can use any name


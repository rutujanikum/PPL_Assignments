import turtle
import abc
from abc import ABC, abstractmethod
from math import sqrt


# modularity achieved by defining separate functions for various tasks
# Interface
class Polygon(abc.ABC):
    @abc.abstractmethod
    def no_of_sides(self):
        pass


# base class
# Hierarchy achieved as More than one classes inherits Shape class
# abstract class
class Shapes(ABC):
    # abstract method/ pure virtual function
    def area(self):
        pass

    # abstract method/ pure virtual function
    def perimeter(self):
        pass


# derived classes
class Circle(Shapes):
    def __init__(self, r=0):
        self.__radius = r
        self.__area = 0
        self.__circumference = 0

    # Polymorphism (overrides method in Shpaes)
    def area(self):
        self.__area = self.__radius * self.__radius * 3.14
        return self.__area

    def __cir_circumference(self):
        self.__circumference = 2 * 3.14 * self.__radius
        return self.__circumference

    def get_cir_properties(self):
        print("*******Circle********")
        print("Area = ", self.area())
        print("Circumference = ", self.__cir_circumference())

    def draw_circle(self):
        t = turtle.Turtle()
        t.circle(self.__radius)
        turtle.done()


# multiple inheritance
class Rectangle(Shapes, Polygon):
    def __init__(self, l=0, w=0):
        self.__length = l
        self.__width = w
        self.__area = 0
        self.__perimeter = 0

    def area(self):
        self.__area = self.__length * self.__width
        return self.__area

    def perimeter(self):
        self.__perimeter = 2 * (self.__length + self.__width)
        return self.__perimeter

    def get_rect_properties(self):
        print("*******Rectangle********")
        print("Area = ", self.area())
        print("Perimeter = ", self.perimeter())

    def no_of_sides(self):
        print("Number of sides = 4")

    def draw_rect(self):
        t = turtle.Turtle()
        t.forward(self.__length)
        t.left(90)
        t.forward(self.__width)
        t.left(90)
        t.forward(self.__length)
        t.left(90)
        t.forward(self.__width)
        t.left(90)
        turtle.done()


class Square(Shapes,Polygon):
    def __init__(self, s=0):
        self.__side = s
        self.__area = 0
        self.__perimeter = 0

    def area(self):
        self.__area = self.__side * self.__side
        return self.__area

    def perimeter(self):
        self.__perimeter = 4 * self.__side
        return self.__perimeter

    def get_sq_properties(self):
        print("*******Square********")
        print("Area = ", self.area())
        print("Perimeter = ", self.perimeter())

    def no_of_sides(self):
        print("Number of sides = 4")

    def draw_sq(self):
        t = turtle.Turtle()
        t.forward(self.__side)
        t.left(90)
        t.forward(self.__side)
        t.left(90)
        t.forward(self.__side)
        t.left(90)
        t.forward(self.__side)
        t.left(90)
        turtle.done()


class Triangle(Shapes, Polygon):
    def __init__(self, s1=0, s2=0, b=0, h=0):
        self.__side1 = s1
        self.__side2 = s2
        self.__breadth = b
        self.__height = h
        self.__area = 0
        self.__perimeter = 0

    def area(self):
        self.__area = 0.5 * self.__breadth * self.__height
        return self.__area

    def perimeter(self):
        self.__perimeter = self.__side1 + self.__side2 + self.__breadth
        return self.__perimeter

    def get_tri_properties(self):
        print("*******Triangle********")
        print("Area = ", self.area())
        print("Perimeter = ", self.perimeter())

    def no_of_sides(self):
        print("Number of sides = 3")


class Parallelogram(Shapes, Polygon):
    def __init__(self, s=0, b=0, h=0):
        self.__side = s
        self.__base = b
        self.__height = h
        self.__area = 0
        self.__perimeter = 0

    def area(self):
        self.__area = self.__base * self.__height
        return self.__area

    def perimeter(self):
        self.__perimeter = 2 * (self.__side + self.__base)
        return self.__perimeter

    def get_para_properties(self):
        print("*******Parallelogram********")
        print("Area = ", self.area())
        print("Perimeter = ", self.perimeter())

    def no_of_sides(self):
        print("Number of sides = 4")


class Ellipse(Shapes):
    def __init__(self, r1=0, r2=0):
        self.__major_axis = r1
        self.__minor_axis = r2
        self.__area = 0
        self.__perimeter = 0

    def area(self):
        self.__area = self.__major_axis * self.__minor_axis * 3.14
        return self.__area

    def perimeter(self):
        self.__perimeter = 2 * 3.14 * sqrt(
            (((self.__minor_axis * self.__minor_axis) + (self.__major_axis * self.__major_axis)) / 2))
        return self.__perimeter

    def get_ell_properties(self):
        print("*******Ellipse********")
        print("Area = ", self.area())
        print("Perimeter = ", self.perimeter())


class Hexagon(Shapes, Polygon):
    def __init__(self, s=0):
        self.__side = s
        self.__area = 0
        self.__perimeter = 0

    def __hex_area(self):
        self.__area = ((3 * sqrt(3)) / 2) * (self.__side * self.__side)
        return self.__area

    def __hex_perimeter(self):
        self.__perimeter = 6 * self.__side
        return self.__perimeter

    def get_hex_properties(self):
        print("*******Hexagon********")
        print("Area = ", self.__hex_area())
        print("Perimeter = ", self.__hex_perimeter())

    def no_of_sides(self):
        print("Number of sides = 6")


class Rhombus(Polygon):
    def __init__(self, d1=0, d2=0, s=0):
        self.__dig1 = d1
        self.__dig2 = d2
        self.__side = s
        self.__area = 0
        self.__perimeter = 0

    def __Rh_area(self):
        self.__area = (self.__dig1 * self.__dig2) / 2
        return self.__area

    def __Rh_perimeter(self):
        self.__perimeter = 4 * self.__side
        return self.__perimeter

    def get_Rh_properties(self):
        print("*******Rhombus********")
        print("Area = ", self.__Rh_area())
        print("Perimeter = ", self.__Rh_perimeter())

    def no_of_sides(self):
        print("Number of sides = 4")


class Octagon(Polygon):
    def __init__(self, s=0):
        self.__side = s
        self.__area = 0
        self.__perimeter = 0

    def __octa_area(self):
        self.__area = (2 * (1 + sqrt(2))) * (self.__side * self.__side)
        return self.__area

    def __octa_perimeter(self):
        self.__perimeter = 8 * self.__side
        return self.__perimeter

    def get_octa_properties(self):
        print("*******Octagon********")
        print("Area = ", self.__octa_area())
        print("Perimeter = ", self.__octa_perimeter())

    def no_of_sides(self):
        print("Number of sides = 8")


class Pentagon(Polygon):
    def __init__(self, s=0, a=0):
        self.__side = s
        self.__apothem = a
        self.__area = 0
        self.__perimeter = 0

    def __pen_area(self):
        self.__area = (self.__apothem * self.__side) / 2
        return self.__area

    def __pen_perimeter(self):
        self.__perimeter = 5 * self.__side
        return self.__perimeter

    def get_pen_properties(self):
        print("*******Pentagon********")
        print("Area = ", self.__pen_area())
        print("Perimeter = ", self.__pen_perimeter())

    def no_of_sides(self):
        print("Number of sides = 5")


s1 = Circle(10)
s1.get_cir_properties()
# s1.draw_circle()

s2 = Rectangle(20, 10)
s2.get_rect_properties()
s2.no_of_sides()
# s2.draw_rect()

s3 = Pentagon(3, 2)
s3.get_pen_properties()
s3.no_of_sides()

s4 = Triangle(10, 10, 10, 7)
s4.get_tri_properties()
s4.no_of_sides()

s5 = Parallelogram(10, 7, 7)
s5.get_para_properties()
s5.no_of_sides()

s6 = Ellipse(10, 8)
s6.get_ell_properties()

s7 = Hexagon(10)
s7.get_hex_properties()
s7.no_of_sides()

s8 = Rhombus(10, 10, 7)
s8.get_Rh_properties()
s8.no_of_sides()

s9 = Octagon(10)
s9.get_octa_properties()
s9.no_of_sides()

s10 = Square(50)
s10.get_sq_properties()
s10.no_of_sides()
s10.draw_sq()



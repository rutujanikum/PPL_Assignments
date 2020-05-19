import turtle
from math import sqrt


class Circle:
    def __init__(self, r=0):
        self.__radius = r
        self.__area = 0
        self.__circumference = 0

    def __cir_area(self):
        self.__area = self.__radius * self.__radius * 3.14
        return self.__area

    def __cir_circumference(self):
        self.__circumference = 2 * 3.14 * self.__radius
        return self.__circumference

    def get_cir_properties(self):
        print("*******Circle********")
        print("Area = ", self.__cir_area())
        print("Circumference = ", self.__cir_circumference())

    def draw_circle(self):
        t = turtle.Turtle()
        t.circle(self.__radius)
        turtle.done()


class Rectangle:
    def __init__(self, l=0, w=0):
        self.__length = l
        self.__width = w
        self.__area = 0
        self.__perimeter = 0

    def __rect_area(self):
        self.__area = self.__length * self.__width
        return self.__area

    def __rect_perimeter(self):
        self.__perimeter = 2 * (self.__length + self.__width)
        return self.__perimeter

    def get_rect_properties(self):
        print("*******Rectangle********")
        print("Area = ", self.__rect_area())
        print("Circumference = ", self.__rect_perimeter())

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


class Square:
    def __init__(self, s=0):
        self.__side = s
        self.__area = 0
        self.__perimeter = 0

    def __sq_area(self):
        self.__area = self.__side * self.__side
        return self.__area

    def __sq_perimeter(self):
        self.__perimeter = 4 * self.__side
        return self.__perimeter

    def get_sq_properties(self):
        print("*******Square********")
        print("Area = ", self.__sq_area())
        print("Perimeter = ", self.__sq_perimeter())

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


class Triangle:
    def __init__(self, s1=0, s2=0, b=0, h=0):
        self.__side1 = s1
        self.__side2 = s2
        self.__breadth = b
        self.__height = h
        self.__area = 0
        self.__perimeter = 0

    def __tri_area(self):
        self.__area = 0.5 * self.__breadth * self.__height
        return self.__area

    def __tri_perimeter(self):
        self.__perimeter = self.__side1 + self.__side2 + self.__breadth
        return self.__perimeter

    def get_tri_properties(self):
        print("*******Triangle********")
        print("Area = ", self.__tri_area())
        print("Perimeter = ", self.__tri_perimeter())


class Parallelogram:
    def __init__(self, s=0, b=0, h=0):
        self.__side = s
        self.__base = b
        self.__height = h
        self.__area = 0
        self.__perimeter = 0

    def __para_area(self):
        self.__area = self.__base * self.__height
        return self.__area

    def __para_perimeter(self):
        self.__perimeter = 2*(self.__side + self.__base)
        return self.__perimeter

    def get_para_properties(self):
        print("*******Parallelogram********")
        print("Area = ", self.__para_area())
        print("Perimeter = ", self.__para_perimeter())


class Ellipse:
    def __init__(self, r1=0, r2=0):
        self.__major_axis = r1
        self.__minor_axis = r2
        self.__area = 0
        self.__perimeter = 0

    def __ell_area(self):
        self.__area = self.__major_axis * self.__minor_axis * 3.14
        return self.__area

    def __ell_perimeter(self):
        self.__perimeter = 2 * 3.14 * sqrt((((self.__minor_axis*self.__minor_axis)+(self.__major_axis*self.__major_axis))/2))
        return self.__perimeter

    def get_ell_properties(self):
        print("*******Ellipse********")
        print("Area = ", self.__ell_area())
        print("Perimeter = ", self.__ell_perimeter())


class Hexagon:
    def __init__(self, s=0):
        self.__side = s
        self.__area = 0
        self.__perimeter = 0

    def __hex_area(self):
        self.__area = ((3*sqrt(3))/2)*(self.__side * self.__side)
        return self.__area

    def __hex_perimeter(self):
        self.__perimeter = 6 * self.__side
        return self.__perimeter

    def get_hex_properties(self):
        print("*******Hexagon********")
        print("Area = ", self.__hex_area())
        print("Perimeter = ", self.__hex_perimeter())


class Rhombus:
    def __init__(self, d1=0, d2=0, s=0):
        self.__dig1 = d1
        self.__dig2 = d2
        self.__side = s
        self.__area = 0
        self.__perimeter = 0

    def __Rh_area(self):
        self.__area = (self.__dig1*self.__dig2)/2
        return self.__area

    def __Rh_perimeter(self):
        self.__perimeter = 4 * self.__side
        return self.__perimeter

    def get_Rh_properties(self):
        print("*******Rhombus********")
        print("Area = ", self.__Rh_area())
        print("Perimeter = ", self.__Rh_perimeter())


class Octagon:
    def __init__(self, s=0):
        self.__side = s
        self.__area = 0
        self.__perimeter = 0

    def __octa_area(self):
        self.__area = (2*(1+sqrt(2)))*(self.__side * self.__side)
        return self.__area

    def __octa_perimeter(self):
        self.__perimeter = 8 * self.__side
        return self.__perimeter

    def get_octa_properties(self):
        print("*******Octagon********")
        print("Area = ", self.__octa_area())
        print("Perimeter = ", self.__octa_perimeter())


class Pentagon:
    def __init__(self, s=0, a=0):
        self.__side = s
        self.__apothem = a
        self.__area = 0
        self.__perimeter = 0

    def __pen_area(self):
        self.__area = (self.__apothem * self.__side)/2
        return self.__area

    def __pen_perimeter(self):
        self.__perimeter = 5 * self.__side
        return self.__perimeter

    def get_pen_properties(self):
        print("*******Pentagon********")
        print("Area = ", self.__pen_area())
        print("Perimeter = ", self.__pen_perimeter())


s1 = Circle(10)
s1.get_cir_properties()
# s1.draw_circle()

s2 = Rectangle(20, 10)
s2.get_rect_properties()
# s2.draw_rect()

s3 = Square(50)
s3.get_sq_properties()
s3.draw_sq()

s4 = Triangle(10, 10, 10, 7)
s4.get_tri_properties()

s5 = Parallelogram(10, 7, 7)
s5.get_para_properties()

s6 = Ellipse(10, 8)
s6.get_ell_properties()

s7 = Hexagon(10)
s7.get_hex_properties()

s8 = Rhombus(10,10,7)
s8.get_Rh_properties()

s9 = Octagon(10)
s9.get_octa_properties()

s10 = Pentagon(3,2)
s10.get_pen_properties()
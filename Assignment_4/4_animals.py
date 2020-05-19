import abc
from abc import ABC, abstractmethod


# modularity achieved by defining separate functions for various tasks
# abstract class
class Herbivores(ABC):
    # abstract method/ pure virtual function
    def veg(self):
        pass


# Interface
class Carnivores(abc.ABC):
    @abc.abstractmethod
    def category(self):
        pass


# base class
# Hierarchy achieved as More than one classes inherits Animal class
class Animals():  # Encapsulation
    def __init__(self, legs=0, eyes=0, ears=0, tail=0):
        self.legs = legs
        self.eyes = eyes
        self.ears = ears
        self.tail = tail

    def _get_Properties(self):  # Protected Function (Abstraction)
        print("Legs = ", self.legs)
        print("Eyes = ", self.eyes)
        print("Ears = ", self.ears)
        print("Tail = ", self.tail)

    # Simple Virtual function
    def say(self):
        print("Unknown sound")


# derived classes
class Tiger(Animals, Carnivores):  # Encapsulation
    __claws = 0  # Private Variable or Property (Abstraction)

    def __init__(self):
        super().__init__(4, 2, 2, 1)
        self.__set_Properties()

    def __set_Properties(self):  # Private Function (Abstraction)
        self.__claws = 4

    def get_Properties(self):
        print("******************************")
        print("Tiger : ")
        super()._get_Properties()
        print("Claws on each paw = ", self.__claws)

    # Method Overriding (Polymorphism)
    def say(self):
        print("Tiger roars")

    # Abstract function from Carnivores Interface
    def category(self):
        print("Large Carnivores")


class Elephant(Animals):
    __trunk = 0  # Private Variable

    def __init__(self):
        super().__init__(4, 2, 2, 1)
        self.__set_Properties()

    def __set_Properties(self):  # Private Function
        self.__trunk = 1

    def get_Properties(self):
        print("******************************")
        print("Elephant : ")
        super()._get_Properties()
        print("Trunk = ", self.__trunk)

    # Method Overriding (Polymorphism)
    def say(self):
        print("Elephant says Pawooo")


class Dog(Animals):  # Encapsulation
    def __init__(self):
        super().__init__(4, 2, 2, 1)

    def get_Properties(self):
        print("******************************")
        print("Dog : ")
        super()._get_Properties()

    # Method Overriding (Polymorphism)
    def say(self):
        print("Dog says Bhoww")


class Turtle(Animals):  # Encapsulation
    __shell = 0

    def __init__(self):
        super().__init__(4, 2, 0, 1)

    def __set_Properties(self):
        self.__shell = 1

    def get_Properties(self):
        print("******************************")
        print("Turtle : ")
        super()._get_Properties()
        print("Shell = ", self.__shell)


class Monkey(Animals):  # Encapsulation
    __hands = 0

    def __init__(self):
        super().__init__(2, 2, 2, 1)

    def __set_Properties(self):
        self.__hands = 2

    def get_Properties(self):
        print("******************************")
        print("Monkey : ")
        super()._get_Properties()
        print("Hands = ", self.__hands)


class Cow(Animals, Herbivores):  # Encapsulation
    def __init__(self):
        super().__init__(4, 2, 2, 1)

    def get_Properties(self):
        print("******************************")
        print("Cow : ")
        super()._get_Properties()

    # Abstract class implementation
    def veg(self):
        print("Cow is Herbivores")


class Horse(Animals, Herbivores):  # Encapsulation
    def __init__(self):
        super().__init__(4, 2, 2, 1)

    def get_Properties(self):
        print("******************************")
        print("Horse : ")
        super()._get_Properties()

    # Abstract class implementation
    def veg(self):
        print("Horse is Herbivores")


class Bull(Animals, Herbivores):  # Encapsulation
    def __init__(self):
        super().__init__(4, 2, 2, 1)

    def get_Properties(self):
        print("******************************")
        print("Bull : ")
        super()._get_Properties()

    # Abstract class implementation
    def veg(self):
        print("Bull is Herbivores")


class Wolf(Animals):  # Encapsulation
    def __init__(self):
        super().__init__(4, 2, 2, 1)

    def get_Properties(self):
        print("******************************")
        print("Wolf : ")
        super()._get_Properties()


class Hen(Animals):  # Encapsulation
    def __init__(self):
        super().__init__(2, 2, 2, 1)

    def get_Properties(self):
        print("******************************")
        print("Hen : ")
        super()._get_Properties()


a = Animals()
a.say()     # base class method
a1 = Tiger()
a1.get_Properties()
a1.say()    # Overridden method
a2 = Elephant()
a2.get_Properties()
a2.say()    # Overridden method
a3 = Dog()
a3.get_Properties()
a3.say()    # Overridden method
a4 = Turtle()
a4.get_Properties()
a5 = Monkey()
a5.get_Properties()
a6 = Cow()
a6.get_Properties()
a6.veg()
a7 = Horse()
a7.get_Properties()
a7.veg()
a8 = Bull()
a8.get_Properties()
a8.veg()
a9 = Wolf()
a9.get_Properties()
a10 = Hen()
a10.get_Properties()

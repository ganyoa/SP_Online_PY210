#!/usr/bin/env python3

from math import pi


class Circle(object):

    def __init__(self, radius):
        self.radius = radius

    def __repr__(self): #step 6
        return 'Circle({})'.format(self.radius)

    def __str__(self): #step 6
        return 'Circle with radius: {}'.format(self.radius)

    @property
    def radius(self):
        return self._radius # _x is an internal value

    @radius.setter # needed to see radius attribute
    def radius(self, rad):
        if rad < 0:
            raise ValueError("radius can't be less than zero")
        self._radius = rad

#step 2, 3
    @property
    def diameter(self):
        return 2 * self._radius

    @diameter.setter
    def diameter(self, rad):
        self.radius = rad / 2

#step 4
    @property
    def area(self):
        return pi * self._radius**2

    @area.setter
    def area(self, area):
        raise AttributeError('Cannot set area')

#step 5
    @classmethod
    def from_diameter(cls , dia):
        return cls(dia / 2)

#step 7
    def __add__(self, other):
        return Circle(self.radius + other.radius)

    def __mul__(self, other):
        return Circle(self.radius * other)

#step 8
    def __gt__(self, other):
        return self.radius > other.radius

    def __lt__(self, other):
        return self.radius < other.radius

    def __eq__(self, other):
        return self.radius == other.radius

    def sort_key(self):
        return self.radius

#step 9
class Sphere(Circle):

    def __repr__(self): #step 6
        return 'Sphere({})'.format(self.radius)

    def __str__(self): #step 6
        return 'Sphere with radius: {}'.format(self.radius)

    @property
    def volume(self):
        return ((4/3) * pi * self.radius**3)

    @property
    def area(self):
        return (4 * pi * self.radius**2)
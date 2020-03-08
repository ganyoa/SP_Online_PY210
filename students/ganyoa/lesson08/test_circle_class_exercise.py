from circle_class_exercise import *

def test_radius():
    c = Circle(4)
    assert c.radius == 4

def test_diameter():
    c = Circle(4)
    assert c.diameter() == 8
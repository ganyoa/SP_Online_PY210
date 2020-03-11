from circle_class_exercise import *

#step 1
def test_radius():
    c = Circle(4)
    assert c.radius == 4

#step 2
def test_diameter():
    c = Circle(4)
    assert c.diameter == 8

#step 3
def test_diameter_to_radius():
    c = Circle(4)
    c.diameter = 20
    assert c.radius == 10

#step 4
def test_area():
    c = Circle(2)
    assert c.area == 12.566370614359172

#step 5
def test_from_diameter():
     c = Circle.from_diameter(8)
     assert c.diameter == 8
     assert c.radius == 4
     assert c.area == 50.26548245743669

#step 6
def test_print():
    c = Circle(32)
    assert c.__str__() == 'Circle with radius: 32'
    assert c.__repr__() == 'Circle(32)'

#step 7
def test_add():
    c1 = Circle(2)
    c2 = Circle(4)
    assert repr(Circle(6)) == repr(c1 + c2)

def test_mul():
    c2 = Circle(4)
    assert repr(c2 * 3) == repr(Circle(12))

#step 8
def test_comparisons():
    c1 = Circle(5)
    c2 = Circle(7)
    c3 = Circle(7)
    assert c2 > c1
    assert c2 == c3

def test_sort():
    a_list = [Circle(6), Circle(7), Circle(8), Circle(4), Circle(0), Circle(2), Circle(3), Circle(5), Circle(9), Circle(1)]
    b_list = a_list[:]
    a_list.sort()
    assert a_list == [Circle(0), Circle(1), Circle(2), Circle(3), Circle(4), Circle(5), Circle(6), Circle(7), Circle(8), Circle(9)]
    assert sorted(b_list, key=Circle.sort_key) == [Circle(0), Circle(1), Circle(2), Circle(3), Circle(4), Circle(5), Circle(6), Circle(7), Circle(8), Circle(9)]

#step 9
def test_sphere_print():
    s = Sphere(32)
    assert s.__str__() == 'Sphere with radius: 32'
    assert s.__repr__() == 'Sphere(32)'

def test_sphere_rad():
    s = Sphere(5)
    assert s.radius == 5

def test_sphere_vol():
    s = Sphere(5)
    assert s.volume == 523.5987755982989

def test_sphere_area():
    s = Sphere(5)
    c = Circle(2)
    assert s.area == 314.1592653589793
    assert c.area == 12.566370614359172

def test_sphere_comparisons():
    s1 = Sphere(5)
    s2 = Sphere(7)
    s3 = Sphere(7)
    assert s2 > s1
    assert s2 == s3

def test_sphere_diameter_to_radius():
    s = Sphere(4)
    s.diameter = 20
    assert s.radius == 10

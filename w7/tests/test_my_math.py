import pytest
import math
import cmath
import numpy as np
from my_mathematics.math import MyMath
from my_mathematics.math import MyComplexMath
from my_mathematics.linear_algebra import Vector

def test_sin():
    assert MyMath.sin(2) == math.sin(2)
    assert MyMath.sin(1) == math.sin(1)
def test_sqrt():
    assert MyMath.sqrt(9) == math.sqrt(9)

def test_complex():
    assert MyComplexMath.sqrt(-4) == (cmath.sqrt(-4).real, cmath.sqrt(-4).imag)


def test_dictance():
    x1 = Vector(1,2,3)
    assert x1.dictances() == np.linalg.norm([1,2,3])
    x2 = Vector(3,-4,5)
    assert x2.dictances() == np.linalg.norm([3, -4, 5])
def test_add_():
    x1 = Vector(1,2,3)
    x2 = Vector(3,-4,5)
    numpy_1 = np.array([1,2,3])
    numpy_2 = np.array([3,-4,5])
    add1 = x1 + x2
    add2 = numpy_1 + numpy_2
    assert add1[0] == add2[0]
    assert add1[1] == add2[1]
    assert add1[2] == add2[2]


def test_sub_():
    x1 = Vector(1,2,3)
    x2 = Vector(3,-4,5)
    numpy_1 = np.array([1,2,3])
    numpy_2 = np.array([3,-4,5])
    sub1 = x1 - x2
    sub2 = numpy_1 - numpy_2
    assert sub1[0] == sub2[0]
    assert sub1[1] == sub2[1] 
    assert sub1[2] == sub2[2] 

def test_and_():
    x1 = Vector(2,3,5)
    x2 = Vector(0,3,11)
    numpy_1 = np.array([2,3,5])
    numpy_2 = np.array([0,3,11])
    and1 = x1 & x2
    and2 = np.dot(numpy_1, numpy_2)
    assert and1 == and2

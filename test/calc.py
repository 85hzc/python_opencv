#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import math
import cmath

def sqrt(x, y):
    try:
        y = math.sqrt(y)
        print(y)
    except ValueError:
        y = cmath.sqrt(y)
        print(y)

def add(x, y):
    return print(x + y)

def subduction(x, y):
    return print(x - y)

def multiplication(x, y):
    return print(x * y)



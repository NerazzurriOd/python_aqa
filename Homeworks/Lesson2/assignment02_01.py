#!/usr/bin/python3

# Assignment 02-01
#
# Task: Implement cylinder volume formula:
#
# Formula: V=pi*r*r*h, where
#
#          V - volume of cylinder
#          pi - pi math constant
#          r - radius of the circular base
#          h - height of cylinder

pi = 3.14
r = 15
h = 75
v = pi * r**2 * h

print(f"Volume of cylinder with radius r={r} and height h={h}: {v}")

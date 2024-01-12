#Given two interior angles (in degrees) of a triangle.
#Write a function to return the 3rd.

def other_angle(a, b):
    other_angle = 180 - a -b
    return other_angle
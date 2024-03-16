import math
def circleArea(r):
    r=float(r)
    s=math.pi*(r**2)
    return s

print("{:.6f}".format(circleArea(input())))
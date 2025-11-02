#sphere dimensions
import math
#to use pi and power

print("Get the dimensions of a sphere")

print("radius?")
radius = input()
# input
radius = float(radius)
surface_area = 4 * math.pi * math.pow(radius, 2)
volume = (4 * math.pi * math.pow(radius, 3)) / 3
ratio = volume / surface_area
# conversion
surface_area = str(round(surface_area))
volume = str(round(volume))
ratio = str(round(ratio))
print("surface area: ", surface_area)
print("volume: ", volume)
print ("ratio :", ratio)
#output
import math

def vol(rad):
	# Write a function that computes the volume of a sphere given its radius
	return 4/3*math.pi*rad**3

obj_kuli = vol(2)
print(obj_kuli)
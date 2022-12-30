# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Anderdon Wayne Loan
# Section: 574
# Assignment: 2.1 LAB more linear interpolation
# Date: 05/09/22#


from math import*
#finds initial positions for x,y,z
x_slope = (-5-8)/(85-12)
y_slope = (30-6)/(85-12)
z_slope = (9-7)/(85-12)
time = 30.0
meters_x = x_slope * (time-12) + 8
meters_y = y_slope * (time-12) + 6
meters_z = z_slope * (time-12) + 7
print("At time 30.0 seconds: ")
print("x1 = " + str(meters_x) + " m")
print("y1 = " + str(meters_y) + " m")
print("z1 = " + str(meters_z) + " m")
print("-----------------------")
#finds second positions for x,y,z
time = 37.5
meters_x = x_slope * (time-12) + 8
meters_y = y_slope * (time-12) + 6
meters_z = z_slope * (time-12) + 7
print("At time 37.5 seconds: ")
print("x2 = " + str(meters_x) + " m")
print("y2 = " + str(meters_y) + " m")
print("z2 = " + str(meters_z) + " m")
print("-----------------------")
#finds third positions for x,y,x
time = 45.0
meters_x = x_slope * (time-12) + 8
meters_y = y_slope * (time-12) + 6
meters_z = z_slope * (time-12) + 7
print("At time 45.0 seconds: ")
print("x3 = " + str(meters_x) + " m")
print("y3 = " + str(meters_y) + " m")
print("z3 = " + str(meters_z) + " m")
print("-----------------------")

#finds fourth positions for x,y,z
time = 52.5
meters_x = x_slope * (time-12) + 8
meters_y = y_slope * (time-12) + 6
meters_z = z_slope * (time-12) + 7
print("At time 52.5 seconds: ")
print("x4 = " + str(meters_x) + " m")
print("y4 = " + str(meters_y) + " m")
print("z4 = " + str(meters_z) + " m")
print("-----------------------")
#finds fifth positions for x,y,z
time = 60.0
meters_x = x_slope * (time-12) + 8
meters_y = y_slope * (time-12) + 6
meters_z = z_slope * (time-12) + 7
print("At time 60.0 seconds: ")
print("x5 = " + str(meters_x) + " m")
print("y5 = " + str(meters_y) + " m")
print("z5 = " + str(meters_z) + " m")




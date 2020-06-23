from math import tan, pi
s=int(input("num of sides"))
l= float(input("length of a side: "))
a= s*(l** 2) / (4 * tan(pi/s))
print("area of polygon ",a)
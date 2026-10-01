#WAP to enter the coefficients of a quadratic equation and findout its roots of the equivalents.
import math
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))  
d =math.sqrt(b**2 - 4*a*c)
root1 = (-b + d) / (2*a)
root2 = (-b - d) / (2*a)
print("Root 1:", root1)
print("Root 2:", root2)

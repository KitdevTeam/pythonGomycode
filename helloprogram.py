###Python test code Nouha Mbarek
""" cardinalité inf prend la clé primaire du plus forte cardinalité
print("hello world")

print("******************checkpoint 7 ****************")
import math
import numpy as np
c=50
h=50
d=input("taper une valeur : \n").split(",")
for i in range(0,len(d)):
 Qs=[math.sqrt((2*c*int(d[i]))/h) for i in range(0,len(d))]
print("result : ",Qs)

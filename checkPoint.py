### checkQuestion 1:
print("******************checkpoint 1 ****************")
for i in range(2000,3200):
        if (i%7==0) & (i%5 != 0):
            print("voila un numero :",i)

print("******************checkpoint 2 ****************")
###checkPoint 2:
def factorieln(ent):
        p=1
        if ent == 0:
            p=1
        else:
            for c in range(1,ent+1):
                p= p*c
            print("le calcul donne :",p)
        return p

print(factorieln(int(input('entrer un nombre :'))))

###checkPoint 3 :
print("******************checkpoint 3 ****************")

dict = {i:i*i for i in range(1,int(input("entrer un entier :")))}
print(dict)

###checkPoint 4 :
print("******************checkpoint 4 ****************")

str= input("say something :")
for i in range(0,len(str)):
    print("result :"+str.replace(str[i],''))

###checkPoint 5 :
print("******************checkpoint 5 ****************")
print(" => convert an array to list with python <= \n ")

import numpy as np
tab = np.array([[1, 2], [3, 4]])
list= tab.tolist()
print("le tableau converti :",list)
### autrement
ligne= int(input("nombre des lignes :"))
cols= int(input("nombre des colonnes :"))
arr = [[int(input("donner une valeur"))] * cols for i in range(ligne)]
tab= np.array(arr)
print(tab.tolist())

###checkPoint 6 :
print("******************checkpoint 6 ****************")
print(" => Calculate a CovMatrix with python <= \n ")
import numpy as np
dim= int(input("dimension du tableau 1D : \n"))
tab =np.array([[int(input("taper une valeur :")) for i in range(dim)]*dim for j in range(dim)])
print("matrix covariante de tab :",np.cov(tab))


###checkPoint 7 :
print("******************checkpoint 7 ****************")
import math
import numpy as np
c=50
h=50
d=input("taper une valeur : \n").split(",")
for i in range(0,len(d)):
 Qs=[math.sqrt((2*c*int(d[i]))/h) for i in range(0,len(d))]
print("result : ",Qs

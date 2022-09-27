# tuples data type : ordered, inmutable, allows duplicate
tuple_org=(1,2,3,4,5) 

#a tuple with just one element is a designación de variable

tupla_1= tuple([1,2,3]) #tupla desde una lista

item=tupla_1[0] #acceso a elementos
item=tupla_1[-1] #último elemtento

# una tupla no puede ser modificada

for i in tupla_1:
    print(i)

for 2 in tupla_1:
    print('yes')

lenght=len(tupla_1) #cantidad de elementos

contar=tupla_1.count(2) #cuenta cantidad de elementos del argumento en la tupla
indice=tupla_1.index(1) #devuelve el índice del elemento

lista=[5,6,3,7]
tupla=tuple(lista) #convertir lsita en tupla y viceversa

b=(1,2,3,4,5,6,7,8,9,10)
c= b[2:5] #slicing tupla del 2 al 4
d=b[:5] #del origen al 4
e=b[::-1] #reverse tuple

tupla_crear=('Chela', 97, 'MDQ')
name , age, city = tupla_crear

#con este método, se asigna en lugar de un índice, una clave para acceder a la info de la tupla

e= (0,1,2,3,4,5,6,7,8,9,10,11,12)
i1, * i2 ,i3 = e   #*i2 representa los elementos internos de la tupla

#working with utples are more efficient, specially with large data sets

import sys

a = [0,1,2,3,4,5,6,7,8,9,10]
b = tuple(a)

print(sys.getsizeof(a))
print(sys.getsizeof(b))  #both have the same amount of elements, but not the same size


import timeit
timeit.timeit(stmt='[0,1,2]', number=[100000])
timeit.timeit(stmt='(0,1,2)', number=[100000]) #creating same amount of elements in tuples or lists takes different times


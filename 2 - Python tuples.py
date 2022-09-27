# tupla: Data type ordenado, inmutable, permite duplicados
#creación de tupla
tupla_1=(1,2,3,4,5) #forma explícita

tupla_2=("Hello") #Una tupla con un solo elemento será como designar un solo elemento a una variable
                  #en este caso, pertenecerá a la clase string.

tupla_3= tuple([1,2,3]) #convierte en tupla una lista

tupla_4=('Chela', 97, 'MDQ')  #con este método, se asigna en lugar de un índice, una clave para acceder a la info de la tupla
name , age, city = tupla_4

#-----
#Acceso a elementos de una tupla
item_1=tupla_1[0] #acceso a elementos
item_ultimo=tupla_1[-1] #último elemtento

# una tupla no puede ser modificada
#----
# Recorriendo una tupla con for
for i in tupla_1:
    print(i)
#----    
e= (0,1,2,3,4,5,6,7,8,9,10,11,12)
e1, * e2 ,e3 = e   #*i2 representa los elementos internos de la tupla
#----

# Buscando elementos en tupla
for 2 in tupla_1:
    print('yes')
#----
#Métodos de tuplas
lenght=len(tupla_1) #cantidad de elementos

contar=tupla_1.count(2) #cuenta cantidad de elementos iguales al argumento 
indice=tupla_1.index(1) #devuelve el índice del elemento
#----

# Slicing
b=(1,2,3,4,5,6,7,8,9,10)
c= b[2:5] #slicing tupla del 2 al 4
d=b[:5] #del origen al 4
e=b[::-1] # elige el rango completo, y la devuelve en orden inverso


#trabajar con tuplas es más eficiente que trabajar con listas:
import sys

x = [0,1,2,3,4,5,6,7,8,9,10]
y = tuple(x)

print(sys.getsizeof(x))
print(sys.getsizeof(y))  #ambas lista y tupla, tienen la mista cantidad de elementos, pero no el mismo tamaño


import timeit
timeit.timeit(stmt='[0,1,2,3,4,5]', number=[500000])
timeit.timeit(stmt='(0,1,2,3,4,5)', number=[500000]) #crear una cantidad muy grande de listas y tuplas, por más que tengan 
                                                     #los mismos elementos, las listas tardan más en crearse.


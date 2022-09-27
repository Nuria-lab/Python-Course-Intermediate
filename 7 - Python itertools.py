# iter tools: product, premutation, combination, accumulate, groupby, infinite iterators
# product

# from itertools import product
# a = [1,2]
# b = [3,4]
# c = list(product(a, b, repeat=1))     #combinación de todos los productos posibles en fomaa de lista (cada producto como tupla)
# print(c)                             #computa el producto cartesiano de los imputs iterables

# from itertools import permutations    #retorna todos los posibles ordenes de un input
# d =[1,2,3]
# p=list(permutations(d, 2))  #con el 2 en el argumento, ve las permutaciones en grupos de a 2
# print(p)

# from itertools import combinations, combinations_with_replacement  #make combinations in a specified lenght
# e=[1,2,3,4]
# c = list(combinations(e,3))   #el segundo argumento implica la cantidad de elementos de la combinación
# print(c)                      #no hay repeticiones

# d= list(combinations_with_replacement(e,3)) #halla las combinaciones posibles repitiendo numeros de
# print(d)                                    #la lista, la cantidad de elementos del segundo argumento

# from itertools import accumulate   #va sumando el valor de una posición con el de la anterior

# e=[1,2,3,4]
# a= accumulate(e)
# print(list(a))   

# from itertools import accumulate
# import operator
# e=[1,2,3,4]
# a= list(accumulate(e, func=operator.mul))   #en lugar de sumar, va a ir acumulando multiplicaciones
# print(a)

# from itertools import groupby    #retorna una lista con el filtro deseado

# def smaller_than(x):
#     return x < 3

# e=[1,2,3,4]
# g= groupby(e, key=smaller_than)

# for key,value in g:
#     print(key, list(value))

# from itertools import groupby
# personas=[{'name':'Tim', 'age':25},{'name':'Lisa', 'age':27},{'name':'Dan', 'age':25},{'name':'Claire', 'age':28}]

# group= groupby(personas, key=lambda x: x['age'])

# for key, value in group:
#     print(key, list(value)) #no me funciona
    

from itertools import count, cycle, repeat

# for i in count(10):  #imprime a partir de 10, de uno en uno
#     print(i)
#     if i == 15:
#         break

# a=[1,2,3]
# for i in cycle(a):
#     print(i)       #repite la lista infinitamente


for i in repeat(1, 4):
     print(i)        #repite el 1, cuatro veces


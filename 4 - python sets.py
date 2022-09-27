#SETS : unorderer, mutable, no duplicates
#creando sets

set_1= {1,2,3,4,5,6}
set_2=set([7,8,9,10])
set_3=set('Hello world') #imprime cada palabra por separado en un lugar del set, en cualquier orden, pero NO IMPRIME VALORES DUPLICADOS
set_4=set()  #método para crear sets vacíos

set_5=set()
set_5.add(1)
set_5.add(2)
set_5.add(3) #maneras de agregar valores al set

set_5.remove(3) #elimina el elemento del argumento
set_5.discard(2) #también elimina, pero si no lo encuentra no corta el programa

set_5.clear() #elimina todo del set
set_5.pop()

#---
for i in set_1:
    print(i)
#---
if 1 in set_1:
    print('yes')
#----

odds = {1,3,5,7,9}
even = {0,2,4,6,8}
primes={2,3,5,7}

u = odds.union(even) #union de dos sets
i = odds.intersection(primes) #marca los elementos iguales de ambos sets


#-----
#resta de sets
set_6={1,2,3,4,5,6,7,8,9}
set_7={1,2,3,10,11,12}

diff_1 = set_6.difference.set_7() #devuelve {4,5,6,7,8,9}, resta de la primera, elementos iguales de la segunda.
diff_2=set_7.symmetric_difference(set_6) #devuelve un set con todos los elementos menos los comunes entre sí.
#----

set_6.update(set_7)  # renueva el set con los elementos nuevos no repetidos
set_6.intersection_update(set_7) #el set se queda solo con los elementos iguales
set_6.difference_update(set_7) #el set se queda con sus elementos menos los repetidos
set_6.symmetric_difference_update(set_7) #el set se queda con los elementos de ambos, menos los repetidos

#----
set_8={1,2,3,4,5,6}
set_9={1,2,3}

set_9.issubset(set_8) #devuele True, si 9 está incluido en 8
set_8.issupetset(set_9) #devuelve True, si 8 contiene a 9
set_9.isdisjoint(set_8)

# ---

a= frozenset([1,2,3,4]) # inmutable







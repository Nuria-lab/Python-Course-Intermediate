#listas : colección de datos ordenada y mutable. Permite elementos duplicados
#Creación de listas
lista=[-1,5,10,20]    # creación explícita de lista

lista_vacia=list()    # creación de lista con el método list()

a= [1,2,3,4,5,6]
b= [i*2-1 for i in a] #creando una lista con elementos desde otra lista, por una expresión

lista_nueva_1=[0] * 5 #crea una lista del mismo elemento 5 veces

lista_nueva_2=lista + lista_nueva_1  #crea una nueva lista con la suma vectorial de las dos
cacho_de_lista=lista[0:2] #crea una nueva lsita de una lista anterior pero un cacho de ella
cacho_de_lista_2=lista[::-1] #nueva lista de lista, en un rango, -1 la ordena del mayor indice al menor
lista_nueva_nueva=lista.copy() #copy method que no genera enlace entre las dos listas
lista_nueva_nuevaa=list(lista) #tambien copia lista sin modificar la original
lista_nuevaaaa=lista[:]
#-------
#Acceder a elemento por índice
item_1 = lista[0] #primer elemento
item_ultimo=lista[-1] #último elemento
item_anteultimo=lista[-2] #penúltimo elemento
#------

#Recorriendo una lista con for
for i in lista:
    print(i) #i es la ubicación del elemento
    
#-----
#Buscando datos en una lista
if 5 in lista:
    print('si')
else:
    print ('no')
#-----
# Métodos de listas: funciones que pueden aplicarse a lista

len(lista) #cantidad de elementos de la lista

lista.append(7) #añade al final
lista.insert(-1,8) #añade a (posición,elemento)
lista.pop() # muestra y elimina el último elemento agregado
lista.remove(7) #elimina el elemento del argumento
lista.clear() #elimina todo y queda una lista vacía
lista.reverse() #ordena de mayor a menor
lista.sort() #ordena de menor a mayor


lista_nueva_2=lista + lista_nueva_1  #crea una nueva lista con la suma vectorial de las dos
cacho_de_lista=lista[0:2] #crea una nueva lsita de una lista anterior pero un cacho de ella
cacho_de_lista_2=lista[::-1] #nueva lista de lista, en un rango, -1 la ordena del mayor indice al menor
lista_nueva_nueva=lista.copy() #copy method que no genera enlace entre las dos listas
lista_nueva_nuevaa=list(lista) #tambien copia lista
lista_nuevaaaa=lista[:]


 


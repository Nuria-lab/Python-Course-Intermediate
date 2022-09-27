# diccionarios: CLAVE:VALOR , desordenados, mutables

#formas de crear un diccionario
dict_1={'name': 'Nu', 'age' : 36, 'email': 'loquesea@xyz.com'} #creando un diccionario 1

dict_2 = dict (name='Nu', age= 36, loc = 'LP') #creando un diccionario 2

#acceder a los valores por key

valor_a= dict_1['name'] #busca la clave 'name' y devuelve el valor que hay en ella
                        #si la key no está en el dict, será comunicado por error

#agregando valores:
dict_1['email'] = 'loquesea@gmail.com' #si la key ya existe, saltará error

# eliminando valores

del dict_1['name'] #elimina el par del diccionario por clave

dict_1.pop('age')  #elimina el par por clave

dict_1.popitem()   #elimina el último agregado

# recorriendo

if 'name' in dict_1:
    print(dict_1['name'])  #imprime todos los valores que hay en la clave de búsqueda


try:
    print(dict_1['name'])   # no deja de ejecutar el programa cuando hay un error

except: 
    print('error - nor found') #key error

#----

for key in dict_1.keys():    #puede ser también for key in dict_1 (imprime normalmente)
    print(key)      #imprime todos las claves que hay en el diccionario como una lista

#----

for value in dict_1.values():   
    print(value)            #iprime los valores

#---

for key, value in dict_1.items():   #imprime las parejas key:value
    print(key, value)   

#---

#copying

dict_1_cpy= dict_1.copy()

dict_1_cpy2=dict(dict_1)

#----

dict_1.update(dict_2)  #las claves iguales quedan, pero se actualizan las nuevas sobre dict_1

#---
tupla=(8,9)
dict_3={tupla:15}   #puede usarse una tupla como key en diccionario (??), pero no una lista
















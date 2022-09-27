#lambda arguments: expressions
#we use lamda when we use that function once in our code


# #add func
# add10 = lambda x: x+10 
# print(add10(5))            #añade 10 a un x

# #similar to
# def add10_func(x):
#     return x+10    #lamda func is shorter in one line

###----

# mult = lambda x,y: x*y
# print(mult(2,7))

##---
list_points=[(1,2),(15,1),(5,-1),(10,4)]
sorted_list_points_1= sorted(list_points, key= lambda x: x[1])  #los pone de menor a mayor según y

print(sorted_list_points_1)


#similar to use this function
# def sort_by(y):
#     return y[1] #la segunda posición es la que va al sorted. en lugar de lamda en key
#                 #se pone el nombre de esta función.

# otra
# sorted_list_points_2= sorted(list_points, key= lambda x: x[0] + x[1])    #x viene a ser la lista de donde salen los datos
# print(sorted_list_points_2)


#---- map function
# a= [1,2,3,4,5]
# b= map(lambda x: x+2, a)    #map function
# print(list(b)) 

# #same as
# c= [x+2 for x in a]
# print(c)

# ----filter function----
# a= [1,2,3,4,5,6]
# b=filter(lambda x: x%2 == 0,a)
# print(list(b))     

# c= [x for x in a if x % 2 == 0]   # + facil
# print(c)


#---
from functools import reduce
from itertools import product
a= [1,2,3,4]
product_a= reduce(lambda x,y: x*y, a)
print(product_a)    #va multiplicando el primero por el segundo, hasta llegar al último y muestra eso

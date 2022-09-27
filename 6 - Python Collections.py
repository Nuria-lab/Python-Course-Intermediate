#collections module: counter, namedtuple, orderedDirect, defaultdict, deque

from collections import Counter

a= 'aaabbbccc'
counter_char= Counter(a)  #devuelve un diccionario con cada letra y su conteo
a.counter.keys() #devuelve una letra de cada
a.counter.values() #devuelve conteo de cada letra
a.most_common() #devuelve moda. si dentro del arg se pone num int, (1)-> más repetido, (2) -> segundo más repetido, etc
lista=list(a.elements()) #devuelve cada elemento dentro de una lista
#---
#namedtuple

from collections import namedtuple

Point= namedtuple ('Point', 'x,y')
pt= Point(1,-4)
print(pt.x, pt.y)

#--
# order Dict
from collections import OrderedDict

ordered_dict= OrderedDict()   #crea un dict ordenado
ordered_dict['a'] = 1
ordered_dict['b'] = 2
ordered_dict['c'] = 3
ordered_dict['d'] = 4
ordered_dict['e'] = 5

#--
# default dict

from collections import defaultdict

d= defaultdict(int)  #devuelve 0 si no existe
d['a'] = 1
d['b'] = 2

#---
d= defaultdict(float) #devuelve 0.0 si no existe
d['a'] = 1
d['b'] = 2

#----
#deque

from collections import deque
d=deque()  #devuelve lista
d.append(1)
d.append(2)
d.appendleft(0) #pone elementos en el punto0
 
d.pop() #remove last element
d.popleft() #remueve primer elemento
d.extend([4,5,6]) #igual que extend lista
d.extendleft({-1,0})


d.rotate()  #invierte

#cadenas: ordenadas, inmutable, representación de texto

from codecs import latin_1_decode


cadena='Hola mundo'
char = cadena[0] #primer elemento
subst = cadena[0:5] #slicing

programa= 'python'

concatenate_str= 'I say ' , cadena, 'con', programa

#--
if 'a' in 'cadena':
    print('yes')
#--

a= '    Holi   '
a = a.strip() # removes extra spaces
#----
#convertir
a= 'Hello World'
a.upper()  #convierte todo a may
a.lower()  #convierte todo a low


#---
a.startswith('Hello') #true 
a.endswith('World')   #true
#---
a.find('o') #looks for the first appearene, return index. also works for substring
a.count('o') #counts the amount of char
a.replace('World', 'Universe') #return hello universe
#---

b='How are you doing?'
l=a.split(' ')  #convierte cadena en elementos de una lista - busca espacios
l2=a.split(',') #comma delimiter
c=' '.join(l2) #convierte a una lsita sin espacios
#---
l_1=[a] * 5
d=' '.join(l_1)

#---
#formating
# %, format(), f-strings

#%
var_1='Tom' 
string_1= 'The variable is %s' % var_1  #para cadenas
 
var_2= 9
string_2= 'The variable is %d' % var_2  #para numerosenteros

var_3= 3.14
string_3= 'Pi is %.2f' %var_3 #para float (.2 indica '2' digitos del float)

# format()

var_4 = 3.1416
var_5= 2.18
string_4 = 'Pi is {:.2f} and e is {}'.format(var_4, var_5)  # (:.f indica cantida de decimales)

# f.string --> recommended
var_4 = 3.1416
var_5= 2.18
string_4 = f'Pi is {var_4} and e is {var_5}'

#f string
var_6= 7.5
string_5=f'El resultado es {var_6+2}'   #pueden ponerse operaciones

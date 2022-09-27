# OOP = OBJECT ORIENTED PROGRAM
from re import T
from xml.dom.expatbuilder import theDOMImplementation


x = 1
type(x) 
#return a CLASS. Diferent datatypes, but they are part of a class

def hello():
    print('Hello')

type(hello) #--> CLASS : function. 

#those are all object of an specific class.
#that CLASS that the object belongs, specifies what we can do with the object.

x=1
y='hello'
# print(x + y) #will introduce an error bc we can't mix those classes
#the operation is not allowed for mixing those classes

cadena='hello'
CADENA=cadena.upper()  #a method for strings. 
                       #is a method acting for an specific object (cadena)
                       #but this method cant be applied on all classes

#how to create an own class?

class Dog:     #own classs, and define operation that dog is able to do

    def __init__(self, name,age):  #special method: instantiate the object once it is created
        self.name=name
        # print(name)            #and it will be called everytime a variable is asign to the class.
        self.age= age                #and everything writed on the argument will pass to this method
                        # the 'name' part, means that when we asign a class to a variable,
                        #we need to write something on the argument, in this case would be
                        #the name of the dog. name is an ATTRUBUTE of the class. this means
                        #all the time we create an object of dog, we need to pass the name, and will
                        #be stored


    # def meow(self):
    #     return 'meaow'   #you can return or print

    def bark(self):       #this is a method: a function inside of a class.
        print('bark')

    def add_one(self, x):  #when this method is called, we need to pass an specific value of x
        return x+1

    def get_name (self):
        return self.name

    def get_age(self):  #self point to variable we are requesting about
        return self.age  

    def set_age(self, age):   #this allows to change attributes
        self.age=age

 
d1= Dog('tim',3)   #we have a variable d, and asign it to a instance of the class dog (with the parenthesis)
           # d is now an object that is type Dog
d1.set_age(4) #this would change the attribute 'age' for d1
print(d1.get_age())  #this will print the attribute 
d2= Dog('Charlie',5)  #another instance of Dog
# print(type(d))
#print(d2.get_name())
# it will print <class '__main__.Dog'> the __main__ is telling us what module this class was defined in
# by default, the module is the __main__ module.
#if d is class Dog, d will be allowed to do everything listed on 'Dog' class. One of those operations is 'bark()' (a method)

# d.bark()   #asigning a method to d. Of course, that method must be included on the functions allowed on the class defined.

# d1 y d2 are two objects of class DOG, and both are 'saved' in dog class

dogs_name=["Tim","Bill"]
dogs_age = [3,5]    #difficult to access to data (find indexes)

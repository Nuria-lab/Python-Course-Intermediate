# INHERITANCE -> two classes very similar
#when two classes are very similar, in this case both are the same, they just differenciate on the speak.
#so we remove __init__ from both, and create a new class, pet, which defines the animal

class Pet:  #generalization
    def __init__(self,name,age):
        self.name=name
        self.age=age
    
    def show(self):
        print(f"I'm {self.name} and I'm {self.age} years old" )

class Cat(Pet):  #inherit: linking pet with cat
    # def __init__(self,name,age):
    #     self.name=name
    #     self.age= age
    def __init__(self,name,age,color):
        super().__init__(name,age)    #this stands for the __init__ on pet class, name and age would be defined there. super() is superclass(inherit)
        self.color=color

    def speak(self):
        print('Meow')
    
    def show(self):
        print(f"I'm {self.name} and I'm {self.age} years old, and I'm {self.color}")


class Dog(Pet):  #linking pet with dog
    # def __init__(self,name,age):
    #     self.name=name
    #     self.age= age

    def speak(self):
        print('Bark')


p= Pet("Pipi", 7)
p.show()
print(type(p))

c= Cat("Lunita", 8, "white")  #the first two are computed in pet, the white part is computed from cat class
c.show()
print(type(c))
c.speak()

d=Dog("Bobbi",7)
d.show()
print(type(d))
d.speak()
#so far, a class object 'pet' can't speak.

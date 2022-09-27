#class attributes: specific to the class, not to the object

class Person:
    gravity=-9.8
    number_of_people = 0  #attribute to the class, no the instance. helps with constant values

    def __init__(self,name):
        self.name=name
        Person.add_person()
    
    @classmethod           #this method is not for an instance, is for the class itself.
    def amount_of_people(cls):
        return cls.number_of_people

    @classmethod
    def add_person(cls):
        cls.number_of_people+=1

p1=Person("Nu")
p2=Person("Cam")



# print(p2.number_of_people)  #p2 is class person, does it have a method called number_of_people? No.
# print(Person.number_of_people)

print(Person.amount_of_people())

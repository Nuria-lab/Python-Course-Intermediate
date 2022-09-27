#advantage of using classes

class Student:
    def __init__ (self, name, age, grade):
        self.name= name
        self.age = age
        self.grade=grade   #0 to 100

    def get_grade(self):
        return self.grade


class Course :    #this class will have the ability to add students to a course.
    def __init__ (self,name, max_students):
        self.name = name
        self.max_students = max_students
        self.students = []
        #self.is_active = False   #we can creat attributes that don't need to be assinged at first as a parameter

    def add_student(self,student):
        if len(self.students) < self.max_students : 
            self.students.append(student)
            return True #if student was added succesfully
        return False
    
    def get_average_grade(self):
        value = 0
        for student in self.students:
            value += student.get_grade()
        
        return value/len(self.students)
        
# the students
s1= Student("Tim", 19,95)
s2= Student("Bill",19,75)
s3= Student("Jill",19,60)


# the course
course = Course("Science",2)
course.add_student(s1)
course.add_student(s2)

# print(course.students[0].name)  #accessing attributes
print(course.get_average_grade())

#we can create another course, and add the students needed.
#python to json
import json
# person= {"name":"Nuria","age":36, "city": "La Plata", "hasChildren": False, "titles": ["engineer","programmer"]}
# personJSON= json.dumps(person, indent=4, sort_keys=True)   #dumpS is for a string
# print(personJSON)

# with open('person.json','w') as file:
#     json.dump(person, file, indent=4)                      #dump is for a file, and it opens as a file

#decoding (json to python)
# person= json.loads(personJSON)             #print en consola
# print(person)

# with open('person.json', 'r') as file:
#     person=json.load(file)            #file

# print(person)

#----
class User:
    def  __init__(self, name,age):
        self.name=name
        self.age=age
user= User('Max', 27)

def enconde_user(o):
    if isinstance(o,User):
        return {"name": o.name, "age" :o.age, o.__class__.__name__:True }
    else:
        raise TypeError ('object in type user is not json serializable' )




from json import JSONEncoder

class UserEnconder(JSONEncoder):
    def default(self,o):
        if isinstance(o,User):
            return {"name": o.name, "age" :o.age, o.__class__.__name__:True }
        return JSONEncoder.default(self,o)



userJSON= UserEnconder().encode(user)
print(userJSON)

user=json.loads(userJSON)

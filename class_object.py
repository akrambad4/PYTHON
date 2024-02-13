# Class is a blueprint of an object
# Object is an instance of a class

class Person:
    # properties/attributes/characteristics
    name = "Allan"
    age = 23

    # Method/Function/Behaviour
    def talk(self):
        print("Person is talking")


teacher = Person()
print(teacher.name)
print(teacher.age)

teacher.talk()

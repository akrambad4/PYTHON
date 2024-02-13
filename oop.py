class Person:
    def __init__(self,fistname,age,gender):
        self.firstname = fistname
        self.age = age
        self.gender = gender
    def details (self):
        print(self.firstname,"is studying")

teacher = Person("John",28,"male")
accountant = Person("Mary",21,"female")
doctor = Person("Mark",20,"male")

print(teacher.firstname,teacher.age,teacher.gender)
print(accountant.firstname,accountant.age,accountant.gender)
print(doctor.firstname,doctor.age,doctor.gender)
# inbuilt functions

number = max(89, 70, 49, 123)
print(number)

x = min(89, 70, 49, 123)
print(x)

z = pow(2, 3)
print(z)

# user-defined functions
def name():
    print("Allan")

name()  # Calling a function

def student():
    name = "Vincent"
    age = 18
    course = "MIT"
    print(name, age, course)

student()

def students(name, age, course):
    print(name, age, course)

students("Vincent", 18, "MIT")
students("Henry", 19, "MIT")
students("Mark", 20, "MIT")
students("Maureen", 17, "MIT")
students("Allan", 18, "MIT")
students("Simon", 19, "MIT")
students("Diana", 20, "MIT")
students("Dedan", 22, "MIT")

# create a user-defined function called employees
# displaying details of five employees
# parameters - fname,age,gender,position,salary

def employees(fullname, age, gender, postion, salary):
    print(fullname, age, gender, postion, salary)

employees("Allan", "28", "Male", "CEO", "200,000")
employees("Salma", "38", "Female", "Assistant CEO", "170,000")
employees("Ian", "48", "Male", "HR", "140,000")
employees("Faith", "24", "Female", "Assistant HR", "120,000")
employees("Brian", "68", "Male", "Secretary", "80,000")

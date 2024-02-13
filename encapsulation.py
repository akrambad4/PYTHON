# CHATGPT

class MyClass:
    def __init__(self):
        self.public_var = "I am public"
        self._protected_var = "I am protected"
        self.__private_var = "I am private"

    def public_method(self):
        print("This is a public method")

    def _protected_method(self):
        print("This is a protected method")

    def __private_method(self):
        print("This is a private method")

obj = MyClass()

print(obj.public_var)
print(obj._protected_var)  # Accessing protected variable (not recommended)
# print(obj.__private_var)  # This will result in an AttributeError

obj.public_method()
obj._protected_method()  # Accessing protected method (not recommended)
# obj.__private_method()  # This will result in an AttributeError



# BLACKBOX


class Employee:
    def __init__(self, name, salary):
        self.__name = name  # private variable
        self._salary = salary  # protected variable

    def show(self):
        print("Name: ", self.__name, 'Salary:', self._salary)

    def set_salary(self, salary):
        if salary < 0:
            print("Invalid salary")
        else:
            self._salary = salary

emp = Employee('Jessa', 8000)
emp.show()
emp.set_salary(10000)
emp.show()
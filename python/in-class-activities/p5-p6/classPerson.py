class Person:

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Name: {self.name}"

class Employee(Person):

    def __init__(self, name, position):
        super().__init__(name)
        self.position = position

    def __str__(self):
        return f"Name: {self.name}\nPosition: {self.position}"

e1 = Employee("John", "Boss")
print(e1)

print(Employee.__dict__)
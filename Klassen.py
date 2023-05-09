class MyClass:
    x = 5


p1 = MyClass()
print(p1.x)


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return (f"{self.name} {self.age}")

    def myfunc(self):
        print("Hello my name is " + self.name)

p1 = Person("John", "36")
p1.myfunc()


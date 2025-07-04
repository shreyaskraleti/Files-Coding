# python class-object using __init__:
class Dog:
    def __init__(self,name,breed,age):
        self.name = name
        self.breed = breed
        self.age = age
d1 = Dog("Bonky", "Shitzu", 2)
print(d1.name)
print(d1.breed)
print(d1.age)
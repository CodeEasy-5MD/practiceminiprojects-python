class Person:
    def __init__(self, name, age, weight, height):
        self.name = name
        self.age = age
        self.weight = weight
        self.height = height

    def display(self):
        print(f"| {'name':<10} | {'age':<5} | {'weight':<8} | {'height':<8} |")
        print(f"| {self.name:<10} | {self.age:<5} | {self.weight:<8} | {self.height:<8} |")


person1 = Person("John", 30, 70, 175)
person1.display()


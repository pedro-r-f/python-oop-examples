class Greetings:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def introduce(self):
        print(f'Hi! My name is {self.name} and I am {self.age} years old.')

person = Greetings('Alice', 23)
person.introduce()
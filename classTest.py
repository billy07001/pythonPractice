class Person :
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def intro(self):
        print("Hi I am ",self.name,", and I am ",self.age,"years old")

x = Person("Billy","20")
x.intro()

class Student(Person):
    def __init__(self, name, age, years):
        super().__init__(name, age)
        self.graduationyear = 2022

y= Student("Pio",20,2022)
y.intro()
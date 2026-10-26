class Animal:
    def __init__(self, name):
        self.name = name
        
    def eat(self):
        print(self.name,"is eating.")            
    
    def sleep(self):
        print(self.name, "is sleeping.")
            
    def make_sound(self):
        print(self.name, "makes a sound")


class Lion(Animal):
    def make_sound(self):
        print(f"The {self.name} roars loudly")
    def eat(self):
        print(f"The {self.name} eats fresh meat")
        
class Elephant(Animal):
    def make_sound(self):
            print(f"The {self.name} trumpets")
    def eat(self):
        print(f"The {self.name} eats grass and fruits")

class Monkey(Animal):
    def make_sound(self):
            print(f"The {self.name} chatters")
    def eat(self):
        print(f"The {self.name} eats bananas")

Lion1 = Lion("Lion")
Elephant1 = Elephant("Elephant")
Monkey1 = Monkey("Monkey")


animals = [Lion1, Elephant1, Monkey1]

for animal in animals:
     animal.make_sound()
     animal.eat
     print()
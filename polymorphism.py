#Polymorphism
class Animal():
    def sound(self):
        print("An animal makes sound")
        
class Dog(Animal):
    def sound(self):
        print("A Dog barks")
        
class Cat(Animal):
    def sound(self):
        print("A cat meows")
        
# Function to demonstrate polymorphism by calling sound() on different objects
def make_animal_sound(animal):
    animal.sound()

#Instantiation   
dog1=Dog()
cat1=Cat()
animal=Animal()

# Calling the same method on different objects
make_animal_sound(dog1)
make_animal_sound(cat1)    
                           
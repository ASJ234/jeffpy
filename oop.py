#Inheritance
#Supper class
class Animal:
    def speak(self):
        print("Animal makes sound")
        
#Sub class        
class Dog(Animal):
    def sound(self):
        print("A dog barks")   
        
#Instantiation
Dog1=Dog()
Dog1.speak()
Dog1.sound()            
class Animal:
    
    def __init__(self, name):
        self.name = name
        self.is_alive = True
        
    def eat(self):
        print(f"{self.name} is eating")
        
    def sleep(self):
        print(f"{self.name} is sleeping")
        
    # def speak(self):
        # raise NotImplementedError("Subclass must implement this method")
        
class Dog(Animal):
    # pass
    def speak(self):
        print(f"{self.name} is barking")

class Cat(Animal):
    # pass
    def speak(self):
        print(f"{self.name} is meowing")

class Bird(Animal):
    # pass
    def speak(self):
        print(f"{self.name} is chirping")

dog = Dog("Buddy")
cat = Cat("Whiskers")
bird = Bird("Tweety")

dog.speak()
cat.speak()
bird.speak()
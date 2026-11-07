from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__ (self, name, habitat):
        self.name = name
        self.habitat= habitat

    def display(self):
            print(f"Name: {self.name} | habitat {self.habitat}")

    @abstractmethod
    def speak (self):
                pass

class Dog (Animal):
        def __init__(self,name,habitat, breed):
            super().__init__(name, habitat)
            self.breed = breed

        def speak (self):
            print(f"{self.name} ({self.breed}) says : Woof! Woof!")


dog = Dog ("Bruno", "Home", "German Sheperd")

print("======Animal Sound============")


dog.display()
dog.speak()
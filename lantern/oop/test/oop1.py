class Animal:
    weight = 0
    speed = 0
    force = 0
    song = ""
    descr = "Animal"

    def __init__(self,weight,speed,force):
        self.weight = weight
        self.speed =speed
        self.force = force


    def sound(self):
        print(self.song)

    def run(self):
        print("Speed is ", self.speed)

    def info(self):
        print (f"The  animal {self.descr}  has weight {self.weight} running with speed {self.speed} km/s fighting with force {self.force} and has a song {self.song}")

class Cat(Animal):
    song = "Maoo"
    descr = "cat"

class Dog(Animal):
    song = "Bark"
    descr = "dog"



vilka = Cat(4,10,10)
vilka.info()

blacky = Dog(10,20,30)
blacky.info()


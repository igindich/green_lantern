class Animal:
    weight = 0
    speed = 0
    force = 0
    song = ""

    def sound(self):
        print("")

    def run(self):
        print("Speed is ", self.speed)


class Cat(Animal):
    song = "Maoo"

    def __init__(self,weight,speed,force):
        self.weight = weight
        self.speed =speed
        self.force = force

    def sound(self):
        print(self.song)

    def run(self):
        pass



vilka = Cat(4,10,10)
vilka.sound()

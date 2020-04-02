import random
class Obctacles:
    def __init__(self, x, y):
        self.x = x
        self.y = y
count_obctacles = 3
ob =[]
o = Obctacles
x = 10
y = 15
for i in range(count_obctacles):
    ob.append(o(random.randint(1, x), random.randint(1, y)))

for i in range(len(ob)):
    print(ob[i].x,ob[i].y)
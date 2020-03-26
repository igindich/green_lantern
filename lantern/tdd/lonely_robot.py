
# create Robot with positio and direction
    # check if Robot have missed asteroid while landing
    # create and test turn_left and turn_right function
    # add move forward, move _backward function
    # Check if it falls fro asteroid during movement
    # add asteroid obstacles
    # update robot movement to respect obstacles
    #
import random, curses

class Obctacles:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Asteroid:
    def __init__(self, x, y, count_obctacles):
        self.ob = []
        self.x = x
        self.y = y
        o = Obctacles
        # if count of obctacles not eq zero generating obctacles
        if count_obctacles > 0:
            for i in range(count_obctacles):
                self.ob.append(o(random.randint(1, self.x), random.randint(1, self.y)))

class Robot:
    def __init__(self, x, y, asteroid, direction):
        self.x = x
        self.y = y
        self.asteroid = asteroid
        self.direction = direction
        if self.x > self.asteroid.x or self.y > self.asteroid.y :
            raise MissAsteroidError()

    def turn_left(self):
        turn = {"N":"W", "W":"S", "S":"E", "E":"N"}
        self.direction = turn[self.direction]

    def turn_right(self):
        turn = {"N":"E", "E":"S", "S":"W", "W":"N"}
        self.direction = turn[self.direction]


class MissAsteroidError(Exception):
    pass


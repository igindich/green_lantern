
# create Robot with positio and direction
    # check if Robot have missed asteroid while landing
    # create and test turn_left and turn_right function
    # add move forward, move _backward function
    # Check if it falls fro asteroid during movement
    # add asteroid obstacles
    # update robot movement to respect obstacles
    #       Asteroid abstraction
    #
    #  Y       N
    #  5
    #  4
    #W 3       R          E
    #  2
    #  1
    #  0  1  2  3  4  5   X
    #          S
    #
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
        # if count of obctacles not eq zero random generating obctacles
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

    # checking if robot has possibilities moving current direction
    def __check_move(self):
        #move = {"N": (0, 1), "S": (0, -1), "E": (1, 0), "W": (-1, 0)}
        if self.direction == "N":
            if self.y + 1 > self.asteroid.y:
                raise RobotOutAsteroidError()
        elif self.direction == "S":
            if self.y - 1 < 0:
                raise RobotOutAsteroidError()
        elif self.direction == "W":
            if self.x - 1 < 0:
                raise RobotOutAsteroidError()
        elif self.direction == "E":
            if self.x + 1 > self.asteroid.x:
                raise RobotOutAsteroidError()

    def move(self):
        self.__check_move()
        if self.direction == "N":
            self.y += 1
        elif self.direction == "S":
            self.y -= 1
        elif self.direction == "W":
            self.x -= 1
        elif self.direction == "E":
            self.x += 1

    def turn_left(self):
        turn = {"N": "W", "W": "S", "S": "E", "E": "N"}
        self.direction = turn[self.direction]

    def turn_right(self):
        turn = {"N": "E", "E": "S", "S": "W", "W": "N"}
        self.direction = turn[self.direction]


class MissAsteroidError(Exception):
    pass

class RobotOutAsteroidError(Exception):
    pass

class RobotHasObstaclesError(Exception):
    pass


import pytest
from lonely_robot import Robot, Asteroid, MissAsteroidError


class TestRobotCreation:
    def test_parameters(self):
        x, y = 10, 15
        direction = "N"
        asteroid = Asteroid(x, y, 0)
        robot = Robot(x, y, asteroid, direction)
        assert robot.x == 10
        assert robot.y == 15
        assert robot.asteroid == asteroid
        assert robot.direction == direction

    @pytest.mark.parametrize(
        "asteroid_size,robot_coordinates",
        (
                ((15, 25, 0), (26, 30)),
                ((15, 25, 0), (26, 24)),
                ((15, 25, 0), (15, 27)),

        )
    )
    def test_check_if_robot_on_asteroid(self, asteroid_size, robot_coordinates):
        with pytest.raises(MissAsteroidError):
            asteroid = Asteroid(*asteroid_size)
            Robot(*robot_coordinates, asteroid,"N")

class TestMove:

    def setup(self):
        self.x, self.y = 10, 15
        self.direction = "N"
        self.asteroid = Asteroid(self.x, self.y, 0)

    @pytest.mark.parametrize(
        "current_direction,result",
        (
                [("N", "W"),
                 ("W", "S"),
                 ("S", "E"),
                 ("E", "N")]
        )
    )
    def test_turn_left(self, current_direction, result):
        robot = Robot(self.x, self.y, self.asteroid, current_direction)
        robot.turn_left()
        assert robot.direction == result

    @pytest.mark.parametrize(
        "current_direction,result",
        (
                [("N", "E"),
                 ("E", "S"),
                 ("S", "W"),
                 ("W", "N")]
        )
    )
    def test_turn_right(self, current_direction, result):
        robot = Robot(self.x, self.y, self.asteroid, current_direction)
        robot.turn_right()
        assert robot.direction == result

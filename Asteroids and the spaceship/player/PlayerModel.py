from math import *
from Position import *
from player.TurningSystem import *


class Bullet():
    pass


class PlayerModel():
    turn_speed = pi/32

    def __init__(self, x=0, y=0, angle=3*pi / 2, base_acceleration=1000, speed=0, radius=30):
        self.position = Position(x, y, angle)
        self.base_acceleration = base_acceleration
        self.speed = speed
        self.radius = radius
        self.is_alive = True
        self.time = 0
        self.is_accelerating = False
        self.turning_system = TurningSystem()

    def turn(self):
        self.position.angle += self.turn_speed * self.turning_system.get_direction()

    def slowdown(self):
        if self.speed < 4:
            self.speed = 0
        self.speed -= self.speed/4

    def shoot(self):
        # спавнит буллеты в направлении angle
        print("пиу пиу пиу")

    def move(self, delta_time):
        moving = self.speed * delta_time
        self.position.x += moving * cos(self.position.angle)
        self.position.y += moving * sin(self.position.angle)

    def accelarate(self, delta_time):
        if self.is_accelerating:
            self.speed += delta_time * self.base_acceleration

    def stop(self):
        self.speed = 0

    def is_alive(self):
        return self.is_alive

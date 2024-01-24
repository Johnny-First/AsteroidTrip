import math

from player.PlayerModel import *
from player.PlayerView import *

class PlayerController:
    def __init__(self, model: PlayerModel, view: PlayerView):
        self.model = model
        self.view = view

    def Update(self, delta_time):
        self.model.Move(delta_time)
        self.view.Move(self.model.position, self.model.radius, self.model.position.angle)
        self.model.Accelarate(delta_time)
        self.model.Turn()
    def Motion(self, event: tkinter.Event):
        self.view.spaceship.SetAngle(Position(event.x, event.y))

    def Brake(self):
        self.model.SlowDown()

    def Accelerate(self, delta_time):
        self.model.Accelarate(delta_time)

    def get_radius(self):
        return self.model.radius

    def get_position(self):
        return self.model.position

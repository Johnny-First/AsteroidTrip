from player.PlayerModel import *
from player.PlayerView import *


class PlayerController:
    def __init__(self, model: PlayerModel, view: PlayerView):
        self.model = model
        self.view = view

    def update(self, delta_time):
        self.model.move(delta_time)
        self.view.move(self.model.position, self.model.radius, self.model.position.angle)
        self.model.accelarate(delta_time)
        self.model.turn()

    def motion(self, event: tkinter.Event):
        self.view.spaceship.set_angle(Position(event.x, event.y))

    def brake(self):
        self.model.slowdown()

    def accelerate(self, delta_time):
        self.model.accelarate(delta_time)

    def get_radius(self):
        return self.model.radius

    def get_position(self):
        return self.model.position

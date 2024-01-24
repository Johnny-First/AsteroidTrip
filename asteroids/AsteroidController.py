from asteroids.AsteroidModel import AsteroidModel
from asteroids.AsteroidView import AsteroidView


class AsteroidController:
    def __init__(self, model: AsteroidModel, view: AsteroidView):
        self.view = view
        self.model = model

    def update(self,delta_time, player_position, player_angle):
        self.model.update(delta_time)
        self.view.set_position(player_position, player_angle, self.model.asteroids)

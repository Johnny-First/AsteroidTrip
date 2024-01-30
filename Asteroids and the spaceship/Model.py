from player.PlayerModel import PlayerModel
from asteroids.AsteroidModel import *


class Model:
    def __init__(self):
        self.player_model = PlayerModel()
        self.asteroid_model = AsteroidModel()

    def check_collision(self, object_1, object_2):
        if object_1.radius + object_2.radius <= object_1.position.get_distance(object_2.position):
            print(f"{object_1}, {object_2} столкнулись!!")

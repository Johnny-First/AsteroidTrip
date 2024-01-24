from Position import Position
from asteroids.AsteroidGenerator import *

class AsteroidModel:
    def __init__(self):
        self.asteroid_generator = AsteroidGenerator()
        self.player_position = Position()
        self.asteroids = self.asteroid_generator.add_asteroids([], 49, self.player_position)



    def update(self, delta_time):
        for asteroid in self.asteroids:
            asteroid.move(delta_time)
            if asteroid.position.get_distance(self.player_position) >= 1000:
                self.asteroids = self.asteroid_generator.add_asteroids(self.asteroids, 1, self.player_position)
                self.asteroids.remove(asteroid)



    def set_player_position(self, player_position):
        self.player_position = player_position
        self.asteroid_generator.set_player_position(player_position)

    def spawn_asteroids(self, how_many = 5):
        angle = self.player_position.angle
        if len(self.asteroids) < how_many:
            self.asteroid_generator.add_asteroids(self.asteroids, how_many - len(self.asteroids), self.player_position)
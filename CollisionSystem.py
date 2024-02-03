from Position import *


class CollisionSystem:
    def is_collision_player_with_asteroids(self, player_radius, player_position: Position, asteroids):
        for asteroid in asteroids:
            if player_radius + asteroid.radius > player_position.get_distance(asteroid.position):
                return True
        return False

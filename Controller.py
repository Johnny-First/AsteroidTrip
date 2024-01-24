from CollisionSystem import CollisionSystem
from player.PlayerController import *
from InputSystem import *
from asteroids.AsteroidController import *
from Model import *
from View import *




class Controller:
    def __init__(self, model: Model, view: View):
        self.model = model
        self.view = view

        self.view.OnUpdate(self.Update)

        self.asteroid_controller = AsteroidController(self.model.asteroid_model, self.view.asteroid_view)
        self.player_controller = PlayerController(self.model.player_model, self.view.player_view)

        self.view.OnMotion(self.Motion)
        self.input_system = InputSystem(self.KeyPress, self.KeyRelease)
        self.collision_system = CollisionSystem()
        self.view.StartView()
    def Motion(self, event: tkinter.Event):
        self.player_controller.Motion(event)

    def KeyPress(self, key):
        key = str(key)[1]
        if key == "w":
            self.player_controller.model.is_accelerating = True
        if key == "a":
            self.player_controller.model.turning_system.press_left()
        if key == "d":
            self.player_controller.model.turning_system.press_right()
        if key == "s":
            self.player_controller.Brake()
    def KeyRelease(self, key):
        key = str(key)[1]
        if key == "w":
            self.player_controller.model.is_accelerating = False
        if key == "a":
            self.player_controller.model.turning_system.release_left()
        if key == "d":
            self.player_controller.model.turning_system.release_right()
    def Update(self, delta_time):
        if self.collision_system.is_collision_player_with_asteroids(self.player_controller.get_radius(),
                                                                    self.player_controller.get_position(),
                                                                    self.asteroid_controller.model.asteroids):
            print('\n\n\n\n\n\n\n')
            print("SMERT PRISHLA!!! PIPEZ TEBE!")
        self.asteroid_controller.update(delta_time, self.player_controller.model.position, self.player_controller.model.position.angle)
        self.player_controller.Update(delta_time)
        self.model.asteroid_model.set_player_position(self.model.player_model.position)
        self.model.asteroid_model.spawn_asteroids()

import tkinter
from player.PlayerView import *
import time
from asteroids.AsteroidView import *



class View:
    def __init__(self):
        self.HEIGHT = 1000
        self.root = tkinter.Tk()
        self.root.geometry(f"{self.HEIGHT}x{self.HEIGHT}+0+0")
        self.canvas = tkinter.Canvas(height=self.HEIGHT, width=self.HEIGHT, background="#11003b")
        self.bg = tkinter.PhotoImage(file="stars.png")
        self.canvas.create_image(500, 500, image=self.bg)

        self.canvas.pack()


        self.root.update()
        self.asteroid_view = AsteroidView(self.HEIGHT, self.root, self.canvas)
        self.player_view = PlayerView(self.HEIGHT, self.root, self.canvas)

    def on_motion(self, motion):
        self.root.bind("<Motion>", motion)

    def start_view(self):
        self.player_view.start_view()
        self.game_loop()

    def game_loop(self):
        global delta_time
        while True:
            self.root.update()
            self.update_controller(delta_time)
            time.sleep(delta_time)

    def on_motion(self, func):
        self.root.bind("<Motion>", func)

    def on_update(self, function):
        self.update_controller = function

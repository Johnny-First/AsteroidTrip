from player.PlayerView import *
import tkinter
from tkinter import ttk
from asteroids.AsteroidView import *


class View():
    def __init__(self):
        self.HEIGHT = 1000
        self.root = tkinter.Tk()
        self.root.geometry(f"{self.HEIGHT}x{self.HEIGHT}+0+0")
        self.canvas = tkinter.Canvas(height=self.HEIGHT, width=self.HEIGHT, background="#11003b")
        self.canvas.pack()

        self.root.update()
        self.asteroid_view = AsteroidView(self.HEIGHT, self.root, self.canvas)
        self.player_view = PlayerView(self.HEIGHT, self.root, self.canvas)

    def OnMotion(self, motion):
        self.root.bind("<Motion>", motion)
    def StartView(self):
        self.player_view.StartView()
        self.GameLoop()
    def GameLoop(self):
        global delta_time
        while True:
            self.root.update()
            self.update_controller(delta_time)
            time.sleep(delta_time)

    def OnMotion(self, func):
        self.root.bind("<Motion>", func)

    def OnUpdate(self, function):
        self.update_controller = function


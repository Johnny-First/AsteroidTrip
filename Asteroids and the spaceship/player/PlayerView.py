
from player.Spaceship import *


from Position import *

FPS = 60
delta_time = 1 / FPS


class PlayerView:
    def __init__(self, height, root, canvas: tkinter.Canvas):
        self.HEIGHT = height
        self.root = root
        self.canvas = canvas
        #self.ship_png = tkinter.PhotoImage(file="./p",)
        #canvas.create_image(500, 500, image=self.ship_png)
        #self.spaceship = Spaceship(self.canvas)
        self.position_UI = self.canvas.create_text(100, 100, text="---", fill="white")

    def move(self, position: Position, radius, angle):
        self.canvas.delete(self.position_UI)
        self.position_UI = self.canvas.create_text(100, 100, text=f"{position}", fill="white")
        #self.spaceship.set_spaceship(position, radius, angle)

    def start_view(self):
        self.bg1 = tkinter.PhotoImage(file="asteroids/meteora.png", height=50, width=50)
        self.canvas.create_image(500, 500, image=self.bg1)
        #self.spaceship.set_spaceship(Position(1, 1), 50, 1)
        pass


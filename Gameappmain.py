import player.PlayerController as pc
from View import *
from Controller import *
from Model import *

import player.PlayerModel as pm

model = Model()
view = View()
controller = Controller(model, view)


#class file for sim.py

import random
import matplotlib.pyplot as plt
import matplotlib.patches as pat

#team colour codes:
class Car():
    def __init__ (self, team, driver, colour, pos):
        self.team = team
        self.driver = driver
        self.colour =  colour
        self.pos = pos


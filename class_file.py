#class file for sim.py

import random
import matplotlib.pyplot as plt
import matplotlib.patches as pat

#team colour codes:
class Car():
    def __init__ (self, team, driver):
        self.team = team
        self.driver = driver
        self.colour =  team_colours.get(team, "gray")


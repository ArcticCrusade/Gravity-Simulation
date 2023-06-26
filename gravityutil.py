import random
from math import floor


G = 4

class Planet:
    x_accel = 0
    y_accel = 0
    
    def __init__(self, start_pos, mass):
        self.x_velocity = random.randint(-150, 150)
        self.y_velocity = random.randint(-150, 150)
        self.x_pos = start_pos[0]
        self.y_pos = start_pos[1]
        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.mass = mass
        self.radius = floor((31.6 * self.mass / 100000) ** (1 / 2.5))

    def get_pos(self):
        return [self.x_pos, self.y_pos]

def calculate_accel(planet1, planet2):
    if id(planet1) == id(planet2):
        return [0, 0]
    mass = planet2.mass
    x_dist = planet1.x_pos - planet2.x_pos
    y_dist = planet1.y_pos - planet2.y_pos

    distance = max((x_dist ** 2 + y_dist ** 2) ** .5, planet1.radius ** 2)
    x_force = G * mass * x_dist / (distance ** 3)
    y_force = G * mass * y_dist / (distance ** 3)
    return [-x_force, -y_force]
    


# Workarround for importing in pygamezero
import sys; sys.path.append('.')

from car import *

class World:
    WIDTH = 800
    HEIGHT = 600

    def __init__(self, objects=[]):
        self.objects = list(objects)

    def update(self, dt):
        for obj in self.objects:
            obj.update(dt)

    def draw(self):
        for obj in self.objects:
            obj.draw()

    def add(self, obj):
        self.objects.append(obj)



# Starting pygamezero simulation
world = World()

def update(dt):
    screen.clear()
    world.update(dt)

def draw():
    world.draw()

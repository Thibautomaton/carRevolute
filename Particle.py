import pygame
from Box2D.b2 import circleShape

from settings import *

class Particle():
    def __init__(self, x_, y_, r_, world):

        self.x = x_
        self.y = y_
        self.r = r_


        self.lifespan = 255


        self.display_surface = pygame.display.get_surface()

        self.body = world.CreateDynamicBody(
            position = pixelToWorld((self.x, self.y))
        )

        cs = circleShape(
            radius = scalarPixelToWorld(self.r)
        )

        self.body.CreateFixture(
            shape = cs,
            density = 1,
            friction = 0.3,
            restitution = 0.5
        )

    def display(self):
        color = (175, 175, 175)
        self.lifespan-=1

        pygame.draw.circle(self.display_surface, color, worldToPixel(self.body.transform.position), self.r)

    def isDead(self):
        if self.lifespan<0:
            return True
        else:
            return False
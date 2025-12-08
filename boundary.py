import pygame.draw
from Box2D.b2 import chainShape
from Box2D import b2World
from settings import *

class Boundary():
    def __init__(self, world):

        self.display_surface = pygame.display.get_surface()

        self.surface = [ (0, HEIGHT/2), (150, 2*HEIGHT/3), (WIDTH/2, HEIGHT/2), (WIDTH-300, HEIGHT/3), (WIDTH, HEIGHT/3), (WIDTH, HEIGHT), (0, HEIGHT)]

        self.ground_body = world.CreateStaticBody(
            position = (0, 0)
        )


        vertices = []

        for surface in self.surface:
            vertices.append(pixelToWorld(surface))

        chain = chainShape(vertices =vertices)

        self.ground_body.CreateFixture(
            shape = chain,
            density = 1,
            friction = 1,
            restitution = 0.5
        )

    def display(self):
        pygame.draw.polygon(self.display_surface, (0, 255, 0), self.surface)
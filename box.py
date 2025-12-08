from time import sleep

import pygame
import math
from settings import pixelToWorld, scalarPixelToWorld, worldToPixel
from Box2D.b2 import polygonShape, fixtureDef
from Box2D import b2Filter

class Box():
    CATEGORY_BOX = 0x0001
    MASK_BOX = 0xFFFF & ~0x0002
    def __init__(self, x_, y_, w_, h_, world):
        self.x = x_
        self.y = y_

        self.w = w_
        self.h = h_

        self.display_surface = pygame.display.get_surface()

        self.body = world.CreateDynamicBody(
            position = pixelToWorld((self.x, self.y))

        )
        box2dW = scalarPixelToWorld(self.w/2)
        box2dH = scalarPixelToWorld(self.h/2)

        ps = polygonShape(
            box = (box2dW, box2dH)
        )

        fixture = fixtureDef(
            shape = ps,
            density = 1,
            friction = 1,
            restitution = 0,
        )

        f = (self.body.CreateFixture(fixture))

        f.filter = b2Filter(categoryBits=0x0001, maskBits=0xFFFF & ~0x0002)

    def display(self):
        color = (175, 175, 175)
        border = (0, 0, 255)

        rect_surface = pygame.Surface((self.w, self.h), pygame.SRCALPHA)

        pygame.draw.rect(rect_surface, color, (0, 0, self.w, self.h))
        pygame.draw.rect(rect_surface, border, (0, 0, self.w, self.h), 2)

        angle_degrees = math.degrees(self.body.transform.angle)

        rotated_surface = pygame.transform.rotate(rect_surface, angle_degrees)

        rotated_rect = rotated_surface.get_rect(center = worldToPixel(self.body.transform.position))

        self.display_surface.blit(rotated_surface, rotated_rect)


    def rotate(self, angle):
        self.body.transform.angle = angle





















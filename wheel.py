import pygame.draw

from settings import pixelToWorld, scalarPixelToWorld, worldToPixel
from Box2D.b2 import circleShape, fixtureDef

from Box2D import b2Filter

class Wheel():
    CATEGORY_WHEEL = 0x0002
    MASK_WHEEL = 0xFFFF & ~0x0001

    def __init__(self, x_, y_, r_, world):
        self.x = x_
        self.y = y_

        self.r = r_
        self.display_surface = pygame.display.get_surface()

        self.body = world.CreateDynamicBody(
            position = pixelToWorld((self.x, self.y))
        )

        cs = circleShape(
            radius = scalarPixelToWorld(self.r)
        )

        fixture = fixtureDef(
            shape = cs,
            restitution = 0,
            friction = 1,
            density = 0.2
        )

        f = self.body.CreateFixture(fixture)

        f.filter = b2Filter(categoryBits=0x0002, maskBits=0xFFFF & ~0x0001)


    def display(self):
        color=(175, 175, 175)
        border = (255, 255, 255)

        pygame.draw.circle(self.display_surface, color, worldToPixel(self.body.position), self.r)
        pygame.draw.circle(self.display_surface, border, worldToPixel(self.body.position), self.r, 2)
        #
        # pygame.draw.line(self.display_surface, (0, 0, 0), (self.x, self.y), (self.body.transform.angle))


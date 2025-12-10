# This is a sample Python script.
import sys

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import pygame
import Box2D
import random
from Box2D.b2 import world
from settings import *
from boundary import Boundary
from Particle import Particle

from Car import Car

pygame.init()

display_surface = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("car")

clock = pygame.time.Clock()

world = world(gravity = (0, -10), doSleep = False)

boundary = Boundary(world)

car = Car(WIDTH-170, 250, world)

particles = []
k=0
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()

    display_surface.fill((0, 0, 0))

    boundary.display()


    k+=1
    if k%3==0:
        particles.append(Particle(random.uniform(WIDTH/2-200, WIDTH/2 + 200), 0, random.uniform(1, 10), world))

    for p in particles:
        p.display()

    car.run()

    if pygame.mouse.get_pressed()[0]:
        # car.whjd1.motorSpeed = 100
        car.rjd1.motorEnabled = True


    world.Step(STEP, 6, 2)
    clock.tick(TARGET_FPS)
    pygame.display.update()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/

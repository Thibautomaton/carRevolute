import math
from wheel import Wheel
from box import Box
import Box2D
from Box2D import b2Vec2

class Car():
    def __init__(self, x, y, world):
        self.FWheel = Wheel(x-130, y+70, 45, world)
        self.BWheel = Wheel(x+130, y+70, 45, world)

        self.mainFrame = Box(x, y, 300, 150,world)

        # self.whjd1 = world.CreateWheelJoint(
        #     bodyA = self.mainFrame.body,
        #     bodyB = self.FWheel.body,
        #     anchor = self.FWheel.body.worldCenter,
        #     axis = (0, 1),
        #     frequencyHz = 4.0,
        #     dampingRatio = 0.7,
        #     enableMotor = True,
        #     maxMotorTorque = 20,
        #     motorSpeed = 0
        #
        # )


        self.rjd1 = world.CreateRevoluteJoint(
            bodyA = self.mainFrame.body,
            bodyB = self.FWheel.body,
            anchor = (self.FWheel.body.worldCenter),
            motorSpeed = math.pi,
            maxMotorTorque = 10000.0,
            enableMotor = False
        )

        self.rjd2 = world.CreateRevoluteJoint(
            bodyA = self.mainFrame.body,
            bodyB = self.BWheel.body,
            anchor = (self.BWheel.body.worldCenter),
            motorSpeed = math.pi,
            maxMotorTorque = 1000.0,
            enableMotor = False
        )

        # self.prisjoint1 = world.CreatePrismaticJoint(
        #     bodyA = self.mainFrame.body,
        #     bodyB = self.FWheel.body,
        #     anchor = self.FWheel.body.worldCenter,
        #     axis = (0,1),
        #     enableLimit = True,
        #     lowerTranslation = -1,
        #     upperTranslation = 1,
        #     enableMotor = False
        # )

        # self.prisjoint2 = world.CreatePrismaticJoint(
        #     bodyA = self.mainFrame.body,
        #     bodyB = self.BWheel.body,
        #     anchor = self.BWheel.body.worldCenter,
        #     axis = (0,1),
        #     enableLimit = True,
        #     lowerTranslation = -0.5,
        #     upperTranslation = 0.5,
        #     enableMotor = False
        # )


    # def toggleMotor(self):
    #     motorstatus = self.rjd1.isMotorEnabled()
    #     self.rjd1.enableMotor(not motorstatus)
    #

    def run(self):
        # dx = self.BWheel.body.transform.position.x - self.FWheel.body.transform.position.x
        # dy = self.BWheel.body.transform.position.y - self.FWheel.body.transform.position.y
        # desired_angle = math.atan2(dy, dx)
        #
        # print(desired_angle)
        #
        # # Option A: direct
        # self.mainFrame.body.transform.angle = math.radians(desired_angle)



        self.FWheel.display()
        self.BWheel.display()
        self.mainFrame.display()

    def reverse(self):
        self.rjd1.motorSpeed *=-1
        self.rjd2.motorSpeed *=-1


import DefensePaths as defensePaths
import SpaceJamClasses as spaceJamClasses
from panda3d.core import Vec3
from math import pi, sin, cos
import math, sys, random
from direct.showbase.ShowBase import ShowBase
from direct.task import Task
from panda3d.core import WindowProperties

class MyApp(ShowBase):

    def __init__(self):
        ShowBase.__init__(self)

        windowTitle = WindowProperties()
        windowTitle.setTitle("Space Jam")
        self.win.requestProperties(windowTitle)

        # It's very important to get rid of code bloat as much as possible. We got rid of many lines in this script just by using classes.
        self.Universe = spaceJamClasses.Universe(self.loader, "./Assets/Universe/Universe.x", self.render, 'Universe', "./Assets/Universe/jeremy-thomas-4dpAqfTbvKA-unsplash.jpg", (0, 0, 0), 15000)
        self.Planet1 = spaceJamClasses.Planet(self.loader, "./Assets/Planets/protoPlanet.x", self.render, 'Planet1', "./Assets/Planets/2k_earth_daymap.jpg", (-6000, -3000, -800), 250)
        self.Planet2 = spaceJamClasses.Planet(self.loader, "./Assets/Planets/protoPlanet.x", self.render, 'Planet2', "./Assets/Planets/2k_jupiter.jpg", (1500, 5000, 280), 250) 
        self.Planet3 = spaceJamClasses.Planet(self.loader, "./Assets/Planets/protoPlanet.x", self.render, 'Planet3', "./Assets/Planets/2k_venus_surface.jpg", (3000, 5000, -1000), 250)
        self.Planet4 = spaceJamClasses.Planet(self.loader, "./Assets/Planets/protoPlanet.x", self.render, 'Planet4', "./Assets/Planets/2k_neptune.jpg", (300, 6000, 500), 150) 
        self.Planet5 = spaceJamClasses.Planet(self.loader, "./Assets/Planets/protoPlanet.x", self.render, 'Planet5', "./Assets/Planets/2k_mars.jpg", (-1000, 5000, -1000), 450) 
        self.Planet6 = spaceJamClasses.Planet(self.loader, "./Assets/Planets/protoPlanet.x", self.render, 'Planet6', "./Assets/Planets/2k_mercury.jpg", (0, -900, -1400), 700) 
        self.SpaceStation1 = spaceJamClasses.SpaceStation(self.loader, "./Assets/SpaceStation/spaceStation.egg", self.render, 'Space Station', "./Assets/SpaceStation/SpaceStation1_Dif2.png", (1500, 1000, -100), 40) 
        self.Hero = spaceJamClasses.PlayerSpaceship (self.loader, "./Assets/Spaceships/Dumbledore/Dumbledore.egg", self.render, 'Hero', "./Assets/Spaceships/Dumbledore/spacejet_C.png", Vec3(1000, 1200, -50), 50)

        self.CameraDefense(self.loader, self.render)
        self.DroneSpawn()

    def CameraDefense(self, loader, render):
        parent = loader.loadModel("./Assets/DroneDefender/Camera/sphere.egg")
        texture = loader.loadTexture("./Assets/DroneDefender/Camera/sphere1_flat.jpg")
        parent.setTexture(texture, 1)
        defensePaths.Camera(render, parent, 'x-axis', 40, (255, 0, 0, 1.0), 'xy')
        defensePaths.Camera(render, parent, 'y-axis', 37, (0, 255, 0, 1.0), 'yz')
        defensePaths.Camera(render, parent, 'z-axis', 34, (0, 0, 255, 1.0), 'xz')

    def DrawBaseballSeams(self, centralobject, droneName, step, numSeams, radius = 1): 
        unitVec = defensePaths.BaseballSeams (step, numSeams, B = 0.4)
        unitVec.normalize()
        position = unitVec * radius * 250 + centralobject.modelNode.getPos()
        spaceJamClasses.Drone(self.loader, "./Assets/DroneDefender/DroneDefender.obj", self.render, droneName, "./Assets/DroneDefender/octotoad1_auv.png", position, 5)

    def DrawCloudDefense(self, centralobject, droneName):
        unitVec = defensePaths.Cloud()
        unitVec.normalize()
        position = unitVec * 500 + centralobject.modelNode.getPos()
        spaceJamClasses.Drone(self.loader, "./Assets/DroneDefender/DroneDefender.obj", self.render, droneName, "./Assets/DroneDefender/octotoad1_auv.png", position, 10)
    
    def DroneSpawn(self):
        fullCycle = 60
        for j in range(fullCycle):
            spaceJamClasses.Drone.droneCount += 1
            nickName = "Drone" + str(spaceJamClasses.Drone.droneCount)
            self.DrawCloudDefense(self.Planet1, nickName)
            self.DrawBaseballSeams(self.Planet4, nickName, j, fullCycle, 2)

app = MyApp()
app.run()
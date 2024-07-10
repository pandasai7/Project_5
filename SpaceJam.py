from direct.showbase.ShowBase import ShowBase
from panda3d.core import CollisionTraverser, CollisionHandlerPusher

import math, sys, random
import SpaceJamClasses 
import DefensePaths
import Player



class MyApp(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
   
        SetupScene(self)
        SetCamera(self)
        #SetMovement(self)
        Collisions(self)  

def SetupScene(self):

    self.rootAssetFolder = './Assets'
    #UNIVERSE
    self.Universe = SpaceJamClasses.Universe(self.loader, self.rootAssetFolder + "/Universe/Universe.x", self.render, 'Universe', self.rootAssetFolder + "/Universe/universe.jpg", (0, 0, 0), 16000)

    self.Planet1 = SpaceJamClasses.Planet(self.loader, self.rootAssetFolder + "/Planets/protoPlanet.x", self.render, 'Planet1', self.rootAssetFolder + "/Planets/earth.jpg", (1000, 0, 0), 250)
    self.Planet2 = SpaceJamClasses.Planet(self.loader, self.rootAssetFolder + "/Planets/protoPlanet.x", self.render, 'Planet2', self.rootAssetFolder + "/Planets/loaf.jpg", (3000, 6000, 0), 300)
    self.Planet3 = SpaceJamClasses.Planet(self.loader, self.rootAssetFolder + "/Planets/protoPlanet.x", self.render, 'Planet3', self.rootAssetFolder + "/Planets/mars.jpg", (7000, -5000, 0), 500)
    self.Planet4 = SpaceJamClasses.Planet(self.loader, self.rootAssetFolder + "/Planets/protoPlanet.x", self.render, 'Planet4', self.rootAssetFolder + "/Planets/purple.jpg", (9000, 6000, 200), 150)
    self.Planet5 = SpaceJamClasses.Planet(self.loader, self.rootAssetFolder + "/Planets/protoPlanet.x", self.render, 'Planet5', self.rootAssetFolder + "/Planets/saturn.jpg", (10000, -2000, 500), 500)
    self.Planet6 = SpaceJamClasses.Planet(self.loader, self.rootAssetFolder + "/Planets/protoPlanet.x", self.render, 'Planet6', self.rootAssetFolder + "/Planets/shamrock.jpg", (12000, -2000, 100), 700)
    
    self.SpaceStation1 = SpaceJamClasses.SpaceStation(self.loader, self.rootAssetFolder + "/Space Station/SpaceStation1B/spaceStation.egg", self.render, 'Space Station', (1500, 1000, -100), 40)

    self.Hero = Player.Spaceship(self.loader, self.taskMgr, self.accept, self.rootAssetFolder + "/Dumbledore/Dumbledore.egg", self.render, 'Hero', self.rootAssetFolder + "/Dumbledore/spacejet_C.png", (100, 200, -50), 50)

    #Baseball Seams
    for i in range(100):
        step = i
        droneName = 'drone' + str(i)
        droneCoords = DrawBaseballSeams(self, self.Planet1, droneName, step, 50)
        self.DroneObj = SpaceJamClasses.Drone(self.loader, "./Assets/DroneDefender/DroneDefender.obj", self.render, droneName, "./Assets/DroneDefender/octotoad1_auv.png", droneCoords, 5)
        i = i + 1
    #X
    for i in range(100):
        step = i
        droneName = 'drone' + str(i)
        droneCoords = DrawXSeams(self, self.Planet2, droneName, step, 150)
        self.DroneObj = SpaceJamClasses.Drone(self.loader, "./Assets/DroneDefender/DroneDefender.obj", self.render, droneName, "./Assets/DroneDefender/octotoad1_auv.png", droneCoords, 5)
        i = i + 1
    #Y
    for i in range(100):
        step = i
        droneName = 'drone' + str(i)
        droneCoords = DrawYSeams(self, self.Planet3, droneName, step, 150)
        self.DroneObj = SpaceJamClasses.Drone(self.loader, "./Assets/DroneDefender/DroneDefender.obj", self.render, droneName, "./Assets/DroneDefender/octotoad1_auv.png", droneCoords, 5)
        i = i + 1
    #Z
    for i in range(100):
        step = i
        droneName = 'drone' + str(i)
        droneCoords = DrawZSeams(self, self.Planet4, droneName, step, 150)
        self.DroneObj = SpaceJamClasses.Drone(self.loader, "./Assets/DroneDefender/DroneDefender.obj", self.render, droneName, "./Assets/DroneDefender/octotoad1_auv.png", droneCoords, 5)
        i = i + 1
    #Cloud
    for i in range(100):
        step = i
        droneName = 'drone' + str(i)
        droneCoords = DrawCloudDefense(self, self.Planet5, droneName)
        self.DroneObj = SpaceJamClasses.Drone(self.loader, "./Assets/DroneDefender/DroneDefender.obj", self.render, droneName, "./Assets/DroneDefender/octotoad1_auv.png", droneCoords, 5)
        i = i + 1

def DrawBaseballSeams(self, centralObject, droneName, step, numSeams, radius = 4.1):
    unitVec = DefensePaths.BaseballSeams(step, numSeams, B = 0.4)
    unitVec.normalize()
    position = unitVec * radius * 250 + centralObject.modelNode.getPos()
    return position

def DrawXSeams(self, centralObject, droneName, step, numSeams, radius = 4.1):
    unitVec = DefensePaths.XSeams(step, numSeams, B = 0.4)
    unitVec.normalize()
    position = unitVec * radius * 250 + centralObject.modelNode.getPos()
    return position

def DrawYSeams(self, centralObject, droneName, step, numSeams, radius = 4.1):
    unitVec = DefensePaths.YSeams(step, numSeams, B = 0.4)
    unitVec.normalize()
    position = unitVec * radius * 250 + centralObject.modelNode.getPos()
    return position

def DrawZSeams(self, centralObject, droneName, step, numSeams, radius = 4.1):
    unitVec = DefensePaths.ZSeams(step, numSeams, B = 0.4)
    unitVec.normalize()
    position = unitVec * radius * 250 + centralObject.modelNode.getPos()
    return position
    
def DrawCloudDefense(self, centralObject, droneName):
    unitVec = DefensePaths.DrawCloud()
    unitVec.normalize()
    position = unitVec * 1250 + centralObject.modelNode.getPos()
    SpaceJamClasses.Drone(self.loader, "./Assets/DroneDefender/DroneDefender.obj", self.render, droneName, "./Assets/DroneDefender/octotoad1_auv.png", position, 10)
    SpaceJamClasses.Drone.droneCount += 1
    nickName = "Drone" + str(SpaceJamClasses.Drone.droneCount)
    return position

def SetCamera(self):
    self.disableMouse() # disables the default panda mouse movement controls
    self.camera.reparentTo(self.Hero.modelNode)
    self.camera.setFluidPos(0, 1, 0)

def SetMovement(self):
    SpaceJamClasses.Player.Thrust(self, 'space')

def Collisions(self):
    self.cTrav = CollisionTraverser()
    self.cTrav.traverse(self.render)
    self.pusher = CollisionHandlerPusher()
    self.pusher.addCollider(self.Hero.collisionNode, self.Hero.modelNode)
    self.cTrav.addCollider(self.Hero.collisionNode, self.pusher)
    self.cTrav.showCollisions(self.render)

app = MyApp()
app.run()
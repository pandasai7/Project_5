from CollideObjectBase import SphereCollideObject
from panda3d.core import Loader, NodePath, Vec3
from direct.task.Task import TaskManager
from typing import Callable
from direct.task import Task
import math, sys, random


class Spaceship(SphereCollideObject):
    def __init__(self, loader: Loader, taskMgr: TaskManager, accept: Callable[[str, Callable], None], modelPath: str, parentNode: NodePath, nodeName: str, texPath: str, posVec: Vec3, scaleVec: float):
        super(Spaceship, self).__init__(loader, modelPath, parentNode, nodeName, Vec3(0, 0, 0), 1)
        self.taskMgr = taskMgr
        self.accept = accept
        self.modelNode.setPos(posVec)
        self.modelNode.setScale(scaleVec)
        self.modelNode.setName(nodeName)
        tex = loader.loadTexture(texPath)
        self.modelNode.setTexture(tex, 1)
        

    #def SetKeyBindings(self):
        #Mouse Control
        #base.disableMouse()
        #base.camera.setPos(-10.0, -15.0, 0.0)
        #base.camera.setHpr(0.0, 0.0, 0.0)
        
        #controls---------
        #quit
        self.accept('escape', self.quit)
        
        #left
        self.accept('arrow_left', self.negativeX, [1]) #LeftPressed
        self.accept('arrow_left-up', self.negativeX, [0]) #LeftReleased

        #right
        self.accept('arrow_right', self.positiveX, [1]) #RightPressed
        self.accept('arrow_right-up', self.positiveX, [0]) #RightReleased

        #up
        self.accept('arrow_up', self.positiveY, [1]) #RightPressed
        self.accept('arrow_up-up', self.positiveY, [0]) #RightReleased

        #down
        self.accept('arrow_down', self.negativeY, [1]) #RightPressed
        self.accept('arrow_down-up', self.negativeY, [0]) #RightReleased

        #self.SetKeyBindings()

    def negativeX(self, keyDown):
        if(keyDown):
            self.taskMgr.add(self.moveNegativeX, 'moveNegativeX')
        else:
                self.taskMgr.remove('moveNegativeX')
    def positiveX(self, keyDown):
        if(keyDown):
            self.taskMgr.add(self.movePositiveX, 'movePositiveX')
        else:
                self.taskMgr.remove('movePositiveX')
    def negativeY(self, keyDown):
        if(keyDown):
            self.taskMgr.add(self.moveNegativeY, 'moveNegativeY')
        else:
                self.taskMgr.remove('moveNegativeY')
    def positiveY(self, keyDown):
        if(keyDown):
            self.taskMgr.add(self.movePositiveY, 'movePositiveY')
        else:
                self.taskMgr.remove('movePositiveY')

    def quit(self):
        sys.exit()

    def moveNegativeX(self, task):
       self.setX((-10, 0, 0))
       return task.cont

    def movePositiveX(self, task):
        self.setX((10, 0, 0))
        return task.cont

    def moveNegativeY(self, task):
        self.setY((0, -10, 0))
        return task.cont

    def movePositiveY(self, task):
        self.setY((0, 10, 0))
        return task.cont
    
    def Thrust(self, keyDown):
        if keyDown:
            self.taskMgr.add(self.ApplyThrust(self, 'forward-thrust'), 'forward-thrust')
        else:
            self.taskMgr.remove('forward-thrust')
    def ApplyThrust(self, task):
        rate = 5
        trajectory = self.render.getRelativeVector(self.modelNode, Vec3.forward())
        trajectory.normalize()
        self.modelNode.setFluidPos(self.modelNode.getPos() + trajectory * rate)
        return Task.cont
    def SetKeyBindings(self):
        self.accept('space', self.Thrust, [1])
        self.accept('space-up', self.Thrust, [0])
    def LeftTurn(self, keyDown):
        if keyDown:
            self.taskManager.add(self.ApplyLeftTurn, 'left-turn')
        else:
            self.taskManager.remove('left-turn')
    def ApplyLeftTurn(self, task):
        rate = .5
        self.modelNode.setH(self.modelNode.getH() + rate)
        return Task.cont
    def setX(self, speed):
        oldPos = self.modelNode.getPos()
        newPos = oldPos + speed
        self.modelNode.setPos(newPos)
    def setY(self, speed):
        oldPos = self.modelNode.getPos()
        newPos = oldPos + speed
        self.modelNode.setPos(newPos)
    def setZ(self, speed):
        oldPos = self.modelNode.getPos()
        newPos = oldPos + speed
        self.modelNode.setPos(newPos)
    def setX(self, speed):
        oldPos = self.modelNode.getPos()
        newPos = oldPos + speed
        self.modelNode.setPos(newPos)

        return newPos
from direct.showbase.ShowBase import ShowBase
from panda3d.core import *
from direct.task import Task
from CollideObjectBase import *

class Planet(ShowBase):
    def __init__(self, loader: Loader, modelPath: str, parentNode: NodePath, nodeName: str, texPath: str, posVec: Vec3, scaleVec: float):
        self.modelNode = loader.loadModel(modelPath) #loads model to modelNode
        self.modelNode.reparentTo(parentNode) #reparents to parentNode, likely the camera (self.render)
        self.modelNode.setPos(posVec) #sets the position of the modelNode
        self.modelNode.setScale(scaleVec) #sets the scale of the modelNode

        self.modelNode.setName(nodeName) #sets the name of the modelNode
        tex = loader.loadTexture(texPath) #loads a texture to object tex
        self.modelNode.setTexture(tex, 1) #applies the loaded texture tex to modelNode
class Drone(ShowBase):
    droneCount = 0
    def __init__(self, loader: Loader, modelPath: str, parentNode: NodePath, nodeName: str, texPath: str, posVec: Vec3, scaleVec: float):
        self.modelNode = loader.loadModel(modelPath) #loads model to modelNode
        self.modelNode.reparentTo(parentNode) #reparents to parentNode, likely the camera (self.render)
        self.modelNode.setPos(posVec) #sets the position of the modelNode
        self.modelNode.setScale(scaleVec) #sets the scale of the modelNode

        self.modelNode.setName(nodeName) #sets the name of the modelNode
        tex = loader.loadTexture(texPath) #loads a texture to object tex
        self.modelNode.setTexture(tex, 1) #applies the loaded texture tex to modelNode
        
class Universe(InverseSphereCollideObject):
    def __init__(self, loader: Loader, modelPath: str, parentNode: NodePath, nodeName: str, texPath: str, posVec: Vec3, scaleVec: float):
        super(Universe, self).__init__(loader, modelPath, parentNode, nodeName, Vec3(0, 0, 0), 0.9)
        self.modelNode = loader.loadModel(modelPath) #loads model to modelNode
        self.modelNode.setPos(posVec)
        self.modelNode.setScale(scaleVec)
        self.modelNode.setName(nodeName)
        tex = loader.loadTexture(texPath)
        self.modelNode.setTexture(tex, 1)

class SpaceStation(CapsuleCollidableObject):
    def __init__(self, loader: Loader, modelPath: str, parentNode: NodePath, nodeName: str, posVec: Vec3, scaleVec: float):
        super(SpaceStation, self).__init__(loader, modelPath, parentNode, nodeName, 1, -1, 5, 1, -1, -5, 10)
        self.modelNode = loader.loadModel(modelPath) #loads model to modelNode
        self.modelNode.setPos(posVec)
        self.modelNode.setScale(scaleVec)
        
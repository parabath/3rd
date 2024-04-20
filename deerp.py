from panda3d.core import Point3
from direct.showbase.ShowBase import ShowBase
from panda3d.core import loadPrcFileData
from deerpl import setup_point_light, setup_ambient_light
from direct.actor.Actor import Actor

configVars ="""
win-size 1270 720
show-frame-rate-meter 1
"""

loadPrcFileData("",configVars)

class MyGame(ShowBase):
    def __init__(self):
        super().__init__()
        #self.set_background_color(0,0,0,1)
        self.cam.setPos(0,-10,2)

        #self.model = Actor("my-models/dance",{"anim1":"my-models/dance-dancing"})
        #self.model.loop("anim1")
        #self.model.reparentTo(self.render)
        self.model=Actor('deer.gltf')
        self.model.reparentTo(self.render)
        self.model.loop("rund")

        setup_point_light(self.model,(5,0,5))
        setup_ambient_light(self.model)

            # Set initial velocity
        self.velocity = Point3(0, 0, 0)

        # Register key handlers
        self.accept("w", self.set_velocity, ["forward"])
        self.accept("a", self.set_velocity, ["left"])
        self.accept("s", self.set_velocity, ["backward"])
        self.accept("d", self.set_velocity, ["right"])
        self.accept("w-up", self.set_velocity, ["stop"])
        self.accept("a-up", self.set_velocity, ["stop"])
        self.accept("s-up", self.set_velocity, ["stop"])
        self.accept("d-up", self.set_velocity, ["stop"])    

    def rotate_cube(self, task):
        dt = globalClock.getDt()  # Get delta time    
        self.cube.setPos(self.cube.getPos() + self.velocity * dt)
        return task.cont
    
    def set_velocity(self, direction):
        if direction == "forward":
            self.velocity.setY(1)
        elif direction == "backward":
            self.velocity.setY(-1)
        elif direction == "left":
            self.velocity.setX(-1)
        elif direction == "right":
            self.velocity.setX(1)
        elif direction == "stop":
            self.velocity.setX(0)
            self.velocity.setY(0)

game = MyGame()
game.run()

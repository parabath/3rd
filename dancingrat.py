from direct.showbase.ShowBase import ShowBase
from panda3d.core import loadPrcFileData
from dancingratl import setup_point_light, setup_ambient_light
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
        self.model=Actor('dancingr.gltf')
        self.model.reparentTo(self.render)
        self.model.loop("dancing")

        setup_point_light(self.model,(5,0,5))
        setup_ambient_light(self.model)


game = MyGame()
game.run()

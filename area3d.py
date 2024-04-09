from panda3d.core import Point3
from direct.showbase.ShowBase import ShowBase

class MyApp(ShowBase):
    def __init__(self):
        super().__init__()

        # Load a 3D model (your .glb model)
        self.cube = self.loader.loadModel("cardboard_box.glb")
        self.cube.reparentTo(self.render)
        self.cube.setScale(0.1)  # Adjust the scale as needed
        self.cube.setPos(0, 0, 0)

        # Rotate the cube smoothly
        self.taskMgr.add(self.rotate_cube, "rotate_cube")

        # Disable culling to prevent model disappearance
        self.cube.setTwoSided(True)

    def rotate_cube(self, task):
        dt = globalClock.getDt()  # Get delta time
        self.cube.setH(self.cube.getH() + 30 * dt)  # Rotate at 30 degrees per second
        return task.cont

if __name__ == "__main__":
    app = MyApp()
    app.run()

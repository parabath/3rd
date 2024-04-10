from panda3d.core import Point3
from direct.showbase.ShowBase import ShowBase

class MyApp(ShowBase):
    def __init__(self):
        super().__init__()

        # Load a 3D model (your .glb model)
        self.cube = self.loader.loadModel("clash_of_clans_-_grand_warden.glb")
        self.cube.reparentTo(self.render)
        self.cube.setScale(0.5)  # Adjust the scale as needed
        self.cube.setPos(0, 0, 0)

        # Rotate the cube smoothly
        self.taskMgr.add(self.rotate_cube, "rotate_cube")

        # Disable culling to prevent model disappearance
        self.cube.setTwoSided(True)

        # Set initial velocity
        self.velocity = Point3(2, 0, 0)

        # Register key handlers
        self.accept("w", self.set_velocity, ["forward"])
        self.accept("a", self.set_velocity, ["left"])
        self.accept("s", self.set_velocity, ["backward"])
        self.accept("d", self.set_velocity, ["right"])
        self.accept("w-up", self.set_velocity, ["stop"])
        self.accept("a-up", self.set_velocity, ["stop"])
        self.accept("s-up", self.set_velocity, ["stop"])
        self.accept("d-up", self.set_velocity, ["stop"])

    #def rotate_cube(self, task):
        #dt = globalClock.getDt()  # Get delta time
        #self.cube.setH(self.cube.getH() + 30 * dt)  # Rotate at 30 degrees per second

        # Move the cube based on velocity
        #self.cube.setPos(self.cube.getPos() + self.velocity * dt)

        #return task.cont
    def rotate_cube(self, task):
        dt = globalClock.getDt()  # Get delta time
        self.cube.setH(self.cube.getH() + 1* dt)  # Rotate horizontally (around Y-axis)
        self.cube.setP(self.cube.getP() + 8 * dt)  # Rotate vertically (around X-axis) by 90 degrees
        self.cube.setPos(self.cube.getPos() + self.velocity * dt)  # Move the cube based on velocity
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

if __name__ == "__main__":
    app = MyApp()
    app.run()
